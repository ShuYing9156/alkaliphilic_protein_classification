from func import *

#將多個FASTA檔案合併成一個檔案
filtered_ncbi = './negative_data_fasta/ncbi_negative_filtered.fasta'
filtered_uniprot = './negative_data_fasta/uniprot_negative_filtered.fasta'
filtered_pdb = './negative_data_fasta/pdb_negative_filtered.fasta'

files = [filtered_ncbi, filtered_uniprot, filtered_pdb]
all_seqs = './all_fasta/all.fasta'


merge_fasta_files(fasta_files = files,
                  output_file = all_seqs)

