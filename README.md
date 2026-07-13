# Protein Structure Data Analysis — BCL2 Family

## Overview
This project analyzes structural properties (length, molecular weight, 
instability index, etc.) of BCL2-family apoptosis proteins, comparing 
pro-apoptotic vs anti-apoptotic groups. Built as part of my bioinformatics 
learning journey, following ___ (name your Project 1 and 2 here for continuity).

## Biological Context
BCL2-family proteins regulate apoptosis (programmed cell death) and are 
frequently dysregulated in cancer — particularly relevant to my research 
on ___ (mention your BCL2/breast carcinoma paper briefly here).

## Proteins Studied
**Anti-apoptotic:** BCL2, BCL2L1, MCL1, BCL2A1, BCL2L2
**Pro-apoptotic:** BAX, BAK1, BID, BAD, BIK, BBC3

## Tools Used
- Python (Pandas, NumPy)
- Biopython (ProtParam)
- Seaborn / Matplotlib
- SciPy (statistical testing)

## Status
🚧 In progress — Day 1: project setup complete
🚧 In progress — Day 2 complete: protein list finalized, sequences fetched from UniProt (data/bcl2_family_proteins.fasta)
🚧 In progress — Day 3 complete: protein structural properties calculated (MW, instability index, aromaticity, GRAVY) via Biopython ProtParam, saved to data/protein_properties.csv
🚧 In progress — Day 4 complete: Seaborn introduced (histplot, kdeplot) for molecular weight and instability index distributions
🚧 In progress — Day 5 complete: group comparisons added (boxplot for instability index, violinplot for molecular weight) between anti- and pro-apoptotic proteins
🚧 In progress — Day 6 complete: relationship plots added (scatterplot for length vs molecular weight, regplot for instability index vs GRAVY score)
🚧 In progress — Day 7 complete: correlation matrix (.corr()) and heatmap added, revealing strong relationships (length-MW, aromaticity-instability index)
🚧 In progress — Day 8 complete: Mann-Whitney U test applied to instability index (anti- vs pro-apoptotic), p-value annotated directly on boxplot (p=0.082, not significant at n=11)


## Folder Structure
- `data/` — raw and processed protein data
- `scripts/` — analysis scripts
- `notebooks/` — exploratory notebooks
- `results/` — generated plots and figures