import pandas as pd

# Use a raw string for the file path
df = pd.read_excel("C:\\xampp\\htdocs\\testsheet.xlsx")

# Find all occurrences of duplicate records based on all columns
duplicates = df[df.duplicated(keep=False)]

# Check if there are any duplicate records
if len(duplicates) > 0:
    # Save all occurrences of duplicates to a new Excel file
    duplicates.to_excel('r2.xlsx', index=False)

    print("All occurrences of duplicates extracted successfully and saved to 'duplicates_only_letsGO.xlsx'.")
else:
    print("No duplicate records found.")
