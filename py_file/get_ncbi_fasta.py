from func import *

email = "ruby2015095231128@gmail.com"
term = "alkaliphilic"
idlist  = "./negative_data/ncbi/ncbi_neg_idlist.txt"
fasta_file = "./negative_data/ncbi/ncbi_neg.fasta"

# fetch_ncbi_ids(email, 
#                term,
#                idlist)

fetch_ncbi_seqs(email,
                idlist,
                fasta_file)








