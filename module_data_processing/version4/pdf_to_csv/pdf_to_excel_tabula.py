# -*- coding: utf-8 -*-
import tabula
import sys
import pathlib



format_file = "csv"
nb_pages = 'all'

try:
    path_dir = pathlib.Path(sys.argv[1]) # convertir un argument en chemin 
except IndexError:
    sys.exit("Vous devez passer en paraametre un chemin vers un fichier Historique.")


directory = pathlib.Path(str(path_dir))
for path in directory.iterdir():
    name_file = str(path).split('\\')[-1].replace('.PDF', '')
    out_file = name_file + ".csv"
    tabula.convert_into(path, out_file, output_format=format_file, stream=True, lattice=True, pages=nb_pages)






