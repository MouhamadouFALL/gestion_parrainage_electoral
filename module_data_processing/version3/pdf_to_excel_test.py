# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract
import csv
from pdf2image import convert_from_path


name_file = input("Entrer le nom du fichier: ")
pdf_file_path = name_file + ".PDF"

# Fonction pour extraire le texte d'une image en utilisant Pytesseract
def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang='eng')  # Utilisez 'eng' pour l'anglais, remplacez-le si nécessaire.
    return text

# Convertir chaque page du PDF en texte et le stocker dans une liste
text_pages = []
images = convert_from_path(pdf_file_path)

for page in images:
    text = extract_text_from_image(page)
    text_pages.append(text)

# Exporter le texte en CSV
csv_output_path = "file_out.csv"

with open(csv_output_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for text in text_pages:
        writer.writerow([text])

print("Extraction de texte terminée. Les données ont été exportées en CSV.")
