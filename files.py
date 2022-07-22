
# Abrindo arquivos/ Opening files
with open("meu_arquivo.txt") as file:
    contents = file.read()
    print(contents)

# Abrindo arquivos  escrevendo no final
with open("meu_arquivo.txt", mode="a") as file:
    file.write("\nlinha 2")

# Criando/abrindo arquivo e sobrescrevendo
with open("criar_arquivo.txt", mode="w") as file:
    file.write("\nlinha q")

# Paths
# !!Colocar o nome da pasta para qual "subiu"
with open("../../arquivos_auxiliares/estudo_path_py.txt") as file:
    contents = file.read()
    print(contents)

<<<<<<< HEAD
# Sobe até pasta-mãe comum. main está em day24_Mail_Merge_Project
with open("./Input/Letters/starting_letter.txt", "r") as fl_latter:
    txt_latter = fl_latter.read()
    print(txt_latter)
# OU
with open("../day24_Mail_Merge_Project/Input/Letters/starting_letter.txt", "r") as fl_latter:
    txt_latter = fl_latter.read()
    print(txt_latter)


# Return all lines in the file, as a list where each line is an item in the list object:
# Ref: https://www.w3schools.com/python/ref_file_readlines.asp
f = open("demofile.txt", "r")
print(f.readlines())
=======
#CSV
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != 'temp':
            temperature.append(int(row[1]))
    print(temperature)
>>>>>>> 1f2319503a7e9e24e7712dd11344757096554ff6
