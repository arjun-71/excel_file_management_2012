from sqlalchemy import create_engine  # Importing SQLAlchemy for creating a connection to the database
import psycopg2  # Importing psycopg2 for PostgreSQL database connection
import pandas as pd  # Importing pandas for handling data in dataframes
import HelperMethods.FilePathReturn as fp  # Importing file path helper methods
import numpy as np  # Importing numpy for numerical operations
import HelperMethods.DatabaseString as dbs  # Importing database connection string helper
import HelperMethods.ExcelToCsv as converter  # Importing method to convert Excel files to CSV
import HelperMethods.csv_name_changer as nameChanger  # Importing method for naming CSV files
import dataManagement.dataBody as dsn  # Importing data management helper methods
import HelperMethods.InformationToObject as objectInserter  # Importing method for inserting data into objects
import HelperMethods.header2 as hds  # Importing header method for CSVs
import HelperMethods.header3 as hds2  # Importing another header method for CSVs
import csv  # Importing the CSV module for handling CSV files
import dataManagement.csv_file_schema as csv_schema  # Importing CSV file schema for validation
import os  # Importing os for file path manipulation
import HelperMethods.resultant_file as rsf  # Importing method for handling resultant file
import HelperMethods.final_output_file as fsn  # Importing method for final output file
import HelperMethods.file_handling_method as fhm  # Importing file handling methods
import sys  # Importing sys for handling system-level operations
import HelperMethods.returnFolderCount as rtn  # Importing method for counting files in folder

# Setting up database connection
databaseConnectionString = dbs.db_url  # Database connection string from helper method
engine = create_engine(databaseConnectionString)  # Creating a connection to the database using SQLAlchemy

# Define file paths and initialize variables
BudgetData_directory = os.path.dirname(os.path.realpath('dataBody.py'))  # Get directory of dataBody.py
sys.path.append(BudgetData_directory)  # Add the directory to system path for module access

file_budget_mapping = {}  # Dictionary to map file names to budget data
budget_data_list = []  # List to store budget data

# Define the resultant CSV file name
resultant_file = 'resultant_file.csv'

# Define year constants
year_2012 = "2012"
year_2013 = "2013"

