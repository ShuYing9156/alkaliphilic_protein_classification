from func import *

exe = './cd-hit-v4.8.1-2019-0228/cd-hit-2d'
input1 = './positive_data/uniprot/uniprot_pos_fil_cdhit40.fasta'

input2 = ['./positive_data/ncbi/ncbi_pos_filtered.fasta',
          './positive_data/pdb/pdb_pos_filtered.fasta']

output = ['./positive_data/ncbi/ncbi_uniprot_cdhit2d40.fasta',
          './positive_data/pdb/pdb_uniprot_cdhit2d40.fasta']

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



