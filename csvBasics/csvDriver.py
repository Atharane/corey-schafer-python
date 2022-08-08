import csv

# using a context manager to open the file
with open('playerdata_2020.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # skip the header row
    next(csv_reader)

    # for line in csv_reader:
    #     print(line)
    #     # line is a list of strings that represent the columns
    #     # print(line[0])

    # writing to a csv file
    with open('playerdata_2020_copy.csv', 'w') as csv_file2:
        # delimiter is the character that separates the columns, default is a comma, it can be  , ; | - tab etc
        csv_writer = csv.writer(csv_file2, delimiter=',')

        # write the header row
        csv_writer.writerow(['Name', 'Nationality', 'Club', 'Rating'])

        for line in csv_reader:
            new_line = [line[1], line[6], line[7], line[8]]
            csv_writer.writerow(new_line)

#  reading and writing using dictionary
with open('playerdata_2020.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line)

    # writing to a csv file using dictionary
    with open('playerdata_2020_copy.csv', 'w') as csv_file2:
        fieldnames = ['long_name', 'nationality', 'club', 'overall']  # fieldnames is a list of headers

        # arguments fieldnames is optional
        csv_writer = csv.DictWriter(csv_file2, fieldnames=fieldnames)

        csv_writer.writeheader()  # write the header row, writes the fieldnames

        for line in csv_reader:
            print(line)
            # this will write the dictionary as a row
            csv_writer.writerow(
                {'long_name': line['long_name'], 'nationality': line['nationality'], 'club': line['club'],
                 'overall': line['overall']})
