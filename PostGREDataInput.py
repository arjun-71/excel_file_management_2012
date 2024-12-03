from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import HelperMethods.FilePathReturn as fp
import numpy as np
import HelperMethods.DatabaseString as dbs
import HelperMethods.ExcelToCsv as converter
import HelperMethods.csv_name_changer as nameChanger
import dataManagement.dataBody as dsn
import HelperMethods.InformationToObject as objectInserter
import HelperMethods.header2 as hds
import HelperMethods.header3 as hds2
import csv
import dataManagement.csv_file_schema as csv_schema
import os
import HelperMethods.resultant_file as rsf
import HelperMethods.final_output_file as fsn
import HelperMethods.file_handling_method as fhm
import sys
import HelperMethods.returnFolderCount as rtn


databaseConnectionString = dbs.db_url
engine = create_engine(databaseConnectionString)

BudgetData_directory = os.path.dirname(os.path.realpath('dataBody.py'))
sys.path.append(BudgetData_directory)

file_budget_mapping = {}
budget_data_list = []

resultant_file = 'resultant_file.csv'

year_2012 = "2012"
year_2013 = "2013"

def processing2013File(year: str):

    if year == "2013":
        count = rtn.count_files_in_folder('/Users/saiarjunshroff/Desktop/2012/excel_file_management_2012/frontend/uploads/2013')
    
    file_list = fhm.addFile(count,"2013")         

    for i in range(len(file_list)):
       
       current_directory = os.getcwd()
       frontend_folder = "frontend"
       uploads_folder = "uploads"
       year = "2013"
       excel_file_path = os.path.join(current_directory, frontend_folder, uploads_folder, year, file_list[i])
       
       csv_data = converter.fileConverter(excel_file_path)
       first_row = csv_data.iloc[1]
       first_column = csv_data.iloc[:, 0]

       name_in_the_file = first_row.iloc[0]
       project_code = csv_data.columns[1]
       parts = project_code.split('/')
       if len(parts) >= 2:

            name_of_the_project = parts[0].strip()
            project_code = parts[1].strip()
       else:
            name_of_the_project = None
            project_code = None

       new_csv_file_name = nameChanger.return_Csv_File_Name(name_of_the_project, project_code)           
       csv_data.to_csv(new_csv_file_name, index=False)
   

       new_csv_data = pd.read_csv(new_csv_file_name)

       budgetData = objectInserter.process_csv_data_2013(new_csv_data, name_of_the_project)        
       result = budgetData.data[name_of_the_project].get('Additional University Costs')

       resultant_file = hds2.generate_project_csv(name_of_the_project, csv_schema.data, project_code)
       
       df = pd.read_csv(resultant_file)

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
            value = budgetData.data[name_of_the_project].get(column1_value, {}).get(column2_value, {}).get(column3_value, None)
            
            if value:
                try:
                    if value.strip():
                        float_value = float(value)
                        if float_value >= 0.0:
                            df = pd.DataFrame([[project_code, column1_value, column2_value, column3_value, float_value]],
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
        if value is not None and value.strip() != '':
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

    current_folder = os.getcwd()
    current_folder_destination = os.path.join(current_folder, 'resulting_file')
    file_path = os.path.join(current_folder_destination, resultant_file)

    df.to_csv(file_path, index=False)


    data = [[name_of_the_project, project_code, total, total]]
    rsf.add_data_to_existing_csv(data)


def processing2012File(year: str):

    if year == "2012":
        count = rtn.count_files_in_folder("/Users/saiarjunshroff/Desktop/2012/excel_file_management_2012/frontend/uploads/2012")        

    file_list = fhm.addFile(count,"2012")           
    for i in range(len (file_list)):
        
        current_directory = os.getcwd()
        frontend_folder = "frontend"
        uploads_folder = "uploads"
        year = "2012"
        excel_file_path = os.path.join(current_directory, frontend_folder, uploads_folder, year, file_list[i])
        
        csv1 = converter.fileConverter(excel_file_path)
        project_code = csv1.columns[1]
        parts = project_code.split('/')
        if len(parts) >= 2:
            name_of_the_project = parts[0].strip()
            project_code = parts[1].strip()
        else:
            name_of_the_project = None
            project_code = None
        

        filePath = fp.get_excel_file_path(file_list[i], i+1, year)         
        

        csv = converter.fileConverter(filePath)

        first_row = csv.iloc[1]
        first_column = csv.iloc[:, 0]

        name_in_the_file = first_row.iloc[0]
        project_code = csv.columns[1]
        parts = project_code.split('/')
        if len(parts) >= 2:
            name_of_the_project = parts[0].strip()
            project_code = parts[1].strip()
        else:
            name_of_the_project = None
            project_code = None

        new_csv_file_name = nameChanger.return_Csv_File_Name(name_of_the_project, project_code)
    
        csv.to_csv(new_csv_file_name, index=False)     

        new_csv_data = pd.read_csv(new_csv_file_name)

        budgetData = objectInserter.process_csv_data(new_csv_data, name_of_the_project)       
        result = budgetData.data[name_of_the_project].get('Additional University Costs')

        resultant_file = hds2.generate_project_csv(name_of_the_project, csv_schema.data, project_code)
        df = pd.read_csv(resultant_file)

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

        current_folder = os.getcwd()
        current_folder_destination = os.path.join(current_folder, 'resulting_file')       
        file_path = os.path.join(current_folder_destination, resultant_file)
        df.to_csv(file_path, index=False)

        data = [[name_of_the_project, project_code, total, total]]
        rsf.add_data_to_existing_csv(data)

processing2013File('2013')
