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
    
