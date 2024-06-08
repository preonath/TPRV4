import pandas as pd

# Load the data
data = pd.read_csv('coinfection.csv')  # Adjust the file name as needed

# Define the mapping from co-infection to color
infection_to_color = {
    'None': '#d9d9d9',  # Light grey for 'None'
    'B19': '#ffcccc',   # Light red for 'B19'
    'Acinetobacter sp.': '#ffff99',  # Light yellow
    'Streptococcus pneumoniae': '#99ccff',  # Light blue
    'Klebsiella pneumoniae': '#cc99ff',  # Light purple
    'Escherichia coli': '#99ff99',  # Light green
    'Pseudomonas spp.': '#ffcc99',  # Light orange
    'Streptococcus pneumoniae, B19': '#ccccff'  # Light lavender
}

# Map the colors
data['Colour_group'] = data['Co-infection'].map(infection_to_color)

# Save the updated data
data.to_csv('updated_data.csv', index=False)

