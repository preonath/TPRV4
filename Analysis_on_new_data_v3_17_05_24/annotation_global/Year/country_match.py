import csv

# Define the file paths
input_file = '/media/asus/275dd380-2319-4638-bcdd-5f65b2b1d4b5/CHRF_Project_Data/TPRV/Analysis_on_new_data_v3_17_05_24/annotation_global/Year/Id_Year.tsv'
output_file = '/media/asus/275dd380-2319-4638-bcdd-5f65b2b1d4b5/CHRF_Project_Data/TPRV/Analysis_on_new_data_v3_17_05_24/annotation_global/Year/ID_Year.tsv'

# Mapping from color code to year based on your legend
color_to_year = {
    '#034e7b': '1980',
    '#0570b0': '2002',
    '#3690c0': '2005',
    '#74a9cf': '2006',
    '#a6bddb': '2007',
    '#d0d1e6': '2012',
    '#f1eef6': '2015',
    '#feedde': '2017',
    '#fdd0a2': '2018',
    '#fdae6b': '2019',
    '#fd8d3c': '2020',
    '#e6550d': '2021',
    '#a63603': '2022'
}

# Open the input file and an output file
with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile, delimiter='\t')
    fieldnames = reader.fieldnames + ['Year']  # Append the new column name 'Year'
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')

    # Write headers to the output file
    writer.writeheader()

    # Process each row in the input file
    for row in reader:
        year_color = row['year_color']
        # Map the color to the corresponding year
        year = color_to_year.get(year_color, 'Unknown')  # Use 'Unknown' if the color is not in the dictionary
        row['Year'] = year
        # Write the updated row to the output file
        writer.writerow(row)

