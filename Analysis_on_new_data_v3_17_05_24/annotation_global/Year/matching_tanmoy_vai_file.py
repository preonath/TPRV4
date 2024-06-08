import csv

# File paths
input_tsv = 'ID_Country_Color_Country.tsv'
input_txt = 'TPRV_global.txt'
output_tsv = 'Updated_ID_Country_Color_Country.tsv'

# Load the sample IDs from the TXT file into a set for quick lookup
with open(input_txt, 'r') as file:
    sample_ids = {line.strip() for line in file}

# Load the #phyloID from the TSV file into another set
phylo_ids = set()
with open(input_tsv, 'r', newline='') as infile:
    reader = csv.DictReader(infile, delimiter='\t')
    for row in reader:
        phylo_ids.add(row['#phyloID'])

# Determine IDs not matched in both sets
unmatched_sample_ids = sample_ids - phylo_ids
unmatched_phylo_ids = phylo_ids - sample_ids

# Print unmatched IDs
print("Sample IDs not matched in TPRV_global.txt:", unmatched_sample_ids)
print("PhyloIDs not matched from TSV:", unmatched_phylo_ids)

# Update the TSV file considering matched IDs
with open(input_tsv, mode='r', newline='') as infile, open(output_tsv, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile, delimiter='\t')
    fieldnames = reader.fieldnames + ['In_TPRV_Global']  # Append the new column name
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')

    # Write headers to the output file
    writer.writeheader()

    # Process each row in the input TSV
    for row in reader:
        # Check if the phyloID is in the list of sample IDs
        if row['#phyloID'] in sample_ids:
            row['In_TPRV_Global'] = row['#phyloID']  # Include the phyloID in the new column if it matches
        else:
            row['#phyloID'] = ''  # Set phyloID to empty if there is no match
            row['In_TPRV_Global'] = ''  # Also set In_TPRV_Global to empty

        # Write the updated row to the output TSV
        writer.writerow(row)

