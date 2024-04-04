import csv
import HelperMethods.csv_name_changer as name_changer

def generate_project_csv(project_name, data, project_code):
    # Function to recursively traverse the dictionary and create CSV content
    def flatten_dict(dictionary, header, rows):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                #print(key)
                #print(value)
                header.append(key)
                flatten_dict(value, header, rows)
                header.pop()
            else:
                header.append(key)
                rows.append(header + [""])
                header.pop()

    header = []
    rows = []

    # Start flattening the dictionary
    flatten_dict(data, header, rows)

    # Create a CSV file and write the content
    filename = name_changer.return_Csv_File_Name(project_name, project_code)
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

    return filename