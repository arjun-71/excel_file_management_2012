import csv
import os
import HelperMethods.final_output_file as fsn

def add_data_to_existing_csv(data):
    try:
        # Create the full file path
      

        # Ensure the output folder exists, create it if it doesn't
       

        with open(fsn.resulting_file, mode='a', newline='') as file:  # Use 'a' for append mode
            writer = csv.writer(file)
            writer.writerows(data)  # Append the data as new rows

        
    except Exception as e:
        return f"Error: {str(e)}"
