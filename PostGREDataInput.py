from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import HelperMethods.FilePathReturn as  fp
import numpy as np
import HelperMethods.DatabaseString as dbs
import HelperMethods.ExcelToCsv as converter
import HelperMethods.csv_name_changer as nameChanger
import dataManagement.dataBody as dsn 
import dataManagement.dataBody
import HelperMethods.InformationToObject as objectInserter
import HelperMethods.header2 as hds     
import HelperMethods.header3 as hds2
import csv
import dataManagement.csv_file_schema as csv_schema
import os
import HelperMethods.resultant_file as rsf
import HelperMethods.final_output_file as fsn
import HelperMethods.file_handling_method as fhm


# Replace {key} with your actual database connection details
databaseConnectionString = dbs.db_url
engine = create_engine(databaseConnectionString)   

#create a dictionary with the new csv file name as the key value and the corresponding budgetData created as the value pair
file_budget_mapping = {}

# Create a list to store BudgetData objects
budget_data_list = []        #declare this as global variable     



#name of the resultant csv file
resultant_file = 'resultant_file.csv'

#alter the addresses based upon the aws lamda function 

#file entry point
#the function for entry of the file 






#extracting the file path

file_list = fhm.addFile(1)           #the following will not work as we are not changing the file name itself
print(file_list)

