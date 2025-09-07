from Bio import Entrez
import random
import time

class GetNCBISeqs:
    def __init__(self, email, db="protein"):
        self.email =email
        self.db = db


    def get_ids(self, term, filename, retmax=100):
        '''
        Query protein IDs from the NCBI protein database and write them to a file.
        
        Parameters:
        email (str): User's email
        term (str): Query keyword
        filename (str): File name to write the ID to
        db (str): Database for the query, default is protein
        retmax (int): Maximum number of records returned per query, default is 100
        '''
        
        # Set Up The Email
        Entrez.email = self.email

        # Get Total Record Count
        handle = Entrez.esearch(db=self.db, term=term)
        record = Entrez.read(handle)
        total_records = int(record["Count"])
        handle.close()

        # Paginated Query
        for start in range(0, total_records, retmax):
            handle = Entrez.esearch(db=self.db, term=term, retmax=retmax, retstart=start)
            record = Entrez.read(handle)
            handle.close()

            # Write id to File
            with open(filename, mode='a+', encoding='utf-8') as idlist_file:
                for id in record['IdList']:
                    idlist_file.write(f'{id}\n')
            
            # Print Current Progress
            print(f"Records {start + 1} to {start + len(record['IdList'])}")
        
        return filename


    def get_seqs(self, id_file, output_file, retmax=100):
        """
        Query sequences from NCBI and write the results to a FASTA file.

        Parameters:
        email (str): User's email
        id_file (str): Filename containing protein IDs
        output_file (str): Name of the output FASTA file
        retmax (int): Maximum number of records per query (default is 100)
        """

        # Set Up The Email
        Entrez.email = self.email

        # Read File and Combine IDs into a List
        idlist = []
        with open(id_file, mode='r', encoding='utf-8') as idlist_file:
            for line in idlist_file:
                idlist.append(line.strip())
        
        print(f"Total IDs: {len(idlist)}")
        print(f"Type of idlist: {type(idlist)}")

        # Query the FASTA of each ID
        with open(output_file, "a+") as fasta_file:
            for start in range(0, len(idlist), retmax):
                # Batch extract IDs
                batch_ids = idlist[start:start + retmax]
                ids = ",".join(batch_ids) # Combine IDs into a comma-separated string
                handle = Entrez.efetch(db="protein", id=ids, rettype="fasta", retmode="text")
                fasta_data = handle.read() # Read FASTA data
                handle.close()

                # Write to file
                fasta_file.write(fasta_data)
                print(f"Records {start + 1} to {start + len(batch_ids)} downloaded.")
        
        return output_file

    
    def gpt_neg_ids_seqs(self, output_file, term = 'protein NOT alkaliphilic'):
        print("🧬 Collect non-alkaliphilic proteins...")

        # Exclusion Criteria
        # exclude_terms = [
        #     "alkaliphilic[All Fields]"
        #     ]
        
        # exclude_query = "NOT (" + " OR ".join(exclude_terms) + ")"

        # # Use '*' to represent all protein entries
        # base_query = "*"

        # # Complete Search Criteria
        # search_query = base_query + " AND " + exclude_query

        # search_query = term

        print(f"🔍 Search Criteria: {term}")

        # Total number of data queries
        handle = Entrez.esearch(self.db, term=term, retmax=0)
        total = int(Entrez.read(handle)["Count"])
        handle.close()
        print(f"✅ Found {total:,} non-alkaliphilic proteins")

        # Random Sample ID
        print("📦 Collecting IDs...)")
        all_ids = set()

        for i in range(111):  #6551 seqs/each 111 batches
            start = random.randint(0, max(0, total - 6551))

            try:
                handle = Entrez.esearch(db="protein", term=term, retstart=start, retmax=6551)
                ids = Entrez.read(handle)["IdList"]
                handle.close()

                all_ids.update(ids)
                print(f"  Batch {i+1}/111: +{len(ids)} (Total: {len(all_ids)})")
                time.sleep(0.3)

            except Exception as e:
                print(f"  Batch {i+1}/111: Fail，error: {e}")
        
        # # 選擇6000個ID作為樣本
        # target = 6000
        # if len(all_ids) > target:
        #     selected_ids = random.sample(list(all_ids), target)
        # else:
        #     selected_ids = list(all_ids)
        # print(f"🎯 準備下載 {len(selected_ids)} 個序列")

        selected_ids = list(all_ids)
        print(f"🎯 Preparing to download {len(selected_ids)} sequences")

        # Download FASTA sequences
        # output_file = "ncbi_non_alka_neg.fasta"
        downloaded = 0

        with open(output_file, 'w') as f:
            for start in range(0, len(selected_ids), 1000):
                batch = selected_ids[start:start+1000]

                try:
                    print(f"📥 Downloading Batch {start//1000 + 1}/{(len(selected_ids)-1)//1000 + 1}")

                    handle = Entrez.efetch(db="protein", id=batch, rettype="fasta", retmode="text")
                    fasta_data = handle.read()
                    handle.close()

                    f.write(fasta_data)
                    downloaded += fasta_data.count('>')
                    time.sleep(0.5)

                except Exception as e:
                    print(f"  ❌ Batch download failed: {e}")
        
        print(f"🎉 Done! Downloaded {downloaded} non-alkaliphilic proteins to {output_file}")
        return output_file
