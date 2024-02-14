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



def addFile(number_of_files):
    file_names = []
    for i in range(1, number_of_files + 1):
        file_name = "2012_sample_construction_file_{}.xlsx".format(i)
        file_names.append(file_name)
    return file_names


    
    