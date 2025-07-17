from func import *

exe = './cd-hit-v4.8.1-2019-0228/cd-hit-2d'
input1 = './negative_data/uniprot/uniprot_neg_fil_cdhit40.fasta'

input2 = ['./negative_data/ncbi/ncbi_neg_filtered.fasta',
          './negative_data/pdb/pdb_neg_filtered.fasta']

output = ['./negative_data/ncbi/ncbi_uniprot_cdhit2d40.fasta',
          './negative_data/pdb/pdb_uniprot_cdhit2d40.fasta']

identity = 0.4
word_size = 2
threads = 23


for i in range(len(input2)):
    print(f'Running CD-HIT-2D for {input2[i]} against {input1}')

    run_cdhit2d(exe,
                input1,
                input2[i],
                output[i],
                identity,
                word_size,
                threads)



