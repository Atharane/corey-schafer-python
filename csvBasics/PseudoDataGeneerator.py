import csv
import requests

# opening a file, using context manager
with open('pseudoTakeout.csv', 'w') as csvfile:
    # creating a csv writer object
    csv_writer = csv.writer(csvfile)

    # writing the header
    csv_writer.writerow(['Name', 'Age', 'Gender', 'Email-id', 'Contact Number'])

    entries = int(input('Number of entries: '))

    for i in range(entries):
        # writing the data
        data = requests.get('https://randomuser.me/api').json()

        name = data['results'][0]['name']['first'] + ' ' + data['results'][0]['name']['last']
        age = data['results'][0]['dob']['age']
        gender = data['results'][0]['gender']
        email_id = data['results'][0]['email']
        contact_number = data['results'][0]['phone']

        row = [name, age, gender, email_id, contact_number]

        csv_writer.writerow(row)
