from Bio import SeqIO

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



if __name__ == "__main__":
    fasta_files = ['./final_data/negative_ncbi.fasta',
                   './final_data/negative_pdb.fasta',
                   './final_data/negative_uniprot.fasta',
                   './final_data/positive_ncbi.fasta',
                   './final_data/positive_pdb.fasta',
                   './final_data/positive_uniprot.fasta']
    
    for fasta_file in fasta_files:
        total_seqs = count_seqs(fasta_file)
        print(f"There are {total_seqs} seqs in {fasta_file}")