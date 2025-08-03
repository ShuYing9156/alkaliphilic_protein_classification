from func import run_cdhit, run_cdhit2d

cdhit_exe = './cd-hit-v4.8.1-2019-0228/cd-hit'

input_files = ['./negative_data/cdhit2d/neg_ncbifil_pdbfil.fasta',
               './positive_data/cdhit2d/pos_ncbifil_pdbfil.fasta']

output_files = ['./negative_data/cdhit2d/neg_ncbipdb_cdhit40.fasta',
                './positive_data/cdhit2d/pos_ncbipdb_cdhit40.fasta']

identity = 0.4
word_size = 2
threads = 23
search_clustering = True
sequence_filter = True

for input, output in zip(input_files, output_files):
    print('Processing input:', input)

    run_cdhit(cdhit_exe,
              input,
              output,
              identity,
              word_size,
              threads,
              search_clustering,
              sequence_filter)



cdhit2d_exe = './cd-hit-v4.8.1-2019-0228/cd-hit-2d'
input1 = './negative_data/uniprot/uniprot_neg_fil_cdhit40.fasta'
# input2 = cdhit output
output = ['./negative_data/cdhit2d/cdhit2d40_neg_to_uniprot.fasta',
          './positive_data/cdhit2d/cdhit2d40_pos_to_uniprot.fasta']

identity = 0.4
word_size = 2
threads = 23


for input2, output_file in zip(output_files, output):
    print(f'Running CD-HIT2D for {input2} against {input1}')

    run_cdhit2d(cdhit2d_exe,
                input1,
                input2,
                output_file,
                identity,
                word_size,
                threads)



