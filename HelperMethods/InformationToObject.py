import pandas as pd
import numpy as np
import HelperMethods.DatabaseString as dbs
import HelperMethods.ExcelToCsv as converter
import HelperMethods.csv_name_changer as nameChanger
import dataManagement.dataBody as dsn 
import dataManagement.dataBody
import HelperMethods.InformationToObject as objectInserter


def process_csv_data(new_csv_data, name_of_the_project):
    codekey_one = ""
    project_name = ""
    section_value = ""
    sub_section_value = ""
    project_code_value = ""
    budgetData = dataManagement.dataBody.BudgetData(name_of_the_project)  # Initialize an empty DataFrame for budgetData

    for index, row in new_csv_data.iterrows():
        project_code_value = new_csv_data.columns[0]

        for column_name, value in row.items():
            if index == 0 and value == "Current Budget":
                project_name = column_name
            if column_name == "Unnamed: 1" and value != "0" and pd.notna(value) and index > 1:
                section_value = value

            if pd.notna(value) and index > 3 and index < 38:
                column_field_value = budgetData.replace_value(column_name)
                print(column_field_value + "->")
                if column_name == project_code_value:
                    sub_section_value = value
                    print(column_field_value)
                if column_field_value in ['Encumbered', 'Expensed', 'Anticipated Costs', 'Uncommitted Budget', 'Current Budget', 'At Construction Budget','Appropriated Budget','Budget Adjustments','Adjusted Budget'] and sub_section_value.find("Subtotal") == -1:
                    budgetData.set_value([project_name, section_value, sub_section_value, column_field_value], value)
                    #print(project_name,section_value, sub_section_value, column_field_value)
                    print(value)
    

    return budgetData
