import csv


# Define the nested header structure
def structure_addition(csv_file_name, project_name):
    nested_header = {
        project_name: {
            'Land Acquisition': {
                'Land Acquisition': {
                    'At Construction Budget': '',
                    'Current Budget': '',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                }
            },
            'Construction Costs': {
                'New Construction Shell/Core': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Renovation': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Special Fixed Equipment': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Site Development / Utilities Extensions': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Landscaping / Signage': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Permits': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Demolition': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Hazardous Materials Abatement / Testing': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                }
            },
            'Consultants': {
                'Construction Mgr': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Architect / Engineer': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Surveys and Tests': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Other': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                }
            },
            'Add Univ Costs': {
                'FF & E': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'IT / Telecommunications': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'AV (Audio Visual)': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Security': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Move-in Costs': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Printing/Advertisement/Misc Admin': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Parking Replacement Reserve': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                "Facilities Support (FACMAN PO's Only": {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                }
            },
            'Contingency': {
                'Contingency, Design Phase': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Contingency, Constr Phase': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                }
            },
            'Fees': {
                'Project Management Cost ( 5 % )': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'FS  Fees ( 0.15 % )': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'EH&S Fees ( 0.21 % )': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'Purchasing Fees ( 0.30 % )': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                },
                'State Risk Mgt Ins ( 0.34 % )': {
                    'At Construction Budget': 'value1',
                    'Current Budget': 'value2',
                    'Encumbered': '',
                    'Expensed': '',
                    'Anticipated Costs': '',
                    'Uncommitted Budget': ''
                }
            }
        }
    }

    # Define the file name for the CSV
    csv_file_name = 'nested_header.csv'

    # Write the nested header to a CSV file
    with open(csv_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        def write_nested_header(nested_header, prefix=''):
            for key, value in nested_header.items():
                if isinstance(value, dict):
                    write_nested_header(value, prefix + key + ' - ')
                else:
                    writer.writerow([prefix + key, value])

        write_nested_header(nested_header)
    return csv_file_name


# Call the function to print the structure
#print_nested_structure(nested_header)

