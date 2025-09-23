import subprocess

class ForCDHIT:
    def __init__(self, exe, input_file, output_file, threads, identity=0.4, word_size=2):
        self.exe = exe
        self.input_file = input_file
        self.output_file = output_file
        self.threads = threads
        self.identity = identity
        self.word_size = word_size
    

    def cdhit(self, search_clustering=False, sequence_filter=False):
        """
        Execute the CD-HIT command.

        Parameters:
        search_clustering (bool): Whether to enable the -sc parameter, default is False.
        sequence_filter (bool): Whether to enable the -sf parameter, default is False.
        """
        command = [self.exe, # Name of the executable file for CD-HIT
                   "-i", self.input_file, # Input file
                   "-o", self.output_file, # Output file
                   "-c", str(self.identity), # Similarity threshold
                   "-n", str(self.word_size), # Word size
                   "-T", str(self.threads) # Number of threads
                   ]
        
        # Add -sc and -sf parameters
        if search_clustering:
            command.append("-sc")
        if sequence_filter:
            command.append("-sf")

        try:
            subprocess.run(command, check=True)
            print(f"CD-HIT executed successfully, results written to {self.output_file}")
        except subprocess.CalledProcessError as e:
            print(f"CD-HIT execution failed: {e}")
        
        return self.output_file
    

    def cdhit2d(self, reference_file):
        """
        Execute the CD-HIT command.

        Parameters:
        input_file_2 (str): The second input fasta file name
        """
        command = [self.exe,
                   "-i", reference_file,
                   "-i2", self.input_file,
                   "-o", self.output_file,
                   "-c", str(self.identity),
                   "-n",str(self.word_size),
                   "-T", str(self.threads)
                   ]
        
        try:
            subprocess.run(command, check=True)
            print(f"CD-HIT-2D executed successfully, results written to {self.output_file}")
        except subprocess.CalledProcessError as e:
            print(f"CD-HIT-2D execution failed: {e}")
        
        return self.output_file




