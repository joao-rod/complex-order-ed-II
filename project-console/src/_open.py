import csv

# Abre o arquivo csv e salva os dados do arquivo em um array
def open_file(filename):
	dados = []
	with open(f'./files/{filename}.csv', 'r') as csv_file:
		file = csv.reader(csv_file, delimiter=";")
		for row in file:
			dados.append(row)
   
	return dados
