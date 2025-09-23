import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataPreprocessingClasses.FastaProcessor import FastaProcessor
from DataPreprocessingClasses.RunCDHIT import ForCDHIT
from count_seq import count_seqs


folders = ['./positive_data/all_data',
           './negative_data/all_data',
           './final_data']

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f'{folder} has been created.')
    
    else:
        print(f'{folder} was existed.')


pos_files = FastaProcessor(input_file = ['./positive_data/ncbi/positive_ncbi_cdhit2d_branch.fasta',
                                         './positive_data/uniprot/positive_uniprot_cdhit.fasta',
                                         './positive_data/pdb/positive_pdb_cdhit2d_branch.fasta'],
                            output_file = './positive_data/all_data/positive_all_data.fasta')


neg_files = FastaProcessor(input_file = ['./negative_data/ncbi/negative_ncbi_cdhit2d_branch.fasta',
                                         './negative_data/uniprot/negative_uniprot_cdhit.fasta',
                                         './negative_data/pdb/negative_pdb_cdhit2d_branch.fasta'],
                            output_file = './negative_data/all_data/negative_all_data.fasta')


pos_all_data = pos_files.merge_fasta_files()
neg_all_data = neg_files.merge_fasta_files()


for_cdhit2d = ForCDHIT(exe = './cd-hit-v4.8.1-2019-0228/cd-hit-2d',
                       input_file = neg_all_data,
                       output_file = './negative_data/all_data/negative_all_cdhit2d.fasta',
                       threads = 23)

neg_all_cdhit2d = for_cdhit2d.cdhit2d(reference_file = pos_all_data)


pos_split = FastaProcessor(input_file = pos_all_data,
                           output_file = ['./positive_data/all_data/positive_ncbi.fasta',
                                          './positive_data/all_data/positive_uniprot.fasta',
                                          './positive_data/all_data/positive_pdb.fasta'])

neg_split = FastaProcessor(input_file = neg_all_cdhit2d,
                           output_file = ['./negative_data/all_data/negative_ncbi.fasta',
                                          './negative_data/all_data/negative_uniprot.fasta',
                                          './negative_data/all_data/negative_pdb.fasta'])

pos_splited_files = pos_split.split_dataset(original_files_list = ['./positive_data/ncbi/positive_ncbi_cdhit2d_branch.fasta',
                                                                   './positive_data/uniprot/positive_uniprot_cdhit.fasta',
                                                                   './positive_data/pdb/positive_pdb_cdhit2d_branch.fasta'])

neg_splited_files = neg_split.split_dataset(original_files_list = ['./negative_data/ncbi/negative_ncbi_cdhit2d_branch.fasta',
                                                                   './negative_data/uniprot/negative_uniprot_cdhit.fasta',
                                                                   './negative_data/pdb/negative_pdb_cdhit2d_branch.fasta'])



datalist = ['./positive_data/ncbi/positive_ncbi_cdhit2d_branch.fasta',
            './positive_data/uniprot/positive_uniprot_cdhit.fasta',
            './positive_data/pdb/positive_pdb_cdhit2d_branch.fasta',
             
             pos_all_data,
             pos_splited_files[0],
             pos_splited_files[1],
             pos_splited_files[2],

             './negative_data/ncbi/negative_ncbi_cdhit2d_branch.fasta',
             './negative_data/uniprot/negative_uniprot_cdhit.fasta',
             './negative_data/pdb/negative_pdb_cdhit2d_branch.fasta',

             neg_all_data,
             neg_splited_files[0],
             neg_splited_files[1],
             neg_splited_files[2]
             ]

for index, item in enumerate(datalist):
    count = count_seqs(item)
    print(f'{index+1}. There are {count} seqs in {item}.')