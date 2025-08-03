import random
from Bio import SeqIO

# 設定檔案路徑
input_list = ['./positive_data/cdhit2d/pos_cdhit2d_ncbi_branch.fasta',
              './positive_data/uniprot/uniprot_pos_fil_cdhit40.fasta',
              './negative_data/cdhit2d/neg_cdhit2d_pdb_branch.fasta']  # 請替換為你的輸入fasta檔案路徑

output_list = ['./positive_data/cut_fasta_file/cut_pos_ncbi.fasta',
               './positive_data/cut_fasta_file/cut_pos_uniprot.fasta',
               './negative_data/cut_fasta_file/cut_neg_pdb.fasta']  # 輸出的隨機子集fasta檔案

num_to_extract = [21673,
                  15179,
                  126]# 要抽取的序列數量


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
