"""Reads protein sequences from FASTA, calculates structural properties using Biopython's ProtParam, and saves results to protein_properties.csv."""
import pandas as pd
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis 
#Load the gene/group info we already have
protein_df = pd.read_csv("data/protein_list.csv")
#Step 1: Empty list to collect one dictionary per protein
results = []
for record in SeqIO.parse("data/bcl2_family_proteins.fasta", "fasta"):
    sequence = str(record.seq)
    analysis = ProteinAnalysis(sequence)
    accession = record.id.split("|")[1]
    mw = analysis.molecular_weight()
    instability = analysis.instability_index()
    aromaticity = analysis.aromaticity()
    gravy = analysis.gravy()
    length = len(sequence)
    #Step 2: Build one dictionary per protein
    results.append({
        "accession": accession,
        "length": length,
        "molecular_weight": mw,
        "instability_index": instability,
        "aromaticity": aromaticity,
        "gravy": gravy
    })
#Step 3: Convert list of dictionaries into a DataFrame
properties_df = pd.DataFrame(results)
#Step 4: Merge with our original gene_name/group info using accession number as the shared key
final_df = pd.merge(protein_df, properties_df, on="accession")
#Step 5: save it
final_df.to_csv("data/protein_properties.csv", index=False)
print(final_df)


