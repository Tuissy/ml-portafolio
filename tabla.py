import csv

with open('data/E0.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    Teams = dict()
    for row in reader:
        Equipos=[]
        Equipos.append(row['HomeTeam'])
        Equipos.append(row['AwayTeam'])
        for x in Equipos:
            Teams.setdefault(x,{'PJ':0, 'G':0, 'E':0, 'P':0, 'GF':0, 'GC':0, 'puntos':0,'DG':0})

        home = Teams[row['HomeTeam']]
        away = Teams[row['AwayTeam']] 

        home['PJ'] += 1
        away['PJ'] += 1

        home['GF'] += int(row['FTHG'])
        away['GF'] += int(row['FTAG'])

        home['GC'] += int(row['FTAG'])
        away['GC'] += int(row['FTHG'])

        if row['FTR'] == 'H':
            home['G'] += 1
            away['P'] += 1
            home['puntos'] += 3
        elif row['FTR'] == 'D':
            home['puntos'] += 1
            away['puntos'] += 1
            home['E'] += 1
            away['E'] += 1
        else:
            away['puntos'] += 3
            home['P'] += 1
            away['G'] += 1  

print(sum(e['PJ'] for e in Teams.values()))                                    # 100
print(sum(e['GF'] for e in Teams.values()), sum(e['GC'] for e in Teams.values()))  # iguales
print(all(e['G'] + e['E'] + e['P'] == e['PJ'] for e in Teams.values()))   # debe dar True
