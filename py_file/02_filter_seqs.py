from func import *

input_fasta = ['./positive_data/ncbi/ncbi_pos.fasta',
               './positive_data/pdb/pdb_pos.fasta',
               './positive_data/uniprot/uniprot_pos.fasta']

output_fasta = ['./positive_data/ncbi/ncbi_pos_filtered.fasta',
                './positive_data/pdb/pdb_pos_filtered.fasta',
                './positive_data/uniprot/uniprot_pos_filtered.fasta']


for i in range( len(input_fasta) ):
    print(f'Processing {input_fasta[i]}')
    filter_seqs(input_fasta[i], output_fasta[i])
    count = count_seqs(output_fasta[i])

print("All sequences have been filtered and counted.")
















