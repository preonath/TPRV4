import csv

# Define the file paths
input_tsv_file = 'ID_Country_Color_Country.tsv'
input_txt_file = 'Missing_IDs_with_Extension.txt'
output_tsv_file = 'Updated_ID_Country_with_Extensions.tsv'

# Read the IDs from the text file (assuming they already have the .1 extension)
ids_to_update = set()
with open(input_txt_file, 'r') as txt_file:
    for line in txt_file:
        # Remove the .1 for matching purposes, and newline characters
        ids_to_update.add(line.strip()[:-2])

# Open the input TSV file and create a new TSV file with updated IDs
with open(input_tsv_file, mode='r', newline='') as infile, open(output_tsv_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile, delimiter='\t')
    fieldnames = reader.fieldnames  # assuming #phyloID is in the fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')

    # Write headers to the output file
    writer.writeheader()

    # Process each row in the input file
    for row in reader:
        # Check if the current row's ID needs to be updated
        if row['#phyloID'] in ids_to_update:
            row['#phyloID'] += '.1'
        writer.writerow(row)

print("Updated TSV file written to", output_tsv_file)