# Function to process files for the year 2013
def processing2013File(year: str):

    if year == "2013":
        # Get the count of files in the 2013 folder
        count = rtn.count_files_in_folder('/Users/saiarjunshroff/Desktop/2012/excel_file_management_2012/frontend/uploads/2013')
    
    # Add files to process from the folder
    file_list = fhm.addFile(count, "2013")         

    # Loop through each file in the file list
    for i in range(len(file_list)):
       
       # Get the current directory and construct the full path to the Excel file
       current_directory = os.getcwd()
       frontend_folder = "frontend"
       uploads_folder = "uploads"
       year = "2013"
       excel_file_path = os.path.join(current_directory, frontend_folder, uploads_folder, year, file_list[i])
       
       # Convert the Excel file to a DataFrame
       csv_data = converter.fileConverter(excel_file_path)
       first_row = csv_data.iloc[1]  # Get the second row of the CSV (likely headers)
       first_column = csv_data.iloc[:, 0]  # Get the first column (likely project names or codes)

       # Extract project name and project code from the first row and column
       name_in_the_file = first_row.iloc[0]
       project_code = csv_data.columns[1]
       parts = project_code.split('/')
       
       if len(parts) >= 2:
            # If the project code contains a '/', split it into project name and code
            name_of_the_project = parts[0].strip()
            project_code = parts[1].strip()
       else:
            # If no '/' in the project code, set both to None
            name_of_the_project = None
            project_code = None

       # Generate a new CSV file name using project name and code
       new_csv_file_name = nameChanger.return_Csv_File_Name(name_of_the_project, project_code)           
       # Save the CSV data to a new file
       csv_data.to_csv(new_csv_file_name, index=False)

       # Read the newly saved CSV data into a DataFrame
       new_csv_data = pd.read_csv(new_csv_file_name)

       # Process the CSV data to create a budget data object
       budgetData = objectInserter.process_csv_data_2013(new_csv_data, name_of_the_project)        
       # Extract a specific value related to additional university costs from the budget data
       result = budgetData.data[name_of_the_project].get('Additional University Costs')

       # Generate the resultant file (output) for the project
       resultant_file = hds2.generate_project_csv(name_of_the_project, csv_schema.data, project_code)
       
       # Read the resultant file into a DataFrame
       df = pd.read_csv(resultant_file)

       # Extract the fourth column from the resultant file
       fourth_column = df.iloc[:, 3]
       # Append the processed budget data to the list
       budget_data_list.append(budgetData)
    
       # Map the new CSV file name to the processed budget data
       file_budget_mapping[new_csv_file_name] = budgetData

       # Access the processed budget data
       budgetData = file_budget_mapping[new_csv_file_name]

       unnamed_3_values = []  # List to store unnamed column values
       total = 0.0  # Initialize a variable to store total value

       # Loop through each row in the DataFrame
       for index, row in df.iterrows():

            # Extract the values of specific columns
            column1_value = row['Land Acquisition']
            column2_value = row['CLAC']
            column3_value = row['Appropriated Budget']

            # Check if the column3_value is one of the specified categories
            if column3_value in ["Expensed", 'Appropriated Budget', 'Budget Adjustments', 'Adjusted Budget', 'Encumbered', 'Anticipated Costs', 'Uncommitted Budget']:
                # Retrieve the corresponding value from the budget data
                value = budgetData.data[name_of_the_project].get(column1_value, {}).get(column2_value, {}).get(column3_value, None)
                
                # If the value is not None, try to convert it to a float
                if value:
                    try:
                        if value.strip():  # If value is not empty, convert it to float
                            float_value = float(value)
                            if float_value >= 0.0:  # Ensure that the value is non-negative
                                # Create a new DataFrame with the values and append to the result CSV
                                df = pd.DataFrame([[project_code, column1_value, column2_value, column3_value, float_value]],
                                                  columns=['name_of_the_project', 'column1_value', 'column2_value', 'column3_value', 'float_value'])

                                # Define the file name and destination for saving the result
                                file_name = "result.csv"
                                current_folder = os.getcwd()
                                current_folder_destination = os.path.join(current_folder, 'resulting_file')
                                resulting_file = os.path.join(current_folder_destination, file_name)

                                # Save the DataFrame to the result file, appending if it already exists
                                df.to_csv(resulting_file, mode='a', header=not os.path.exists(resulting_file), index=False)

                    except ValueError:
                        pass

            # Check if the value is numeric and process accordingly
            checker = 0
            value = None
            if value is not None and value.strip() != '':
                checker = 0
                try:
                    decimal_value = float(value)
                except ValueError:
                    checker = 1
            else:
                checker = 2

            # If the checker is 0 (valid value), add it to the total and store in the DataFrame
            if checker == 0:
                total += decimal_value
                df.at[index, 'Unnamed: 3'] = decimal_value

       # Get the final destination folder for saving the processed file
       current_folder = os.getcwd()
       current_folder_destination = os.path.join(current_folder, 'resulting_file')
       file_path = os.path.join(current_folder_destination, resultant_file)

       # Save the final DataFrame to the file
       df.to_csv(file_path, index=False)

       # Prepare data for saving to the final result CSV
       data = [[name_of_the_project, project_code, total, total]]
       # Add data to the existing resultant CSV
       rsf.add_data_to_existing_csv(data)

