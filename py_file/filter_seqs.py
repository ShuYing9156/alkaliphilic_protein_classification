from func import *

input_fasta = ['./negative_data/ncbi/ncbi_neg.fasta',
               './negative_data/pdb/pdb_neg.fasta',
               './negative_data/uniprot/uniprot_neg.fasta']

output_fasta = ['./negative_data/ncbi/ncbi_neg_filtered.fasta',
                './negative_data/pdb/pdb_neg_filtered.fasta',
                './negative_data/uniprot/uniprot_neg_filtered.fasta']


for i in range( len(input_fasta) ):
    print(f'Processing {input_fasta[i]}')
    filter_seqs(input_fasta[i], output_fasta[i])
    count = count_seqs(output_fasta[i])

print("All sequences have been filtered and counted.")
















