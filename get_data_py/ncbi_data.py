import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataPreprocessingClasses.NCBISeqs import GetNCBISeqs


folders = ['./positive_data',
           './positive_data/ncbi',

           './negative_data',
           './negative_data/ncbi']

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f'{folder} has been created.')
    
    else:
        print(f'{folder} was existed.')


alka = GetNCBISeqs(email = 'ruby2015095231128@gmail.com')

positive_ncbi_ids = alka.get_ids(term = 'alkaliphilic',
                                 filename = './positive_data/ncbi/positive_ncbi_idlist.txt')

positive_ncbi_seqs = alka.get_seqs(id_file = positive_ncbi_ids,
                                   output_file = './positive_data/ncbi/positive_ncbi.fasta')

negative_ncbi_ids = alka.get_ids(term = 'enzyme',
                                 filename = './negative_data/ncbi/negative_ncbi_idlist.txt')

negative_ncbi_seqs = alka.get_seqs(id_file = negative_ncbi_ids,
                                   output_file = './negative_data/ncbi/negative_ncbi.fasta')
