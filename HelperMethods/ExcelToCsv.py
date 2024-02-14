import pandas as pd
import os

def fileConverter(excel_file_address):
    # Check if the Excel file exists
    
    if not os.path.isfile(excel_file_address):
        return None  # Return None if the file does not exist
    
    # Define the output CSV file name (you can customize this)
    csv_file_name = "output.csv"
    
    try:
        # Convert the Excel file to a CSV file
        df = pd.read_excel(excel_file_address, engine="openpyxl")
        df.to_csv(csv_file_name, index=False)
        
        # Read the CSV file into a pandas DataFrame
        converted_df = pd.read_csv(csv_file_name)
        
        
        return converted_df
    except Exception as e:
        return None
    