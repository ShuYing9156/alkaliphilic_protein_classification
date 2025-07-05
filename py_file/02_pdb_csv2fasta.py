from func import *

#將CSV檔案中的PDB序列轉換為FASTA格式並寫入檔案。
pdb_seqs_fasta = './pdb_fasta/pdb_all_seqs.fasta'
pdb_seqs_csv = './pdb_fasta/rcsb_pdb_sequence_20250422064207.csv'


pdb_csv2fasta(csv_file = pdb_seqs_csv, 
              fasta_file = pdb_seqs_fasta)


