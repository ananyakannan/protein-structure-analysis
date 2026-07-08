import pandas as pd
import requests
#Step 1: Load our protein list CSV
protein_df = pd.read_csv("data/protein_list.csv")
#Step 2: Prepare an empty string to collect all FASTA sequences
all_sequences = ""
#Step 3: Loop thorugh each row of the DataFrame
for index, row in protein_df.iterrows():
    accession = row["accession"] 
    gene = row["gene_name"]
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        all_sequences += response.text
        print(f"Fetched {gene} successfully")
    else:
        print(f"Failed to fetch {gene}")
#Step 4: Save everything to one FASTA file
with open("data/bcl2_family_proteins.fasta", "w") as f:
    f.write(all_sequences)
