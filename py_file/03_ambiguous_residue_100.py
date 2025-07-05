from func import *

#根據長度和模糊殘基條件過濾FASTA檔案中的序列。
ncbi_seqs_fasta = './negative_data_fasta/ncbi_negative.fasta'
uniprot_seqs = './negative_data_fasta/uniprot_negative.fasta'
pdb_seqs_fasta = './negative_data_fasta/pdb_negative.fasta'

filtered_ncbi = './negative_data_fasta/ncbi_negative_filtered.fasta'
filtered_uniprot = './negative_data_fasta/uniprot_negative_filtered.fasta'
filtered_pdb = './negative_data_fasta/pdb_negative_filtered.fasta'

residues = ['B', 'J', 'o', 'U', 'X', 'Z']


filter_seqs(input_file = ncbi_seqs_fasta,
            output_file = filtered_ncbi,
            min_length = 100,
            ambiguous_residues = residues)

filter_seqs(input_file = uniprot_seqs,
            output_file = filtered_uniprot,
            min_length = 100,
            ambiguous_residues = residues)

filter_seqs(input_file = pdb_seqs_fasta,
            output_file = filtered_pdb,
            min_length = 100,
            ambiguous_residues = residues)


