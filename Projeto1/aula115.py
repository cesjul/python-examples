from pathlib import Path
import csv

PATH_CSV = Path(__file__).parent / 'aula115.csv'

with open(PATH_CSV, 'r', encoding= 'utf-8') as file:
    reader = csv.DictReader(file)

    for line in reader:
        print(line['Endereco'])