# Function to process files for the year 2012
def processing2012File(year: str):

    if year == "2012":
        # Get the count of files in the 2012 folder
        count = rtn.count_files_in_folder("/Users/saiarjunshroff/Desktop/2012/excel_file_management_2012/frontend/uploads/2012")   

    # Add files to process from the folder
    file_list = fhm.addFile(count, "2012")           
    for i in range(len(file_list)):                             
        
        # Get the current directory and construct the full path to the Excel file
        current_directory = os.getcwd()
        frontend_folder = "frontend"
        uploads_folder = "uploads"
        year = "2012"
        excel_file_path = os.path.join(current_directory, frontend_folder, uploads_folder, year, file_list[i])
        
        # Convert the Excel file to a DataFrame
        csv1 = converter.fileConverter(excel_file_path)
        project_code = csv1.columns[1]
        parts = project_code.split('/')
        
        if len(parts) >= 2:
            # If the project code contains a '/', split it into project name and code
            name_of_the_project = parts[0].strip()
            project_code = parts[1].strip()
        else:
            name_of_the_project = None
            project_code = None
        

        # Get the full file path for processing
        filePath = fp.get_excel_file_path(file_list[i], i+1, year)         
        

        # Convert the file to a DataFrame
        csv = converter.fileConverter(filePath)

        first_row = csv.iloc[1]
        first_column = csv.iloc[:, 0]

        name_in_the_file = first_row.iloc[0]
        project_code = csv.columns[1]
        parts = project_code.split('/')
        
        if len(parts) >= 2:
            # Extract project name and code from the first row
            name_of_the_project = parts[0].strip()
            project_code = parts[1].strip()
        else:
            name_of_the_project = None
            project_code = None

        # Generate the new CSV file name
        new_csv_file_name = nameChanger.return_Csv_File_Name(name_of_the_project, project_code)
    
        # Save the CSV data to the new file
        csv.to_csv(new_csv_file_name, index=False)     

        # Read the CSV data back into a DataFrame
        new_csv_data = pd.read_csv(new_csv_file_name)

        # Process the data into a budget data object
        budgetData = objectInserter.process_csv_data(new_csv_data, name_of_the_project)       
        result = budgetData.data[name_of_the_project].get('Additional University Costs')

        # Generate the resultant CSV file for the project
        resultant_file = hds2.generate_project_csv(name_of_the_project, csv_schema.data, project_code)
        df = pd.read_csv(resultant_file)

        # Extract values and process data as in the 2013 file processing function
        fourth_column = df.iloc[:, 3]
        budget_data_list.append(budgetData)
        file_budget_mapping[new_csv_file_name] = budgetData

        budgetData = file_budget_mapping[new_csv_file_name]

        unnamed_3_values = []
        total = 0.0

        for index, row in df.iterrows():
            column1_value = row['Land Acquisition']
            column2_value = row['CLAC']
            column3_value = row['Appropriated Budget']

            if column3_value in ["Expensed", 'Appropriated Budget', 'Budget Adjustments', 'Adjusted Budget', 'Encumbered', 'Anticipated Costs', 'Uncommitted Budget']:
                value = budgetData.data[name_of_the_project].get(column1_value, {}).get(column2_value, {}).get(column3_value)
                
                if value and value.strip():
                    try:
                        float_value = float(value)
                        df = pd.DataFrame([[name_of_the_project, column1_value, column2_value, column3_value, float_value]],
                                        columns=['name_of_the_project', 'column1_value', 'column2_value', 'column3_value', 'float_value'])
                        file_name = "result.csv"
                        current_folder = os.getcwd()
                        current_folder_destination = os.path.join(current_folder, 'resulting_file')
                        resulting_file = os.path.join(current_folder_destination, file_name)
                        df.to_csv(resulting_file, mode='a', header=not os.path.exists(resulting_file), index=False)
                    except ValueError:
                        pass

            checker = 0
            value = None
            if value and value.strip():
                checker = 0
                try:
                    decimal_value = float(value)
                except ValueError:
                    checker = 1
            else:
                checker = 2
            
            if checker == 0:
                total += decimal_value
                df.at[index, 'Unnamed: 3'] = decimal_value

        # Final output path and saving
        current_folder = os.getcwd()
        current_folder_destination = os.path.join(current_folder, 'resulting_file')       
        file_path = os.path.join(current_folder_destination, resultant_file)
       
        df.to_csv(file_path, index=False)

        # Add data to final output CSV
        data = [[name_of_the_project, project_code, total, total]]
        rsf.add_data_to_existing_csv(data)

# Call the function to process 2012 files
processing2012File('2012')
