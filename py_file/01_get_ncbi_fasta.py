from func import *

email = "ruby2015095231128@gmail.com"
term = "alkaliphilic"
idlist  = "./positive_data/ncbi/ncbi_pos_idlist.txt"
fasta_file = "./positive_data/ncbi/ncbi_pos_seqs.fasta"

# fetch_ncbi_ids(email, 
#                term,
#                idlist)

fetch_ncbi_seqs(email,
                idlist,
                fasta_file)








