import csv
def cvReader():
    with open("team.csv", 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            print(dict(row))

cvReader()