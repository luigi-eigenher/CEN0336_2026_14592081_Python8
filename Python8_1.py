# Exercício 1

# Criando a estrutura de dados
dic = {}

# Lendo arquivo .txt
with open("fasta.txt", "r") as info:
    for linha in info:
        linha = linha.rstrip()

        if linha[0] == ">": #extraindo as infos da sequência
            nome, tamanho, cord = linha.split(" ", 2)
            cont = {"A": 0, "C": 0, "T": 0, "G": 0}

        else:
            cont["A"] += linha.count("A")
            cont["C"] += linha.count("C")
            cont["T"] += linha.count("T")
            cont["G"] += linha.count("G")

            dic[nome] = [tamanho, cord, cont]

#imprimindo as informações
print("Nome", "A", "C", "T", "G", sep="\t")

for nome in dic:
    print(nome, dic[nome][2]["A"], dic[nome][2]["C"],
          dic[nome][2]["T"], dic[nome][2]["G"], sep="\t")