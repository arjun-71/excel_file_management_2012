import pandas as pd
import os

def get_excel_file_path(excel_filename, project_code, year):
    current_directory = os.getcwd()
    frontend_folder = "frontend"
    uploads_folder = "uploads"
    
    # Check if the excel_filename contains '2012' or '2013'
    if '2012' in excel_filename:
        standardized_filename = "2012_sample_construction_file_{}.xlsx".format(project_code)
    elif '2013' in excel_filename:
        standardized_filename = "2013_sample_construction_file_{}.xlsx".format(project_code)
    else:
        # If the filename doesn't contain '2012' or '2013', use the original filename
        standardized_filename = excel_filename

    # Construct the full file path
    excel_file_path = os.path.join(current_directory, frontend_folder, uploads_folder,year, standardized_filename)
    return excel_file_path
