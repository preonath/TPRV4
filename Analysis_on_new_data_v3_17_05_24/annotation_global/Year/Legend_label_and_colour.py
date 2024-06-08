import csv
from collections import OrderedDict
import random

def generate_hex_color():
    """Generates a random hex color code."""
    return f'#{random.randint(0, 0xFFFFFF):06x}'

# Define the file paths
input_file = 'Updated_ID_Year.tsv'

# Initial mapping from year to color
year_color_map = {
    '1980': '#034e7b',
    '2002': '#0570b0',
    '2005': '#3690c0',
    '2006': '#74a9cf',
    '2007': '#a6bddb',
    '2012': '#d0d1e6',
    '2015': '#f1eef6',
    '2017': '#feedde',
    '2018': '#fdd0a2',
    '2019': '#fdae6b',
    '2020': '#fd8d3c',
    '2021': '#e6550d',
    '2022': '#a63603'
}

# Read the file and ensure all years have a color
with open(input_file, mode='r', newline='') as infile:
    reader = csv.DictReader(infile, delimiter='\t')
    for row in reader:
        year = row['Year']
        if year not in year_color_map:
            year_color_map[year] = generate_hex_color()  # Generate a color if year is not in map

# Sorting the years to maintain consistency
sorted_years = sorted(year_color_map, key=int)  # Sort years numerically

# Create the legend rows
legend_colors = 'LEGEND_COLORS\t' + '\t'.join(year_color_map[year] for year in sorted_years)
legend_labels = 'LEGEND_LABELS\t' + '\t'.join(sorted_years)

# Print or write to a file
print(legend_colors)
print(legend_labels)

