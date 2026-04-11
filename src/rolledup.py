import pandas as pd

# Modified URL to export as CSV
sheet_id = '1rb7H7I_kId9oIoWaTJpBC4jPYZFqyC2AjHMC3wBbGg8'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv'

# Load the data
df = pd.read_csv(url)

# Convert numeric columns for aggregation
# We keep a string version of Quantity for the "allocations" column
df['Quantity_str'] = df['Quantity'].astype(str)
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Total Value ($)'] = pd.to_numeric(df['Total Value ($)'], errors='coerce')

# Group and apply different logic to each column
grouped_df = df.groupby(['Order ID', 'Transaction Status']).agg({
    'Quantity': 'sum',               # Sum the numeric values
    'Total Value ($)': 'sum',        # Sum the numeric values
    'Quantity_str': lambda x: ' | '.join(x) # Join the individual strings
}).reset_index()

# Rename the joined column to 'allocations'
grouped_df = grouped_df.rename(columns={'Quantity_str': 'allocations'})

# Reorder columns to put allocations at the end (optional)
grouped_df = grouped_df[['Order ID', 'Transaction Status', 'Quantity', 'Total Value ($)', 'allocations']]

print(grouped_df)