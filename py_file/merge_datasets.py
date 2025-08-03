from func import *

#將多個FASTA檔案合併成一個檔案
neg_fil_ncbi = './negative_data/ncbi/ncbi_neg_filtered.fasta'
neg_fil_pdb = './negative_data/pdb/pdb_neg_filtered.fasta'

pos_fil_ncbi = './positive_data/ncbi/ncbi_pos_filtered.fasta'
pos_fil_pdb = './positive_data/pdb/pdb_pos_filtered.fasta'


files = [[neg_fil_ncbi, neg_fil_pdb], 
         [pos_fil_ncbi, pos_fil_pdb]]

output = ['./negative_data/cdhit2d/neg_ncbifil_pdbfil.fasta', 
          './positive_data/cdhit2d/pos_ncbifil_pdbfil.fasta']

for fasta_files, output_file in zip(files, output):
    merge_fasta_files(fasta_files = fasta_files,
                      output_file = output_file)
