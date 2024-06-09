import pandas as pd

def get_unique_types(df):
    """ Extract unique types from the second column of a DataFrame, assumed to be the 'Type' column. """
    return sorted(df.iloc[:, 1].unique())

def get_color_inputs(types):
    """ Get color input for each type from the user in a single batch. """
    colors = {}
    print("Enter the HEX color for", len(types), "types in the order shown below, each on a new line:")
    for type_ in types:
        print(f"Type {type_}:")
    input_colors = [input() for _ in types]
    for type_, color in zip(types, input_colors):
        colors[str(type_).strip()] = color.strip()
    return colors

def apply_colors(df, color_dict):
    """ Apply colors to the DataFrame based on type-color mapping.
        Insert the color as the third column in the DataFrame. """
    color_column = df.iloc[:, 1].apply(lambda x: color_dict.get(str(x).strip(), 'Unknown'))
    df.insert(2, 'Color', color_column)
    return df

def print_terminal_output(color_mapping):
    """ Print the final color and type mapping to the terminal, with special formatting. """
    sorted_keys = sorted(color_mapping.keys())
    sorted_colors = [color_mapping[key] for key in sorted_keys]
    
    # Generate a string of '1's with length equal to the number of types
    ones = '\t'.join(['1'] * len(sorted_colors))
    
    # Print each part with labels and values separated by tabs
    print(f"LEGEND_SHAPES\t{ones}")
    print(f"LEGEND_COLORS\t" + "\t".join(sorted_colors))
    print(f"LEGEND_LABELS\t" + "\t".join(sorted_keys))

# Load the data
df = pd.read_csv('annotation.tsv', delimiter='\t')

# Find unique types
unique_types = get_unique_types(df)

# Get color mappings from the user
color_mapping = get_color_inputs(unique_types)

# Apply colors based on type
df_colored = apply_colors(df, color_mapping)

# Save the new DataFrame to a file
df_colored.to_csv('annotation_colour.tsv', sep='\t', index=False)

# Print output in the terminal as specified
print_terminal_output(color_mapping)

print("Updated file with colors has been saved as 'annotation_colour.tsv'")

