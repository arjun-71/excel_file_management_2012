def return_Csv_File_Name(name_of_the_project, project_code):
    name_of_the_project = name_of_the_project.replace(" ", "")
    project_code = project_code.replace(" ","")
    new_csv_file_name = f"{name_of_the_project}-{project_code}.csv"
    return new_csv_file_name
     