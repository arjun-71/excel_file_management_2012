import pandas as pd
import os

def get_excel_file_path(excel_filename):
   
    

    # Get the absolute path to the current working directory
    current_directory = os.getcwd()



    # Specify the folder name
    frontend_folder = "frontend"
    uploads_folder = "uploads"

    # Combine the current directory, frontend folder, and the Excel filename to get the full path
    excel_file_path = os.path.join(current_directory, frontend_folder,uploads_folder, excel_filename)
    #print("the excel file path is : ")
    #print(excel_file_path)

    # Combine the current directory and the Excel filename to get the full path
    #excel_file_path = os.path.join(current_directory, excel_filename)
   # print("the current excel file path is")
    #print(excel_file_path)
    return excel_file_path

# Get the Excel file path using the get_excel_file_path() function


# Read the Excel file into a DataFrame
#df = pd.read_excel(excel_path)
#print(df.head())

#excel_file = pd.read_excel(excel_path, sheet_name=None)
#for sheet_name, df_data in excel_file.items():
    #print('Loading worksheet {sheet_name}...')
    

    # {'fail', 'replace', 'append'}
#df_data.to_sql(TABLE_NAME, enigne, if_exists='append', index=False)

