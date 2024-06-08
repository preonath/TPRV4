import csv

# Define the file paths
input_file = 'ID_Year.tsv'
output_file = 'ID_Year_Color.tsv'

# Define the mapping from year to color
year_to_color = {
    '2015': '#b35806',
    '2016': '#e08214',
    '2017': '#fdb863',
    '2018': '#fee0b6',
    '2019': '#d8daeb',
    '2020': '#b2abd2',
    '2021': '#8073ac',
    '2022': '#542788'
}

# Open the input file and an output file
with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile, delimiter='\t')
    fieldnames = reader.fieldnames + ['Year_Color']  # Append the new column name
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')
    
    # Write headers to the output file
    writer.writeheader()
    
    # Process each row in the input file
    for row in reader:
        year = row['Year']
        # Assign the corresponding color from the year_to_color mapping
        row['Year_Color'] = year_to_color.get(year, 'Unknown')  # Use 'Unknown' for any missing years
        # Write the updated row to the output file
        writer.writerow(row)

