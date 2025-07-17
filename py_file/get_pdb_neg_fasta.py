import requests

# PDB ID.txt file path
file_path = "./negative_data/pdb/pdb_neg_idlist.txt"

# Read PDB ID list
with open(file_path, "r") as file:
    pdb_ids = [line.strip() for line in file if line.strip()]  # Remove empty lines and extra whitespace

# Output FASTA file path
output_fasta = "./negative_data/pdb/pdb_neg.fasta"

# Open output file
with open(output_fasta, "w") as output_file:
    for pdb_id in pdb_ids:
        url = f"https://www.rcsb.org/fasta/entry/{pdb_id}"  # API URL
        response = requests.get(url)
        
        if response.status_code == 200:
            # Write sequence to output file
            output_file.write(response.text)
            print(f"Added {pdb_id} sequence to {output_fasta}")
        else:
            print(f"Failed to fetch sequence for {pdb_id}")

print(f"All sequences have been saved to {output_fasta}")
