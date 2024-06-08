import csv

# Define the file paths
input_file = 'TLC.csv'
output_file = 'output_with_groups_and_colors.csv'

# Define the mapping from TLC ranges to colors
range_to_color = {
    '1-9': '#ffffd9',
    '10-49': '#edf8b1',
    '50-99': '#225ea8',
    '150-199': '#c7e9b4',
    '250-299': '#7fcdbb',
    '300-349': '#41b6c4',
    '350-399': '#1d91c0',
    '>=500': '#0c2c84'
}

# Open the input file and an output file
with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['Group', 'Color']  # Append new columns for group and color
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    # Write headers to the output file
    writer.writeheader()
    
    # Process each row in the input file
    for row in reader:
        tlc = int(row['TLC'])  # Assuming TLC is always an integer
        
        # Determine the group based on the TLC value
        if 1 <= tlc <= 9:
            group = '1-9'
        elif 10 <= tlc <= 49:
            group = '10-49'
        elif 50 <= tlc <= 99:
            group = '50-99'
        elif 150 <= tlc <= 199:
            group = '150-199'
        elif 250 <= tlc <= 299:
            group = '250-299'
        elif 300 <= tlc <= 349:
            group = '300-349'
        elif 350 <= tlc <= 399:
            group = '350-399'
        elif tlc >= 500:
            group = '>=500'
        else:
            group = 'Other'  # For values that do not fit any specified ranges

        # Get the corresponding color
        color = range_to_color.get(group, 'Unknown')  # Use 'Unknown' for any group not defined

        # Add the group and color to the row
        row['Group'] = group
        row['Color'] = color
        
        # Write the updated row to the output file
        writer.writerow(row)

