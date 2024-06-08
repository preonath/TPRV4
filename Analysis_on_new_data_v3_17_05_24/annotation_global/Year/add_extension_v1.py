import csv

# Define the file paths
input_tsv_file = 'annotation.tsv'
output_tsv_file = 'updated_annotation.tsv'

# Open the input TSV file and create a new TSV file with updated IDs
with open(input_tsv_file, mode='r', newline='') as infile, open(output_tsv_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile, delimiter='\t')
    fieldnames = reader.fieldnames  # This captures the headers from the input file
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')

    # Write headers to the output file
    writer.writeheader()

    # Process each row in the input file
    for row in reader:
        # Append "CSF.1" to the #phyloID
        row['#phyloID'] += 'CSF.1'
        writer.writerow(row)

print("Updated TSV file with 'CSF.1' extensions is written to", output_tsv_file)

