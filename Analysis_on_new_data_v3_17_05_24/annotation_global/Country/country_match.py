import csv

# Define the file paths
input_file = 'Id_country.tsv'
output_file = 'ID_Country_Color_Country.tsv'

# Mapping from color code to country name
color_to_country = {
    '#4daf4a': 'Bangladesh',
    '#e41a1c': 'China',
    '#377eb8': 'Coted\'Ivoire',
    '#984ea3': 'Germany',
    '#ff7f00': 'Ghana',
    '#ffff33': 'India',
    '#a65628': 'South Africa',
    '#f781bf': 'USA'
}

# Open the input file and an output file
with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile, delimiter='\t')
    fieldnames = reader.fieldnames + ['Country']  # Append the new column name 'Country'
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')

    # Write headers to the output file
    writer.writeheader()

    # Process each row in the input file
    for row in reader:
        # Get the country color code from the row
        country_color = row['Country_color']
        # Map the color to the corresponding country
        country_name = color_to_country.get(country_color, 'Unknown')  # Use 'Unknown' if the color is not in the dictionary
        # Add the country name to the row
        row['Country'] = country_name
        # Write the updated row to the output file
        writer.writerow(row)

