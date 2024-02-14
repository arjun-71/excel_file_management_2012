import os 
import csv


column_headings = ["Project_Name", "Project_Number", "Total_Expense", "Sum"]
file_name = "result.csv"

current_folder = os.getcwd()
current_folder_destination = os.path.join(current_folder, 'resulting_file')
resulting_file = os.path.join(current_folder_destination, file_name)


with open(resulting_file,  mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(column_headings)  # Write the column headings)