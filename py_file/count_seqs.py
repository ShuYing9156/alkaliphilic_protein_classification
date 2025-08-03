from func import *

# datalist = ['./negative_data/ncbi/ncbi_neg.fasta',
#             './negative_data/ncbi/ncbi_neg_filtered.fasta',
#             './negative_data/pdb/pdb_neg.fasta',
#             './negative_data/pdb/pdb_neg_filtered.fasta',
#             './negative_data/cdhit2d/neg_ncbifil_pdbfil.fasta',
#             './negative_data/cdhit2d/neg_ncbipdb_cdhit40.fasta',
#             './negative_data/cdhit2d/cdhit2d40_neg_to_uniprot.fasta',
#             './negative_data/uniprot/uniprot_neg.fasta',
#             './negative_data/uniprot/uniprot_neg_filtered.fasta',
#             './negative_data/uniprot/uniprot_neg_fil_cdhit40.fasta',
#             './positive_data/ncbi/ncbi_pos.fasta',
#             './positive_data/ncbi/ncbi_pos_filtered.fasta',
#             './positive_data/pdb/pdb_pos.fasta',
#             './positive_data/pdb/pdb_pos_filtered.fasta',
#             './positive_data/uniprot/uniprot_pos.fasta',
#             './positive_data/uniprot/uniprot_pos_filtered.fasta',
#             './positive_data/uniprot/uniprot_pos_fil_cdhit40.fasta',
#             './positive_data/cdhit2d/pos_ncbifil_pdbfil.fasta',
#             './positive_data/cdhit2d/pos_ncbipdb_cdhit40.fasta',
#             './positive_data/cdhit2d/cdhit2d40_pos_to_uniprot.fasta',
#             './negative_data/cdhit2d/neg_cdhit2d_ncbi_branch.fasta',
#             './negative_data/cdhit2d/neg_cdhit2d_pdb_branch.fasta',
#             './positive_data/cdhit2d/pos_cdhit2d_ncbi_branch.fasta',
#             './positive_data/cdhit2d/pos_cdhit2d_pdb_branch.fasta']

datalist = ['./negative_data/cut_fasta_file/cut_neg_pdb.fasta',
             './positive_data/cut_fasta_file/cut_pos_ncbi.fasta',
             './positive_data/cut_fasta_file/cut_pos_uniprot.fasta']

for file, i in zip(datalist, range(len(datalist))):
    count = count_seqs(file)
    print(f'{i+1}. There are {count} seqs in {file}')

