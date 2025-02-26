from pathlib import Path
import csv

PATH_CSV = Path(__file__).parent / 'aula116.csv'

costumers_list = [
    {'Name': 'John Smith', 'Address':'507th, Backer Street'},
    {'Name': 'Antony Harlow', 'Address': '1156th, 5th Avenue'},
    {'Name': 'George MacDonell', 'Address': '154th, Marina Drive'},
]


# with open(PATH_CSV, 'w', encoding='utf-8') as file:
#     columns = costumers_list[0].keys()
#     writer = csv.writer(file, lineterminator='\r')
#     writer.writerow(columns)

#     for costumers in costumers_list:
#         writer.writerow(costumers.values())

with open(PATH_CSV, 'w', encoding='utf-8') as arquivo:
    columns = costumers_list[0].keys()
    writer = csv.DictWriter(
        arquivo, fieldnames= columns,
        lineterminator = '\r' # sem kwarg, o codigo pula duas linhas
    )
    writer.writeheader()
    for costumers in costumers_list:
        writer.writerow(costumers)