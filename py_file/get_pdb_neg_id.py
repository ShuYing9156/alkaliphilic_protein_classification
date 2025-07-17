import requests
import json

# Search conditions definition
query = {
    "type": "terminal",
    "service": "full_text",
    "parameters": {
        "value": "enzyme"  # Search keyword
    }
}

# API endpoint
url = "https://search.rcsb.org/rcsbsearch/v2/query"

# Pagination parameters
page_size = 100  # Maximum 100 results per page
start = 0
total_results = None

# Open file to record the results
with open("./negative_data/pdb/pdb_negative_idlist.txt", "w") as file:
    while True:
        # Assemble request parameters
        params = {
            "query": query,
            "request_options": {
                "paginate": {
                    "start": start,
                    "rows": page_size
                }
            },
            "return_type": "entry"
        }

        try:
            # Send POST request
            response = requests.post(url, json=params)

            # Check HTTP status code
            if response.status_code == 200:
                results = response.json()

                # If first query, get total results count
                if total_results is None:
                    total_results = results.get("total_count", 0)
                    print(f"Found a total of {total_results} results.")

                # if there is no result, terminate the program
                if total_results == 0:
                    print("Did not find any results.")
                    break

                # Extract PDB ID and write to file
                pdb_ids = [entry["identifier"] for entry in results["result_set"]]
                for pdb_id in pdb_ids:
                    file.write(pdb_id + "\n")

                # Update start position
                start += page_size

                # Check if all results have been retrieved
                if start >= total_results:
                    break
            else:
                print(f"Search failed, HTTP status code: {response.status_code}")
                print(f"Response content: {response.text}")
                break

        except Exception as e:
            print(f"An error occurred: {e}")
            break

print("All PDB IDs have been successfully written to enzyme_pdb_ids.txt (if any results were found).")
