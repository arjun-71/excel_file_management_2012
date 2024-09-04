def addFile(number_of_files, year_keyword):
    file_names = []
    for i in range(1, number_of_files + 1):
        if year_keyword == '2012':
            
            file_name = "2012_sample_construction_file_{}.xlsx".format(i)
        elif year_keyword == '2013':
            file_name = "2013_sample_construction_file_{}.xlsx".format(i)
        else:
            raise ValueError("Unsupported year keyword: {}".format(year_keyword))
        file_names.append(file_name)
    return file_names