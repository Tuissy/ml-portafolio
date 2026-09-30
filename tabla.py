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

        home['DG'] = home['GF'] - home['GC']
        away['DG'] = away['GF'] - away['GC']


print(sum(e['PJ'] for e in Teams.values()))                                    # 100
print(sum(e['GF'] for e in Teams.values()), sum(e['GC'] for e in Teams.values()))  # iguales
print(all(e['G'] + e['E'] + e['P'] == e['PJ'] for e in Teams.values()))   # debe dar True

orden = sorted(Teams.items(), key=lambda x: (x[1]['puntos'],x[1]['DG'],x[1]['GF']), reverse=True)
posicion = enumerate(orden, start=1)

print(f'{"Pos":<10} {"Equipo":<23} {"PJ":>10} {"G":>10} {"E":>10} {"P":>10} {"GF":>10} {"GC":>10} {"DG":>10} {"Pts":>10}')

for pos, (nombre, datos) in posicion:
    print(f"{pos:<10} {nombre:<23} {datos['PJ']:>10} {datos['G']:>10} {datos['E']:>10} {datos['P']:>10} {datos['GF']:>10} {datos['GC']:>10} {datos['DG']:>+10} {datos['puntos']:>10}")