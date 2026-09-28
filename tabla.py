import csv

with open('data/E0.csv', newline='') as csvfile:

    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['HomeTeam'], row['AwayTeam'], row['FTHG'], row['FTAG'])
