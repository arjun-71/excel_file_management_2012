import csv
import HelperMethods.header as hds

#the resulting csv name
csv_file = 'result.csv'

# 2. Open the CSV file in write mode (or 'w' mode).
with open(csv_file, 'w', newline='') as file:
    # 3. Create a CSV writer object.
    csv_writer = csv.writer(file)

    # 4. Write the header row to define the column names.
    
    header = hds.create_updated_header()
    csv_writer.writerow(header)

    # 5. Write data rows to add content to the CSV file.
    data_rows = [
        ['', 30, 'New York'],
        ['Bob', 25, 'Los Angeles'],
        ['Charlie', 35, 'Chicago'],
    ]
    for row in data_rows:
        csv_writer.writerow(row)

# 6. Close the file.
file.close()

print(f'{csv_file} has been created and initialized with data.')
