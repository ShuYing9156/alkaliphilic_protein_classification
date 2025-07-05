from func import *

#用CD-HIT2D將NCBI_negative.fasta與UniProt_negative40.fasta比較
exe = './cd-hit-v4.8.1-2019-0228/cd-hit-2d'
input_file1 = './positive_data_fasta/uniprot_fasta/filtered_uniprot_seqs_40.fasta'
input_file2 = './positive_data_fasta/pdb_fasta/filtered_pdb_seqs.fasta'
input_file3 = './positive_data_fasta/NCBI_fasta/filtered_seqs.fasta'
output1 = './positive_data_fasta/pdb_fasta/filtered_pdb_seqs_uni.fasta'
output2 = './positive_data_fasta/NCBI_fasta/filtered_seqs_uni.fasta'
identity = 0.4
word_size = 2
threads = 20


# run_cdhit2d(exe, input_file1, input_file2, output1, identity, word_size, threads)


run_cdhit2d(exe, input_file1, input_file3, output2, identity, word_size, threads)



