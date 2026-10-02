import csv


with open('data/E0.csv', newline='') as archivo:
    Teams = {}
    reader = csv.DictReader(archivo)
    
    for row in reader:
        Equipo = []
        Equipo.append(row['HomeTeam'])
        Equipo.append(row['AwayTeam'])
        for x in Equipo:
            Teams.setdefault(x,{'PJ':0, 'G':0, 'E':0, 'P':0, 'GF':0, 'GC':0, 'DG':0, 'Pts':0})

        home = Teams[row['HomeTeam']]
        away = Teams[row['AwayTeam']]

        home['PJ'] += 1
        away['PJ'] += 1

        if row['FTR'] == 'H':
            home['G'] += 1
            home['Pts'] += 3
            away['P'] += 1
        elif row['FTR'] == 'D':
            home['E'] += 1
            away['E'] += 1
            home['Pts'] += 1
            away['Pts'] += 1
        else:
            home['P'] += 1
            away['G'] += 1
            away['Pts'] += 3

        home['GF'] += int(row['FTHG'])
        home['GC'] += int(row['FTAG'])
        away['GF'] += int(row['FTAG'])
        away['GC'] += int(row['FTHG'])

        home['DG'] = int(home['GF']) - int(home['GC'])
        away['DG'] = int(away['GF']) - int(away['GC'])

    orden = sorted(Teams.items(), key=lambda x: (x[1]['Pts'],x[1]['DG'],x[1]['GF']), reverse=True)
    posicion = enumerate(orden, start=1)
    print(f"{'Pos':<12}{'Equipo':<28}{'PJ':<10} {'G':<10} {'E':<10}{'P':<10}{'GF':<10}{'GC':<10}{'DG':<10}{'Pts':<10}")
    for pos, (nombre, datos) in posicion:
        print(f'{pos:<10} {nombre:<18} {datos['PJ']:>10} {datos['G']:>10} {datos['E']:>10} {datos['P']:>10} {datos['GF']:>10} {datos['GC']:>10} {datos['DG']:>+10} {datos['Pts']:>10}')

    print(sum(e['PJ'] for e in Teams.values()))
    print(sum(e['GF'] for e in Teams.values()), sum(e['GC'] for e in Teams.values()))
    print(all(e['G'] + e['E'] + e['P'] == e['PJ'] for e in Teams.values()))
    print(all(e['Pts'] == 3*e['G'] + e['E'] for e in Teams.values()))

