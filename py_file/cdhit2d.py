from func import *

exe = './cd-hit-v4.8.1-2019-0228/cd-hit-2d'
input1 = './negative_data/uniprot/uniprot_neg_fil_cdhit40.fasta'

input2 = ['./negative_data/cdhit2d/neg_ncbifil_pdbfil.fasta',
          './positive_data/cdhit2d/pos_ncbifil_pdbfil.fasta']

output = ['./negative_data/cdhit2d/cdhit2d40_neg_to_uniprot.fasta',
          './positive_data/cdhit2d/cdhit2d40_pos_to_uniprot.fasta']

identity = 0.4
word_size = 2
threads = 23


for input2_file, output_file in zip(input2, output):
    print(f'Running CD-HIT2D for {input2_file} against {input1}')

    run_cdhit2d(exe,
                input1,
                input2_file,
                output_file,
                identity,
                word_size,
                threads)



