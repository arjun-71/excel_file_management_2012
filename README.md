Construction Budget Data Processing

This project processes Excel files related to construction budget data from the years 2012 and 2013. The program converts Excel files to CSV format, processes the data, and generates resultant CSV files containing budget information for university construction projects.

 Features:
- Converts Excel files to CSV format.
- Processes the budget data and inserts it into a database.
- Generates resultant CSV files containing relevant budget data.
- Supports data validation and error handling.

 Dependencies:
To run the project, ensure the following dependencies are installed:
-  SQLAlchemy : for database connection.
-  psycopg2 : PostgreSQL adapter for Python.
-  pandas : for handling data in dataframes.
-  numpy : for numerical operations.
-  os : for file path manipulation.
-  csv : for handling CSV files.

To install these dependencies, use:
   bash
pip install sqlalchemy psycopg2 pandas numpy
   

Usage:

1. Store Excel files in the Frontend Folder:
   Place the Excel files you want to process into the  frontend/uploads/2012  or  frontend/uploads/2013  folders, depending on the year.

2. Run the Code:
   - To process files from 2012, use the following command:
        bash
     python your_script.py processing2012File('2012')
        

   - To process files from 2013, use the following command:
        bash
     python your_script.py processing2013File('2013')
        

3. Output:
   After running the script, the processed data will be stored in the  resulting_file  folder as CSV files. You can check the folder for the resultant CSV files.

Notes:
- Ensure your environment has access to the necessary file paths (e.g.,  frontend/uploads/2012  or  frontend/uploads/2013 ).
- The code assumes the Excel files are structured in a specific format with columns for  Land Acquisition ,  CLAC , and  Appropriated Budget .
