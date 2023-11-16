# -*- coding: utf-8 -*-
import csv
import sys
import pathlib


# ouvrir un dossier
# parcourir les fichiers d'un dossier
# organiser les données 
# creer un ficher electeur pour la commune
# ajouter les communes dans le fichier commune
# ajouter les électeurs dans le fichier électeur global



header = ['id', 'num electeur', 'Prénom(s)', 'Nom', 'Date Naiss', 'cni', 'date_exp', 'phone', 'Commune', 'centre', 'Bureau','Parrain',]
ignore_header = ['N� �lecteur', '', 'Pr�nom(s)', 'Nom', 'Date Naiss.']

content = []
data_head = []
commune = []
dep = None
id_commune = None
parrain = "Non"
cni = ''
date_exp = ''
phone = ''
name_commune = None
lieu_vote = None
office = None

name_centre = set()
centres = []



try:
    dep = int(input("Entrer ID Département: "))
    id_commune = int(input("Entrer ID Commune: "))
    path_dir = pathlib.Path(sys.argv[1]) # convertir un argument en chemin 
except IndexError:
    sys.exit("Vous devez passer en paraametre un chemin vers un fichier Historique.")


directory = pathlib.Path(str(path_dir))
for path in directory.iterdir():

    # Read File CSV Elector
    try:
        with open(path, 'r', encoding="utf-8", errors="replace") as csv_f:
            csv_reader = csv.reader(csv_f)
            first_com = next(csv_reader)
            
            # contenant data communes
            commune.append(first_com[0])
            commune.insert(0, '')
            commune.append(dep)

            data_head.append(first_com)
            for line in csv_reader:
                if len(line) < 3:
                    data_head.append(line)
                elif line == ignore_header:
                    for x in range(len(data_head)):
                        if x == 0:
                            name_commune = data_head[x][0]
                        if x == 1:
                            lieu_vote = data_head[x][0]
                        if x == 2:
                            office = data_head[x][0]
                else:
                    line.append(name_commune)
                    line.append(lieu_vote)
                    line.append(office)
                    line.append(parrain)
                    line = list(filter(None, line))
                    line.insert(0, '')
                    line.insert(5, cni)
                    line.insert(6, date_exp)
                    line.insert(7, phone)
                    content.append(line)
                    name_centre.add(lieu_vote)

                    data_head.clear()
        
        # Centre par commune
        for elt in name_centre:
            centre = list()
            centre.insert(0, '')
            centre.append(elt)
            centre.append(id_commune)
            centres.append(centre)

        with open("centres.csv", 'a+', newline="", encoding="utf-8", errors="replace") as f_centre:
            csv_writer = csv.writer(f_centre)
            for ce in centres:
                csv_writer.writerow(ce)

        # electeurs par commune
        csv_name = str(path).split('\\')[-1]
        with open(csv_name, 'w', newline="", encoding="utf-8", errors="replace") as csv_file:
            # creating a csv writer object
            csv_writer = csv.writer(csv_file)

            # ecrire les en-tetes (fields)
            csv_writer.writerow(header)

            # remplir les colonnes (rows)
            for elector in content:
                csv_writer.writerow(elector) 


        # Communes
        with open("communes.csv", 'a+', newline="", encoding="utf-8", errors="replace") as file_com:
            csv_writer = csv.writer(file_com)
            csv_writer.writerow(commune)
            # for item in communes_tab:
            #     csv_writer.writerow(item)

        # Electeurs
        with open("electeurs.csv", 'a+', newline="", encoding="utf-8", errors="replace") as file_e:
            csv_writer = csv.writer(file_e)
            for elector in content:
                csv_writer.writerow(elector)

        commune.clear()
        content.clear()
        centres.clear()
        name_centre.clear()

        id_commune += 1
            
    except EnvironmentError as e:
        print("Impossible d'ouvrir le fichier. [", e, "]")

file = open("idcommnune.txt", 'w')
file.write(">> " +str(id_commune)+ " <<")
file.close()