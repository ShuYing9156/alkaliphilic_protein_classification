from Bio import Entrez
from Bio import SeqIO
import pandas as pd
import subprocess

__all__ = ['fetch_ncbi_ids',
         'fetch_ncbi_seqs',
         'csv2fasta',
         'filter_seqs',
         'count_seqs',
         'merge_fasta_files',
         'run_cdhit',
         'all2three',
         'run_cdhit2d']

def fetch_ncbi_ids(email, term, filename, db="protein", retmax=100):
    """
    從NCBI的蛋白質數據庫中查詢符合條件的蛋白質ID，並將其寫入檔案。

    參數:
    email (str): 使用者的電子郵件
    term (str): 查詢的關鍵字
    filename (str): 將ID寫入的檔案名稱
    db (str): 查詢的數據庫，預設為 "protein"
    retmax (int): 每次查詢返回的最大記錄數，預設為100
    """
    # 設置電子郵件
    Entrez.email = email

    # 獲取總記錄數
    handle = Entrez.esearch(db=db, term=term)
    record = Entrez.read(handle)
    total_records = int(record["Count"])
    handle.close()

    # 分頁查詢
    for start in range(0, total_records, retmax):
        handle = Entrez.esearch(db=db, term=term, retmax=retmax, retstart=start)
        record = Entrez.read(handle)
        handle.close()

        # 將id寫入檔案
        with open(filename, mode='a+', encoding='utf-8') as idlist_file:
            for id in record['IdList']:
                idlist_file.write(f'{id}\n')

        # 印出當前頁的id
        print(f"Records {start + 1} to {start + len(record['IdList'])}")


def fetch_ncbi_seqs(email, id_file, output_file, retmax=100):
    """
    從NCBI查詢FASTA序列並將結果寫入檔案。

    參數：
    email (str): 使用者電子郵件。
    id_file (str): 包含蛋白質ID的檔案名稱。
    output_file (str): 輸出FASTA檔案的名稱。
    retmax (int): 每次查詢的最大記錄數（預設為100）。
    """
    # 設置電子郵件
    Entrez.email = email

    # 讀檔並將ID合成list
    idlist = []
    with open(id_file, mode='r', encoding='utf-8') as idlist_file:
        for line in idlist_file:
            idlist.append(line.strip())

    print(f"Total IDs: {len(idlist)}")
    print(f"Type of idlist: {type(idlist)}")

    # 查詢每個ID的FASTA
    with open(output_file, "a+") as fasta_file:
        for start in range(0, len(idlist), retmax):
            # 分批取出ID
            batch_ids = idlist[start:start + retmax]
            ids = ",".join(batch_ids)  # 將ID合併成逗號分隔的字串
            handle = Entrez.efetch(db="protein", id=ids, rettype="fasta", retmode="text")
            fasta_data = handle.read()  # 讀取FASTA資料
            handle.close()
            # 寫入檔案
            fasta_file.write(fasta_data)
            print(f"Records {start + 1} to {start + len(batch_ids)} downloaded.")


def csv2fasta(csv_file, fasta_file):
    """
    將CSV檔案中的PDB序列轉換為FASTA格式並寫入檔案。

    參數：
    csv_file (str): 輸入的CSV檔案名稱。
    fasta_file (str): 輸出的FASTA檔案名稱。
    """
    # 讀取CSV檔案
    all_seqs = pd.read_csv(csv_file)

    # 選取需要的欄位
    seqs_needed = all_seqs[['Entry ID', 'Sequence']]
    
    # 寫入FASTA檔案
    with open(fasta_file, 'w') as fasta_file:
        for _, row in seqs_needed.iterrows():
            entry_id = row['Entry ID']
            sequence = row['Sequence']
            if pd.notna(entry_id) and pd.notna(sequence):
                fasta_file.write(f">{entry_id}\n{sequence}\n")


def filter_seqs(input_file, output_file, min_length=100, ambiguous_residues=None):
    """
    過濾FASTA檔案中的序列，根據長度和模糊殘基條件。

    參數：
    input_file (str): 輸入的FASTA檔案名稱。
    output_file (str): 輸出的過濾後FASTA檔案名稱。
    min_length (int): 最小序列長度，預設為100。
    ambiguous_residues (list): 模糊殘基列表，預設為None。
    """
    if ambiguous_residues is None:
        ambiguous_residues = ['B', 'J', 'o', 'U', 'X', 'Z']  # 預設模糊殘基

    sequence_count = 0

    with open(input_file, 'r') as input_fasta, open(output_file, 'w') as output_fasta:
        for record in SeqIO.parse(input_fasta, 'fasta'):
            sequence = str(record.seq)

            # 檢查序列長度和模糊殘基
            if len(sequence) > min_length and not any(res in ambiguous_residues for res in sequence):
                SeqIO.write(record, output_fasta, 'fasta')
                sequence_count += 1

    print(f"過濾完成，結果已寫入 {output_file}")
    print(f"{output_file} 有 {sequence_count} 筆序列資料。")


