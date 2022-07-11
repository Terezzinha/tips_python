
# Abrindo arquivos/ Opening files
with open("meu_arquivo.txt") as file:
    contents = file.read()
    print(contents)

# Abrindo arquivos  escrevendo no final
with open("meu_arquivo.txt", mode="a") as file:
    file.write("\nlinha 2")

# Abrindo arquivo e sobrescrevendo
with open("criar_arquivo.txt", mode="w") as file:
  file.write("\nlinha q")

#Paths
with open("../../arquivos_auxiliares/estudo_path_py.txt") as file:
    contents = file.read()
    print(contents)

#CSV
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != 'temp':
            temperature.append(int(row[1]))
    print(temperature)
