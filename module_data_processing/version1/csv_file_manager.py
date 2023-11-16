# -*- coding: utf-8 -*-
import csv


# name file csv
name_csv = input("Entrer le nom du fichier CSV: ")
csv_path = name_csv + ".csv"

name_Region = input("Entrer le nom de la Region: ").lower().capitalize()
name_dep = input("Entrer le nom du Departement: ").lower().capitalize()
parrain = "Non"


# initialize the title and the rows list
header = ['id', 'num electeur', 'Prénom(s)', 'Nom', 'Date Naiss', 'Commune', 'Lien de vote', 'Bureau','Parrain', 'Region', 'Departement']
content = []
data_head = []

commune = None
lieu_vote = None
office = None

ignore_header = ['N� �lecteur', '', 'Pr�nom(s)', 'Nom', 'Date Naiss.']

# Read File CSV Elector
try:
    with open(csv_path, 'r', encoding="utf-8", errors="replace") as csv_f:
        csv_reader = csv.reader(csv_f)

        first_com = next(csv_reader)
        data_head.append(first_com)
        for line in csv_reader:
            if len(line) < 3:
                data_head.append(line)
            elif line == ignore_header:
                for x in range(len(data_head)):
                    if x == 0:
                        commune = data_head[x][0]
                    if x == 1:
                        lieu_vote = data_head[x][0]
                    if x == 2:
                        office = data_head[x][0]
            else:

                line.append(commune)
                line.append(lieu_vote)
                line.append(office)
                line.append(parrain)
                line.append(name_Region)
                line.append(name_dep)
                line = list(filter(None, line))
                line.insert(0, '')
                content.append(line)

                data_head.clear()

    # name of csv file
    csv_name = name_csv+".csv"
    with open(csv_name, 'w', newline="", encoding="utf-8", errors="replace") as csv_file:
        # creating a csv writer object
        csv_writer = csv.writer(csv_file)

        # ecrire les en-tetes (fields)
        csv_writer.writerow(header)

        # remplir les colonnes (rows)
        for elector in content:
            csv_writer.writerow(elector)
            
except EnvironmentError as e:
    print("Impossible d'ouvrir le fichier. [", e, "]")