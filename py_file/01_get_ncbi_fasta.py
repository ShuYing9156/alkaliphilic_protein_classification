from func import *

#從NCBI的蛋白質數據庫中查詢符合條件的蛋白質ID，並將其寫入檔案。
email = 'ruby2015095231128@gmail.com'
term = 'alkaliphilic'
idlist = './negative_data_fasta/ncbi_negative_idlist.txt'


fetch_ncbi_ids(email = email, 
               term = term, 
               filename = idlist)



#從NCBI查詢FASTA序列並將結果寫入檔案。
ncbi_seqs_fasta = './negative_data_fasta/ncbi_negative.fasta'


fetch_ncbi_seqs(email = email, 
                id_file = idlist, 
                output_file = ncbi_seqs_fasta)



