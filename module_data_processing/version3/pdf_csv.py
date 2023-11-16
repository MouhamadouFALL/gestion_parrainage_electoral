
import csv
from pypdf import PdfReader
from pdfminer.high_level import extract_text, extract_pages


name_file = input("Entrer le nom du fichier: ")
pdf_file_path = name_file + ".PDF"

header_data = ['id', 'num electeur', 'Prénom(s)', 'Nom', 'Date Naiss', 'cni', 'date_exp', 'phone', 'Commune', 'centre', 'Bureau','Parrain',]
data = []

num_elect = None
prenom = None
nom = None
date_naiss = ""
commune = ""
centre = ""
office = None
parrain = "Non"

cni = ""
date_exp = ""
phone = ""

reader = PdfReader(pdf_file_path)
number_of_pages = len(reader.pages)
word_to_del = (":", "électeur", "Nom", "Lieu de vote", "N°", "Prénom(s)", "Bureau", "Localité")
n = 0
while n < number_of_pages:
    page = reader.pages[n]
    text = page.extract_text()
    text = text.split("\n")

    header = text[0]
    text.pop(0)
    text.pop()

    for w in word_to_del:
        header = header.replace(w, "")
    header = header.split()
    office = header[-1]
    header.pop()
    tmp = []
    for x in header:
        if x not in tmp:
            tmp.append(x)

    commune = " ".join(tmp)
    centre = commune

    for line in text:
        content = []
        line = line.split(" ")
        if len(line) > 2:
            num_elect = line[0]
            nom = line[-1]
            prenom = " ".join(line[1:-1])
        else:
            num_elect = line[0]
            prenom = line[1]
            nom = line[2]

        content.insert(0, '')
        content.append(num_elect)
        content.append(prenom)
        content.append(nom)
        content.append(date_naiss)
        content.append(cni)
        content.append(date_exp)
        content.append(phone)
        content.append(commune)
        content.append(centre)
        content.append(office)
        content.append(parrain)
        data.append(content)
    n += 1

data.pop()
csv_name = name_file + ".csv"
with open(csv_name, 'w', newline="", encoding="utf-8", errors="replace") as csv_file:
    # creating a csv writer object
    csv_writer = csv.writer(csv_file)

    # ecrire les en-tetes (fields)
    csv_writer.writerow(header_data)

    # remplir les colonnes (rows)
    for elector in data:
        csv_writer.writerow(elector)
