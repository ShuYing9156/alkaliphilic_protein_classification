from func import *

#根據給定的FASTA檔案，將 all_fasta_file 寫入不同的FASTA檔案
all_fasta_file = './all_fasta/all40.fasta'
filtered_ncbi = './negative_data_fasta/ncbi_negative_filtered.fasta'
filtered_uniprot = './negative_data_fasta/uniprot_negative_filtered.fasta'
filtered_pdb = './negative_data_fasta/pdb_negative_filtered.fasta'

original_files = [filtered_ncbi, filtered_uniprot, filtered_pdb]

ncbi_branch = './all_fasta/all40_ncbi.fasta'
uniprot_branch = './all_fasta/all40_uniprot.fasta'
pdb_branch = './all_fasta/all40_pdb.fasta'

output_files = [ncbi_branch, uniprot_branch, pdb_branch]


all2three(all_fasta_file = all_fasta_file,
          original_files = original_files,
          output_files = output_files)


