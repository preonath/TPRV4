import pandas as pd

# Load the data
data = pd.read_csv('coinfection.csv')

# Ensure 'None' values are correctly mapped and remove any leading/trailing spaces
data['Co-infection'] = data['Co-infection'].str.strip().fillna('None')

# Define the mapping from co-infection to color
infection_to_color = {
    'None': '#d9d9d9',  # Light grey for 'None'
    'B19': '#ffcccc',   # Light red for 'B19'
    'Acinetobacter sp.': '#ffff99',  # Light yellow
    'Streptococcus pneumoniae': '#99ccff',  # Light blue
    'Klebsiella pneumoniae': '#cc99ff',  # Light purple
    'Escherichia coli': '#99ff99',  # Light green
    'Pseudomonas spp.': '#ffcc99',  # Light orange
    'Streptococcus pneumoniae, B19': '#ccccff',  # Light lavender
    'Acinetobacter baumannii': '#ff99cc'  # Light pink for 'Acinetobacter baumannii'
}

# Map the colors
data['Colour_group'] = data['Co-infection'].map(infection_to_color)

# Save the updated data
output_file_path = 'updated_data_corrected.csv'
data.to_csv(output_file_path, index=False)
