import pandas as pd

def get_unique_types(df):
    """ Extract unique types from the second column of a DataFrame, assumed to be the 'Type' column. """
    return sorted(df.iloc[:, 1].unique())  # Using index 1 for the second column

def get_color_inputs(types):
    """ Get color input for each type from the user in a single batch, after types are sorted. """
    colors = {}
    print("Enter the HEX color for", len(types), "types in the order shown below, each on a new line:")
    for type_ in types:
        print(f"Type {type_}:")
    # Read multiple lines of input
    input_colors = [input() for _ in types]
    for type_, color in zip(types, input_colors):
        colors[str(type_).strip()] = color.strip()  # Convert type_ to string here and strip any whitespace
    return colors

def apply_colors(df, color_dict):
    """ Apply colors to the DataFrame based on type-color mapping. """
    # Using .get to avoid KeyError if a type is missing in the color dictionary
    df['Color'] = df.iloc[:, 1].apply(lambda x: color_dict.get(str(x).strip(), 'Unknown'))  # Using index 1 for the second column
    return df

def print_terminal_output(color_mapping):
    """ Print the final color and type mapping to the terminal in the specified format. """
    # Sort the color mapping by type
    sorted_keys = sorted(color_mapping.keys())
    sorted_colors = [color_mapping[key] for key in sorted_keys]
    print("\t".join(sorted_colors))
    print("\t".join(sorted_keys))

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

