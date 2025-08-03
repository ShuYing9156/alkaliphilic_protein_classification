import random
from Bio import SeqIO
from func import count_seqs
import os
import shutil

# 設定檔案路徑
input_list = ['./positive_data/cdhit2d/pos_cdhit2d_ncbi_branch.fasta',
              './positive_data/uniprot/uniprot_pos_fil_cdhit40.fasta',
              './negative_data/cdhit2d/neg_cdhit2d_pdb_branch.fasta']  # 請替換為你的輸入fasta檔案路徑

output_list = ['./final_data/positive_ncbi.fasta',
               './final_data/positive_uniprot.fasta',
               './final_data/negative_pdb.fasta']  # 輸出的隨機子集fasta檔案

base_line = ['./negative_data/cdhit2d/neg_cdhit2d_ncbi_branch.fasta',
             './negative_data/uniprot/uniprot_neg_fil_cdhit40.fasta',
             './positive_data/cdhit2d/pos_cdhit2d_pdb_branch.fasta']

num_to_extract = [count_seqs(base_line[0]),
                  count_seqs(base_line[1]),
                  count_seqs(base_line[2])] # 要抽取的序列數量

# 原始檔案路徑與新檔案名稱對應（可以自行修改）
files_to_copy = {
    base_line[0]: "negative_ncbi.fasta",
    base_line[1]: "negative_uniprot.fasta",
    base_line[2]: "positive_pdb.fasta",
}

os.makedirs('./final_data', exist_ok=True)

for input_file, output_file, num in zip(input_list, output_list, num_to_extract):
    # 讀取所有序列
    all_records = list(SeqIO.parse(input_file, "fasta"))
    
    # 確認序列總數
    total_sequences = len(all_records)
    print(f"原始檔案中共有 {total_sequences} 筆序列")

    # 檢查抽取數量是否合理
    if num > total_sequences:
        print(f"錯誤：要抽取的數量 ({num}) 大於總序列數 ({total_sequences})")
        exit(1)
    
    # 隨機抽取序列
    random_subset = random.sample(all_records, num)

    # 將抽取的序列寫入新檔案
    SeqIO.write(random_subset, output_file, "fasta")

    print(f"已成功從 {total_sequences} 筆序列中隨機抽取 {num} 筆")
    print(f"隨機抽取的序列已保存至 {output_file}")

for src, new_name in files_to_copy.items():
    dst = os.path.join('./final_data', new_name)
    shutil.copy2(src, dst)  # copy2會保留檔案的metadata
    print(f"Copied {src} to {dst}")


# # 讀取所有序列
# all_records = list(SeqIO.parse(input_fasta, "fasta"))

# # 確認序列總數
# total_sequences = len(all_records)
# print(f"原始檔案中共有 {total_sequences} 筆序列")

# # 要抽取的序列數量
# num_to_extract = 46301

# # 檢查抽取數量是否合理
# if num_to_extract > total_sequences:
#     print(f"錯誤：要抽取的數量 ({num_to_extract}) 大於總序列數 ({total_sequences})")
#     exit(1)

# # 隨機抽取序列
# random_subset = random.sample(all_records, num_to_extract)

# # 將抽取的序列寫入新檔案
# SeqIO.write(random_subset, output_fasta, "fasta")

# print(f"已成功從 {total_sequences} 筆序列中隨機抽取 {num_to_extract} 筆")
# print(f"隨機抽取的序列已保存至 {output_fasta}")