for i in range(0,1):      

  filePath = fp.get_excel_file_path(file_list[i])
  print(filePath)
  





  
  #converting excel file to csv file
  #start here

  csv = converter.fileConverter(filePath)       #this is working
  #print(csv.head())


  first_row = csv.iloc[1]
  print(first_row)
  first_column = csv.iloc[:, 0]
  #print(first_column)

  #the following variable contains the name mentioned in the file
  name_in_the_file =first_row.iloc[0] 
  print(name_in_the_file)
  #name_of_the_project = csv.columns[3]
  #print(name_of_the_project)              
  project_code = csv.columns[1]         #the following splits the name of the file into three segments
  parts = project_code.split('/')
  if len(parts) >= 2:
    name_of_the_project = parts[0].strip()  # Get the first part as name_of_the_project
    project_code = parts[1].strip()  # Get the second part as project_code
  else:
    name_of_the_project = None  # Handle the case where there are not enough parts
    project_code = None
  



  # Generate a new CSV file name without spaces
  new_csv_file_name = nameChanger.return_Csv_File_Name(name_of_the_project, project_code)
  #print(new_csv_file_name)
  print("the new resulting csv file name")
  print(new_csv_file_name)


  #update the name in the folder as well 

  # Save the DataFrame to the new CSV file
  csv.to_csv(new_csv_file_name, index=False)

  # Read and print the first few rows of the new CSV file
  new_csv_data = pd.read_csv(new_csv_file_name)

  #print(new_csv_data.head())

  # the following object created contains the lew object of type cost 
  budgetData = objectInserter.process_csv_data(new_csv_data, name_of_the_project)  



  #print(budgetData.get_value(name_of_the_project))


  #checking the functionality of new csv generator engine

  #print(csv_schema.data)

  resultant_file = hds2.generate_project_csv(name_of_the_project, csv_schema.data, project_code)
  print(f'CSV file "{resultant_file}" has been created for the project "{name_of_the_project}".')

  df = pd.read_csv(resultant_file)

  #print(df.head(30))

  fourth_column = df.iloc[:, 3] 
  #print(fourth_column)

  #the following adds and maps the new object created and maps it to the required file name
  budget_data_list.append(budgetData)

  #the following dictionary contains the budget data schema for every csv file
  file_budget_mapping[new_csv_file_name] = budgetData

  #print(budget_data_list[0].get_value(['Polytechnic Zoom Classrooms & Space Upgrades','Construction Costs','Renovation']))


  # Read the CSV file into a DataFrame


  # Loop through all rows in the DataFrame
  ##or fileName, budgetData in file_budget_mapping.items():
  budgetData = file_budget_mapping[new_csv_file_name]             #name of the dictionary for csv file mapping 
  #print(budgetData.get_value(name_of_the_project))
      
  # Create an empty list to store values for 'Unnamed: 3'
  unnamed_3_values = []
  current_Budget_Total = 0
  encumbered_Total = 0
  Expensed_Total = 0
  anticipated_Total = 0
  uncommitted_Total = 0
  total = 0.0

  for index, row in df.iterrows():                #figure this out please its irritating 
      column1_value = row['Land Acquisition']
      column2_value = row['Land Acquisition.1']
      column3_value = row['At Construction Budget']

      if column3_value == "Expensed":
        
        value = budgetData.get_value([name_of_the_project, column1_value, column2_value, column3_value])
        checker = 0
        
        if value is not None and value.strip() != '':
          checker = 0
          try:
              decimal_value = float(value)
              #print(decimal_value)
          except ValueError:
              checker = 1
        else:

          checker = 2
        #find the value of the five column values
        if checker == 0:
          



        #if(budgetData.get_value([name_of_the_project, column1_value, column2_value, column3_value])!= None):
          #print(column1_value, column2_value, column3_value)
          #print(budgetData.get_value([name_of_the_project, column1_value, column2_value, column3_value]))
          total = total + decimal_value
          #print(column1_value+" "+column2_value+" "+column3_value)
          df.at[index, 'Unnamed: 3'] = decimal_value    

          #value_str = budgetData.get_value([name_of_the_project, column1_value, column2_value, column3_value])
    

  # Check if the string is not empty and is a valid numeric value
          #if value_str.strip() != '':
            # integer_value = float(value_str)
            #  current_Budget_Total+=integer_value
        # print(budgetData.get_value([name_of_the_project, column1_value, column2_value,column3_value]))
        
        # current_Budget_Total+= float(budgetData.get_value([name_of_the_project, column1_value, column2_value, column3_value]))
    # if(column3_value == 'Encumbered' and budgetData.get_value([name_of_the_project, column1_value, column2_value, column3_value])!= None):
      #   encumbered_Total+= float(budgetData.get_value([name_of_the_project, column1_value, column2_value, column3_value]))
    # if(column3_value == 'Expensed' and budgetData.get_value([name_of_the_project, column1_value, column2_value, column3_value])!= None):
      #   Expensed_Total+= float(budgetData.get_value([name_of_the_project, column1_value, column2_value, column3_value]))
    #  if(column3_value == 'Anticipated Costs' and budgetData.get_value([name_of_the_project, column1_value, column2_value, column3_value])!= None):
    #     anticipated_Total+= float(budgetData.get_value([name_of_the_project, column1_value, column2_value, column3_value]))
    # if(column3_value == 'Uncommitted Budget' and budgetData.get_value([name_of_the_project, column1_value, column2_value, column3_value])!= None):
      #    uncommitted_Total+= float(budgetData.get_value([name_of_the_project, column1_value, column2_value, column3_value]))
      
      
      #print(column1_value, column2_value, column3_value)        

      # Calculate the value you want to set for 'Unnamed: 3' based on budgetData
      #unnamed_3_value = budgetData.get_value([name_of_the_project, column1_value, column2_value, column3_value])
      
      # Append the calculated value to the list
      #unnamed_3_values.append(unnamed_3_value)

  # Assign the list of 'Unnamed: 3' values to the DataFrame

    

  # Print the first few rows of the DataFrame

  #print(df.head(60))   
  print(resultant_file)

  print(uncommitted_Total)

  print(total)


  #create the resultant file and add to the final output file here



  current_folder = os.getcwd()   
  current_folder_destination = os.path.join(current_folder,'resulting_file')




  file_path = current_folder_destination + "/"+resultant_file


  # Save the DataFrame to the specified file path
  df.to_csv(file_path, index=False)  # index=False to avoid saving the index column


  #create the file
  #call the global scope file declared in the function 
  #in the function write the data
  #return the updated file back to the main file



  column_headings = ["Project_Name,Project_Number,Total_Expense,sumz"]
  data = [
      [name_of_the_project, project_code, total, total]
  ]

  # Define your column headings as separate elements in a list
  column_headings = ["Project_Name", "Project_Number", "Total_Expense", "Sum"]

  # Define your data with actual values


  data = [
      [name_of_the_project, project_code, total, total]
  ]

  file_name = "result.csv"

  current_folder = os.getcwd()
  current_folder_destination = os.path.join(current_folder, 'resulting_file')
  resulting_file = os.path.join(current_folder_destination, file_name)
  #print(resulting_file)

  #file_path = current_folder_destination + "/"+"resulting_file"

  rsf.add_data_to_existing_csv(data)



















    # Process or print the values as needed
   #getting the corresponsding value from the budgetData
    






     
     
     


#print (budgetData['Polytechnic Zoom Classrooms & Space Upgrades']['Construction Costs']['Renovation'])
            
            #use the insert function here please
#print(project_code_value)
#print(budgetData.get_value(['Polytechnic Zoom Classrooms & Space Upgrades']))
#print(budgetData.get_value(['Polytechnic Zoom Classrooms & Space Upgrades', 'Land Acquisition', 'Land Acquisition', 'At Construction Budget']))  # This will print 'new_value'

                
#print(field_List)  #the following list contains the list of all major fields for the above costs  

 

#creating a dictionary data structure for storing  values 


# def extract_and_insert_single_sheet(sheet_name, excel_file, table_name):
#     df = pd.read_excel(excel_file, sheet_name)
#     df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

# # Replace 'main.xlsx' with the actual path to your Excel file
# excel_file_path = filePath
# sheet_name_to_process = 'Sheet1'  # Replace with the desired sheet name
# table_name_to_insert = dbs.table_name  # Replace with the desired table name

# extract_and_insert_single_sheet(sheet_name_to_process, excel_file_path, table_name_to_insert)