import sys
import os
sys.path.append(
    os.path.abspath(
        os.path.join( os.path.dirname(__file__), '..' )
    )
)

from DataPreprocessingClasses.FastaProcessor import FastaProcessor
from DataPreprocessingClasses.RunCDHIT import ForCDHIT
from count_seq import count_seqs


folders = ['./positive_data',
           
           './positive_data/ncbi',
           './positive_data/uniprot',
           './positive_data/pdb',
           './positive_data/ncbiANDpdb',

           './negative_data',
           
           './negative_data/ncbi',
           './negative_data/uniprot',
           './negative_data/pdb',
           './negative_data/ncbiANDpdb']

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f'{folder} has been created.')
    
    else:
        print(f'{folder} was existed.')



pos_ncbi_ori = FastaProcessor(input_file = './positive_data/ncbi/positive_ncbi.fasta',
                              output_file = './positive_data/ncbi/positive_ncbi_filtered.fasta')

neg_ncbi_ori = FastaProcessor(input_file = './negative_data/ncbi/negative_ncbi.fasta',
                              output_file = './negative_data/ncbi/negative_ncbi_filtered.fasta')

pos_ncbi_filtered = pos_ncbi_ori.filter_seqs()
neg_ncbi_filtered = neg_ncbi_ori.filter_seqs()


pos_pdb_ori = FastaProcessor(input_file = './positive_data/pdb/positive_pdb.fasta',
                             output_file = './positive_data/pdb/positive_pdb_filtered.fasta')

neg_pdb_ori = FastaProcessor(input_file = './negative_data/pdb/negative_pdb.fasta',
                             output_file = './negative_data/pdb/negative_pdb_filtered.fasta')

pos_pdb_filtered = pos_pdb_ori.filter_seqs()
neg_pdb_filtered = neg_pdb_ori.filter_seqs()



pos_merge_file = FastaProcessor(input_file = [pos_ncbi_filtered, pos_pdb_filtered],
                                output_file = './positive_data/ncbiANDpdb/positive_ncbiANDpdb.fasta')

neg_merge_file = FastaProcessor(input_file = [neg_ncbi_filtered, neg_pdb_filtered],
                                output_file = './negative_data/ncbiANDpdb/negative_ncbiANDpdb.fasta')

pos_ncbiANDpdb = pos_merge_file.merge_fasta_files()
neg_ncbiANDpdb = neg_merge_file.merge_fasta_files()



pos_toCDHIT = ForCDHIT(exe = './cd-hit-v4.8.1-2019-0228/cd-hit',
                       input_file = pos_ncbiANDpdb,
                       output_file = './positive_data/ncbiANDpdb/positive_ncbiANDpdb_cdhit.fasta',
                       threads = 23)

neg_toCDHIT = ForCDHIT(exe = './cd-hit-v4.8.1-2019-0228/cd-hit',
                       input_file = neg_ncbiANDpdb,
                       output_file = './negative_data/ncbiANDpdb/negative_ncbiANDpdb_cdhit.fasta',
                       threads = 23)

pos_ncbiANDpdb_cdhit = pos_toCDHIT.cdhit()
neg_ncbiANDpdb_cdhit = neg_toCDHIT.cdhit()



pos_uniprot_ori = FastaProcessor(input_file = './positive_data/uniprot/positive_uniprot.fasta',
                                 output_file = './positive_data/uniprot/positive_uniprot_filtered.fasta')

neg_uniprot_ori = FastaProcessor(input_file = './negative_data/uniprot/negative_uniprot.fasta',
                                 output_file = './negative_data/uniprot/negative_uniprot_filtered.fasta')

pos_uniprot_filtered = pos_uniprot_ori.filter_seqs()
neg_uniprot_filtered = neg_uniprot_ori.filter_seqs()



pos_tocdhit = ForCDHIT(exe = './cd-hit-v4.8.1-2019-0228/cd-hit',
                       input_file = pos_uniprot_filtered,
                       output_file = './positive_data/uniprot/positive_uniprot_cdhit.fasta',
                       threads = 23)

