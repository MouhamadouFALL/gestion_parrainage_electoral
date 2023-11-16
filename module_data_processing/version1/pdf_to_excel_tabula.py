# -*- coding: utf-8 -*-
import tabula
import pandas as pd


name_file = input("Entrer le nom du fichier: ")

pdf_file = name_file + ".pdf"
out_file = name_file + ".csv"
format_file = "csv"
nb_pages = 'all'

tabula.convert_into(pdf_file, out_file, output_format=format_file, stream=True, lattice=True, pages=nb_pages)








