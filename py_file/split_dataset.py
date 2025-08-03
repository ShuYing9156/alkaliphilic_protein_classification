from func import *

#根據給定的FASTA檔案，將 all_fasta_file 寫入不同的FASTA檔案
all_fasta_files = ['./negative_data/cdhit2d/cdhit2d40_neg_to_uniprot.fasta',
                   './positive_data/cdhit2d/cdhit2d40_pos_to_uniprot.fasta' ]



neg_original_files = ['./negative_data/ncbi/ncbi_neg_filtered.fasta',
                      './negative_data/pdb/pdb_neg_filtered.fasta']

pos_original_files = ['./positive_data/ncbi/ncbi_pos_filtered.fasta',
                      './positive_data/pdb/pdb_pos_filtered.fasta']

ori_files_list = [neg_original_files, pos_original_files]



neg_output_files = ['./negative_data/cdhit2d/neg_cdhit2d_ncbi_branch.fasta',
                    './negative_data/cdhit2d/neg_cdhit2d_pdb_branch.fasta']

pos_output_files = ['./positive_data/cdhit2d/pos_cdhit2d_ncbi_branch.fasta',
                    './positive_data/cdhit2d/pos_cdhit2d_pdb_branch.fasta']

output_files_list = [neg_output_files, pos_output_files]



for all_fasta_file, original_files, output_files in zip(all_fasta_files, ori_files_list, output_files_list):
    print(f"Processing {all_fasta_file}\nwith original files {original_files}\nand output files {output_files}\n")
    
    split_dataset(all_fasta_file,
                  original_files,
                  output_files)


