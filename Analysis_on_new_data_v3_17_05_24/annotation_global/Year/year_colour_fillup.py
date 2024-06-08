import csv
import random

def generate_hex_color():
    """ Generates a random hex color code. """
    return f'#{random.randint(0, 0xFFFFFF):06x}'

# Define file paths
input_file = 'ID_Year.tsv'
output_file = 'Updated_ID_Year.tsv'

# Read existing data
year_to_color = {}
with open(input_file, mode='r', newline='') as infile:
    reader = csv.DictReader(infile, delimiter='\t')
    data = list(reader)  # Convert iterator to list to reuse it

    # First pass to collect existing year-color mappings
    for row in data:
        if row['Year'] in year_to_color:
            continue  # Skip if the year already has a color
        elif row['Year'] and row.get('year_color'):
            year_to_color[row['Year']] = row['year_color']
        elif row['Year'] and not row.get('year_color'):
            # Assign a new color if not existing
            year_to_color[row['Year']] = generate_hex_color()

# Write updated data
fieldnames = reader.fieldnames if 'year_color' in reader.fieldnames else reader.fieldnames + ['year_color']
with open(output_file, mode='w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()

    # Second pass to output data with updated colors
    for row in data:
        if not row.get('year_color'):  # Only update if missing
            row['year_color'] = year_to_color[row['Year']]
        writer.writerow(row)

print("Updated file written to", output_file)

