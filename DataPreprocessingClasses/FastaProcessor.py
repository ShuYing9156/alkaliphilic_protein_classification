from Bio import SeqIO
import pandas as pd
import random


class FastaProcessor:
    def __init__(self, input_file, output_file, min_length = 100, ambiguous_residue = None):
        """
        Initialize FastaProcessor object.

        Parameters:
        input_file (str or list): Name of the input FASTA file.
        output_file (str or list): Name of the output FASTA file.
        min_length (int): Minimum sequence length, default is 100.
        ambiguous_residues (list): List of ambiguous residues, default is None.
        """
        self.input_file = input_file
        self.output_file = output_file
        self.min_length = min_length
        if ambiguous_residue is None:
            self.ambiguous_residue = ['B', 'J', 'o', 'U', 'X', 'Z']
        else:
            self.ambiguous_residue = ambiguous_residue
    
    def csv2fasta(self):
        """
        Converts the PDB sequences in the CSV file to FASTA format and writes to a file.
        The input file must be a csv file.
        """
        # Check if self.input_file is a CSV file
        if not self.input_file.endswith('.csv'):
            raise ValueError("Input file must be a CSV file.")

        # Read CSV file
        all_seqs = pd.read_csv(self.input_file)

        # Select required columns
        seqs_needed = all_seqs[['Entry ID', 'Sequence']]

        # Write to FASTA file
        with open(self.output_file, 'w') as fasta_file:
            for _, row in seqs_needed.iterrows():
                entry_id = row['Entry ID']
                sequence = row['Sequence']

                if pd.notna(entry_id) and pd.notna(sequence):
                    fasta_file.write(f'>{entry_id}\n{sequence}\n')
    

    def filter_seqs(self):
        """
        Filter sequences in FASTA files based on length and ambiguous residue conditions.
        """
        sequence_count = 0

        with open(self.input_file, 'r') as input_fasta, open(self.output_file, 'w') as output_fasta:
            for record in SeqIO.parse(input_fasta, 'fasta'):
                sequence = str(record.seq)
                    
                # Check sequence length and ambiguous residues
                if len(sequence) > self.min_length and not any(res in self.ambiguous_residue for res in sequence):
                    SeqIO.write(record, output_fasta, 'fasta')
                    sequence_count += 1
                        
        print(f'The output file {self.output_file} has {sequence_count} sequences.\n')

        return self.output_file
    

    def merge_fasta_files(self):
        """
        Merges multiple FASTA files into a single file.
        The input file must be a list of paths to the FASTA files to be merged, e.g. ['file1.fasta', 'file2.fasta', 'file3.fasta']
        """
        # Check if self.input_file is a list
        if not isinstance(self.input_file, list):
            raise ValueError("Input file must be a list of FASTA file paths.")
        
        merged_records = []

        for file in self.input_file:
            records = list( SeqIO.parse(file, 'fasta') )
            merged_records.extend(records)
        
        # Writes all sequences to a new FASTA file.
        SeqIO.write(merged_records, self.output_file, 'fasta')
        print(f'Merge completed, the result has been written to {self.output_file}.')

        return self.output_file
    

    def split_dataset(self, original_files_list):
        """
        Filter sequences based on the given sequence ID and write them to different FASTA files.
        Output_file must be a list.

        Parameters:
        original_files_list (list): A list of names of reference FASTA files.
        """
        # Check if self.output_file and original_files_list are both lists
        if not isinstance(self.output_file, list):
            raise ValueError("Output file must be a list.")
        
        if not isinstance(original_files_list, list):
            raise ValueError("Original files list must be a list.")
        
        # Read all sequence IDs from a fasta file
        all_ids = set()
        for record in SeqIO.parse(self.input_file, 'fasta'):
            all_ids.add(record.id)
        
        # Read filtered sequence ID
        filtered_ids = [set() for _ in original_files_list]
        
        for i, filtered_file in enumerate(original_files_list):
            for record in SeqIO.parse(filtered_file, 'fasta'):
                filtered_ids[i].add(record.id)
        
        # Prepare to write to different FASTA files
        records = [ [] for _ in self.output_file ]

        for record in SeqIO.parse(self.input_file, 'fasta'):
            seq_id = record.id
            
            for i, filtered_id in enumerate(filtered_ids):
                if seq_id in filtered_id:
                    records[i].append(record)
                    break   # After finding the corresponding ID, you can exit the loop.
        
        # written to different FASTA files
        for records_list, output_file in zip(records, self.output_file):
            SeqIO.write(records_list, output_file, 'fasta')
        
        print('The sequence has been successfully written to their respective FASTA files.')

        return self.output_file
    

    def reservoir_sampling(self, reference_file, seed=None):
        '''
        Randomly samples a nmber of sequences equal to reference_fasta from the original fasta file using reservoir sampling,
        and saves it to output_fasta. Optionally set the random seed.

        Parameters:
        reference_file (str): Path to the reference FASTA file (used to determine sample size).
        '''
        # Optionally set the random seed for reproducible results
        if seed is not None:
            random.seed(seed)
        
        # Count the number of sequences in the reference FASTA file
        reference_count = sum(1 for _ in SeqIO.parse(reference_file, 'fasta'))
        print(f'There are {reference_count} sequences in {reference_file}.')

        # Initialize an empty reservoir (list) to store sampled sequences
        reservoir = []

        for i, seq in enumerate(SeqIO.parse(self.input_file, 'fasta')):
            if i < reference_count:
                reservoir.append(seq)  # For the first 'reference_count' sequences, add them directly to the reservoir.
            
            else:
                j = random.randint(0, i)
                if j < reference_count:
                    reservoir[j] = seq  # If the random index falls within the reservoir, replace that sequence.
                
        
        # Write the sampled sequences in the reservoir to the output FASTA file
        SeqIO.write(reservoir, self.output_file, 'fasta')
        print(f'Randomly sampled {reference_count} sequences and saved to {self.output_file}.')

        return self.output_file