neg_tocdhit = ForCDHIT(exe = './cd-hit-v4.8.1-2019-0228/cd-hit',
                       input_file = neg_uniprot_filtered,
                       output_file = './negative_data/uniprot/negative_uniprot_cdhit.fasta',
                       threads = 23)

pos_uniprot_cdhit = pos_tocdhit.cdhit()
neg_uniprot_cdhit = neg_tocdhit.cdhit()



pos_cdhit2d = ForCDHIT(exe = './cd-hit-v4.8.1-2019-0228/cd-hit-2d',
                       input_file = './positive_data/ncbiANDpdb/positive_ncbiANDpdb_cdhit.fasta',
                       output_file = './positive_data/ncbiANDpdb/positive_ncbiANDpdb_cdhit2d.fasta',
                       threads = 23)


neg_cdhit2d = ForCDHIT(exe = './cd-hit-v4.8.1-2019-0228/cd-hit-2d',
                       input_file = './negative_data/ncbiANDpdb/negative_ncbiANDpdb_cdhit.fasta',
                       output_file = './negative_data/ncbiANDpdb/negative_ncbiANDpdb_cdhit2d.fasta',
                       threads = 23)

pos_ncbiANDpdb_to_uniprot = pos_cdhit2d.cdhit2d(reference_file = './positive_data/uniprot/positive_uniprot_cdhit.fasta')
neg_ncbiANDpdb_to_uniprot = neg_cdhit2d.cdhit2d(reference_file = './negative_data/uniprot/negative_uniprot_cdhit.fasta')



pos_to_split = FastaProcessor(input_file = pos_ncbiANDpdb_to_uniprot,
                              output_file = ['./positive_data/ncbi/positive_ncbi_cdhit2d_branch.fasta',
                                             './positive_data/pdb/positive_pdb_cdhit2d_branch.fasta'])


neg_to_split = FastaProcessor(input_file = neg_ncbiANDpdb_to_uniprot,
                              output_file = ['./negative_data/ncbi/negative_ncbi_cdhit2d_branch.fasta',
                                             './negative_data/pdb/negative_pdb_cdhit2d_branch.fasta'])


pos_splited = pos_to_split.split_dataset(original_files_list = ['./positive_data/ncbi/positive_ncbi.fasta',
                                                                './positive_data/pdb/positive_pdb.fasta'])

neg_splited = neg_to_split.split_dataset(original_files_list = ['./negative_data/ncbi/negative_ncbi.fasta',
                                                                './negative_data/pdb/negative_pdb.fasta'])



datalist = ['./positive_data/ncbi/positive_ncbi.fasta',
            './positive_data/uniprot/positive_uniprot.fasta',
            './positive_data/pdb/positive_pdb.fasta',

            './positive_data/ncbi/positive_ncbi_filtered.fasta',
            './positive_data/uniprot/positive_uniprot_filtered.fasta',
            './positive_data/pdb/positive_pdb_filtered.fasta',

            './positive_data/ncbi/positive_ncbi_cdhit2d_branch.fasta',
            './positive_data/uniprot/positive_uniprot_cdhit.fasta',
            './positive_data/pdb/positive_pdb_cdhit2d_branch.fasta',

            './negative_data/ncbi/negative_ncbi.fasta',
            './negative_data/uniprot/negative_uniprot.fasta',
            './negative_data/pdb/negative_pdb.fasta',

            './negative_data/ncbi/negative_ncbi_filtered.fasta',
            './negative_data/uniprot/negative_uniprot_filtered.fasta',
            './negative_data/pdb/negative_pdb_filtered.fasta',

            './negative_data/ncbi/negative_ncbi_cdhit2d_branch.fasta',
            './negative_data/uniprot/negative_uniprot_cdhit.fasta',          
            './negative_data/pdb/negative_pdb_cdhit2d_branch.fasta'
            ]

for index, item in enumerate(datalist):
    count = count_seqs(item)
    print(f'{index+1}. There are {count} seqs in {item}.')
