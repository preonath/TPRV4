import csv

# Define the file paths
input_file = 'ID_Genotype.tsv'
output_file = 'ID_Genotype_Color.tsv'

# Define the mapping from genotype to color
genotype_to_color = {
    '1': '#b35806',   # Example color
    '2': '#e08214',   # Example color
    '3': '#fdb863',   # Example color
    '1,2': '#fee0b6',  # Example color for combined genotypes '1,2' (or equivalent ['1', '2'])
}

# Open the input file and an output file
with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile, delimiter='\t')
    fieldnames = reader.fieldnames + ['Genotype_Color']  # Append the new column name for colors
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')

    # Write headers to the output file
    writer.writeheader()

    # Process each row in the input file
    for row in reader:
        genotype = row['Genotype']
        # Normalize the genotype string to handle spaces and ensure consistency
        normalized_genotype = genotype.replace(' ', '').replace('[', '').replace(']', '').replace("'", '')
        # Check if normalized genotype needs to be translated (e.g., '2,1' to '1,2')
        if normalized_genotype == '2,1':
            normalized_genotype = '1,2'
        # Assign the corresponding color from the genotype_to_color mapping
        row['Genotype_Color'] = genotype_to_color.get(normalized_genotype, 'Unknown')  # Use 'Unknown' for any missing genotypes
        # Write the updated row to the output file
        writer.writerow(row)

