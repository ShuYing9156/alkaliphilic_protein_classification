from func import *

#用CD-HIT將相似的序列聚類
exe = './cd-hit-v4.8.1-2019-0228/cd-hit'

'''
input_file = [filtered_ncbi, filtered_uniprot, filtered_pdb]
output_file = []
identity = [40, 50, 60, 70, 80, 90, 95]
dataset = ['ncbi', 'uniprot', 'pdb']

for i in dataset:
    for j in identity:
        output_file.append(f'./cdhit_result/{i}{j}.fasta')

word_size = [2, 3, 4, 5, 5, 5, 5]
sc = True
sf = True

output_index = 0

for file in input_file:
    count_identity = 0
    count_word_size = 0
    
    for k in range(7):
        run_cdhit(executable = exe,
                  input_file = file,
                  output_file = output_file[output_index + k],
                  identity = identity[count_identity - 1],
                  word_size = word_size[count_word_size - 1],
                  search_clustering = sc,
                  sequence_filter = sf)
        
        count_identity += 1
        count_word_size += 1
    
    output_index += 7
'''

input_file = './positive_data_fasta/uniprot_fasta/filtered_uniprot_seqs.fasta'
output = './positive_data_fasta/uniprot_fasta/filtered_uniprot_seqs_40.fasta'
identity = 0.4
word_size = 2
threads = 20

run_cdhit(executable = exe,
          input_file = input_file,
          output_file = output,
          identity = identity,
          word_size = word_size,
          threads = threads,
          search_clustering = True,
          sequence_filter = True)

print(count_seqs(output))

