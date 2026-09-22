import csv

with open('/Users/hectorfigueredo/Desktop/Curso-Machine Learning/repos/ml-portafolio/ml-portafolio/data/E0.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['HomeTeam'], row['AwayTeam'], row['FTHG'], row['FTAG'])
