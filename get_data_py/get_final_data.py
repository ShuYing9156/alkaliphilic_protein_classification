import sys
import os
import subprocess

# sys.path.append(
#     os.path.abspath(
#         os.path.join( os.path.dirname(__file__), '..' )
#     )
# )

from DataPreprocessingClasses.FastaProcessor import FastaProcessor


# Check if the destination folder exists; if not, create it
if not os.path.exists('./final_data'):
    os.makedirs('./final_data')  # Create the destination folder
    print(f"Destination folder './final_data' has been created.")



pos_ncbi = './positive_data/all_data/positive_ncbi.fasta'

pos_uniprot = FastaProcessor(input_file = './positive_data/all_data/positive_uniprot.fasta',
                             output_file = './final_data/positive_uniprot.fasta')

pos_pdb = './positive_data/all_data/positive_pdb.fasta'


neg_ncbi = FastaProcessor(input_file = './negative_data/all_data/negative_ncbi.fasta',
                          output_file = './final_data/negative_ncbi.fasta')

neg_uniprot = './negative_data/all_data/negative_uniprot.fasta'

neg_pdb = FastaProcessor(input_file = './negative_data/all_data/negative_pdb.fasta',
                         output_file = './final_data/negative_pdb.fasta')



final_neg_ncbi = neg_ncbi.reservoir_sampling(reference_file = pos_ncbi,
                                             seed = 9156)

final_pos_uniprot = pos_uniprot.reservoir_sampling(reference_file = neg_uniprot,
                                                   seed = 9156)

final_neg_pdb = neg_pdb.reservoir_sampling(reference_file = pos_pdb,
                                           seed = 9156)



## Copy other three files
# Source file and destination folder
source_files = [pos_ncbi, pos_pdb, neg_uniprot]
destination_folder = './final_data'

# Execute the cp command
for index, file in enumerate(source_files):
    try:
        result = subprocess.run(['cp', file, destination_folder], check=True)
        print(f"{file} has been successfully copied to {destination_folder}")
    
    except subprocess.CalledProcessError as e:
        print(f"Copy failed: {e}")