def count_seqs(fasta_file):
    """
    計算FASTA檔案中的序列數量。

    參數：
    fasta_file (str): 要計算序列數量的FASTA檔案名稱。

    返回：
    int: 序列的數量。
    """
    count = 0

    for record in SeqIO.parse(fasta_file, "fasta"):
        count += 1

    return count


def merge_fasta_files(fasta_files, output_file):
    """
    將多個FASTA檔案合併成一個檔案。

    參數：
    fasta_files (list): 要合併的FASTA檔案路徑列表，例如 ['file1.fasta', 'file2.fasta', 'file3.fasta']
    output_file (str): 輸出的合併後的FASTA檔案名稱
    """
    merged_records = []

    for fasta in fasta_files:
        # 讀取每個FASTA檔案
        records = list(SeqIO.parse(fasta, "fasta"))
        merged_records.extend(records)

    # 將所有序列寫入新的FASTA檔案
    SeqIO.write(merged_records, output_file, "fasta")
    print(f"合併完成，結果已寫入 {output_file}")


def run_cdhit(executable, input_file, output_file, identity, word_size, threads=1, search_clustering=False, sequence_filter=False):
    """
    執行 CD-HIT 指令。

    參數：
    executable (str): CD-HIT 的可執行檔名稱。
    input_file (str): 輸入的FASTA檔案名稱。
    output_file (str): 輸出的FASTA檔案名稱。
    identity (float): 相似度閾值。
    word_size (int): 框架長度。
    threads (int): 使用的執行緒數量，預設為 1。
    search_clustering (bool): 是否啟用 -sc 參數，預設為 False。
    sequence_filter (bool): 是否啟用 -sf 參數，預設為 False。
    """
    command = [
        executable,  # CD-HIT 的可執行檔名稱
        "-i", input_file,  # 輸入檔案
        "-o", output_file,  # 輸出檔案
        "-c", str(identity),  # 相似度閾值
        "-n", str(word_size),  # 框架長度
        "-T", str(threads)  # 執行緒數量
    ]

    # 添加 -sc 和 -sf 參數
    if search_clustering:
        command.append("-sc")
    if sequence_filter:
        command.append("-sf")

    try:
        subprocess.run(command, check=True)
        print(f"CD-HIT 執行成功，結果已寫入 {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"CD-HIT 執行失敗: {e}")


def all2three(all_fasta_file, original_files, output_files):
    """
    根據給定的序列 ID 過濾序列，並將其寫入不同的 FASTA 檔案。

    參數：
    all_fasta_file (str): 包含所有序列的FASTA檔案名稱。
    original_files (list): 3個FASTA檔案的名稱列表。
    output_files (list): 輸出的FASTA檔案名稱列表，對應於3個FASTA檔案。
    """
    # 讀取 all.fasta 中的所有序列 ID
    all_ids = set()
    for record in SeqIO.parse(all_fasta_file, "fasta"):
        all_ids.add(record.id)

    # 讀取過濾的序列 ID
    filtered_ids = [set() for _ in original_files]
    for i, filtered_file in enumerate(original_files):
        for record in SeqIO.parse(filtered_file, "fasta"):
            filtered_ids[i].add(record.id)

    # 準備寫入不同的 FASTA 檔案
    records = [[] for _ in output_files]

    for record in SeqIO.parse(all_fasta_file, "fasta"):
        seq_id = record.id
        for i, filtered_id in enumerate(filtered_ids):
            if seq_id in filtered_id:
                records[i].append(record)
                break  # 找到對應的 ID 後就可以跳出循環

    # 寫入到不同的 FASTA 檔案
    for records_list, output_file in zip(records, output_files):
        SeqIO.write(records_list, output_file, "fasta")

    print("序列已成功寫入各自的 FASTA 檔案。")


def run_cdhit2d(executable, input_file1, input_file2, output_file, identity, word_size, threads=1):
    """
    執行 CD-HIT-2D 指令。

    參數：
    executable (str): CD-HIT-2D 的可執行檔名稱。
    input_file1 (str): 第一個輸入的FASTA檔案名稱。
    input_file2 (str): 第二個輸入的FASTA檔案名稱。
    output_file (str): 輸出的FASTA檔案名稱。
    identity (float): 相似度閾值。
    word_size (int): 框架長度。
    threads (int): 使用的執行緒數量，預設為 1。
    """
    command = [
        executable,  # CD-HIT-2D 的可執行檔名稱
        "-i", input_file1,  # 第一個輸入檔案
        "-i2", input_file2,  # 第二個輸入檔案
        "-o", output_file,  # 輸出檔案
        "-c", str(identity),  # 相似度閾值
        "-n", str(word_size),  # 框架長度
        "-T", str(threads)  # 執行緒數量
    ]

    try:
        subprocess.run(command, check=True)
        print(f"CD-HIT-2D 執行成功，結果已寫入 {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"CD-HIT-2D 執行失敗: {e}")

