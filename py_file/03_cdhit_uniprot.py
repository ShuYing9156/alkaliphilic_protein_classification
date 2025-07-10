from func import *

exe = './cd-hit-v4.8.1-2019-0228/cd-hit'
input = './positive_data/uniprot/uniprot_pos_filtered.fasta'
output = './positive_data/uniprot/uniprot_pos_fil_cdhit40.fasta'
identity = 0.4
word_size = 2
threads = 23
search_clustering = True
sequence_filter = True

run_cdhit(exe,
          input,
          output,
          identity,
          word_size,
          threads,
          search_clustering,
          sequence_filter)