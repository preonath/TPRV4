import csv

# Define the file paths
input_file = 'ID_outcome.tsv'
output_file = 'ID_Outcome_Color.tsv'

# Define the mapping from outcome type to color
outcome_to_color = {
    'Died': '#1f78b4',       # Blue
    'Discharged': '#33a02c', # Green
    'DORB': '#e31a1c'        # Red
}

# Open the input file and an output file
with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile, delimiter='\t')
    fieldnames = reader.fieldnames + ['Outcome_Color']  # Append the new column name
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')
    
    # Write headers to the output file
    writer.writeheader()
    
    # Process each row in the input file
    for row in reader:
        outcome = row['Outcome']
        # Assign the corresponding color from the outcome_to_color mapping
        row['Outcome_Color'] = outcome_to_color.get(outcome, 'Unknown')  # Use 'Unknown' for any missing outcomes
        # Write the updated row to the output file
        writer.writerow(row)

