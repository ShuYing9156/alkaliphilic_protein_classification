from func import *

datalist = ['./positive_data_fasta/NCBI_fasta/seqs.fasta',
            './positive_data_fasta/NCBI_fasta/filtered_seqs.fasta',
            './positive_data_fasta/NCBI_fasta/filtered_seqs_uni.fasta',
            './positive_data_fasta/pdb_fasta/pdb_all_seqs.fasta',
            './positive_data_fasta/pdb_fasta/filtered_pdb_seqs.fasta',
            './positive_data_fasta/pdb_fasta/filtered_pdb_seqs_uni.fasta',
            './positive_data_fasta/uniprot_fasta/uniprotkb_seqs.fasta',
            './positive_data_fasta/uniprot_fasta/filtered_uniprot_seqs.fasta',
            './positive_data_fasta/uniprot_fasta/filtered_uniprot_seqs_40.fasta']

for i in datalist :
    # print(i)
    count = count_seqs(i)
    print(f'There are {count} seqs in {i}')

