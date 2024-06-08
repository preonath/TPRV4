import csv

# Define the file paths
input_file = 'TLC.csv'
output_file = 'output_with_groups_and_colors.csv'

# Define the mapping from TLC ranges to colors
range_to_color = {
    '0': '#f300f7',
    '1-9': '#1bd9f1',
    '10-99': '#d12700',
    '100-499': '#0176ed',
    '>=500': '#f2b9f8'
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
        if tlc == 0:
            group = '0'
        elif 1 <= tlc <= 9:
            group = '1-9'
        elif 10 <= tlc <= 99:
            group = '10-99'
        elif 100 <= tlc <= 499:
            group = '100-499'
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

print(f"Output file saved as {output_file}")

