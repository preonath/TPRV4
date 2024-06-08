import csv

# The IDs that were not found in the tree
missing_ids = [
    "CHRF_BD0003", "DQ873386", "DQ873387", "DQ873388", "DQ873389",
    "EU175855", "EU175856", "EU200667", "EU546204", "EU546205",
    "EU546206", "EU546207", "EU546210", "EU546211", "HQ593530",
    "HQ593531", "HQ593532", "JN183922", "JN798193", "JN798194",
    "JN798195", "JN798196", "KJ541119", "KJ541120", "KJ541121",
    "KM390024", "KM390025", "KU871314", "KU871315", "MZ820170",
    "MZ820171", "AY622943", "DQ873390", "DQ873391", "EU874248",
    "JN183921", "JN183925", "JN798192"
]

# File paths
input_file = 'Updated_ID_Year.tsv'
output_file = 'Missing_IDs_with_Extension.txt'

# Read the existing IDs from the TSV file
existing_ids = set()
with open(input_file, mode='r', newline='') as infile:
    reader = csv.DictReader(infile, delimiter='\t')
    for row in reader:
        existing_ids.add(row['#phyloID'])

# Write the matching missing IDs to a text file with the ".1" extension
with open(output_file, 'w') as outfile:
    for id_ in missing_ids:
        if id_ in existing_ids:
            outfile.write(f"{id_}.1\n")

print(f"Missing IDs written to {output_file}")

