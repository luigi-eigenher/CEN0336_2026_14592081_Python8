#Exercício 3

#Estrutura de dados
dic = {}

# Lendo arquivo .txt
with open("fasta.txt", "r") as info:
    for linha in info:
        linha = linha.rstrip()

        if linha[0] == ">": #extraindo as infos da sequência:
                nome, tamanho, cord = linha.split(" ", 2)
                base = "" #definindo a string que será dividida

        else:
            base = base + linha 
            dic[nome] = base #adcionando ao dicionário a string que será dividida

#dividindo a sequência em códons, primeiro quadro
dic_1_quadro = dic.copy()
for nome in dic_1_quadro:
    nova_base = " ".join(dic_1_quadro[nome][i:i+3] for i in range(0, len(dic_1_quadro[nome]), 3))
    dic_1_quadro[nome] = nova_base

#dividindo a sequência em códons, segundo quadro
dic_2_quadro = dic.copy()
for nome in dic_2_quadro:
    dic_2_quadro[nome] = dic_2_quadro[nome][1:]
    nova_base = " ".join(dic_2_quadro[nome][i:i+3] for i in range(0, len(dic_2_quadro[nome]), 3))
    dic_2_quadro[nome] = nova_base

#dividindo a sequência em códons, terceiro quadro
dic_3_quadro = dic.copy()
for nome in dic_3_quadro:
    dic_3_quadro[nome] = dic_3_quadro[nome][2:]
    nova_base = " ".join(dic_3_quadro[nome][i:i+3] for i in range(0, len(dic_3_quadro[nome]), 3))
    dic_3_quadro[nome] = nova_base

#Criando o arquivo de saída
with open("Python_08.codons-3frames.nt", "w") as saida:
    for nome in dic:
        saida.write(nome + "(Quadro1)" + " " + "codons" + "\n" + dic_1_quadro[nome] + "\n")
        saida.write(nome + "(Quadro2)" + " " +  "codons" + "\n" + dic_2_quadro[nome] + "\n")
        saida.write(nome + "(Quadro3)" + " " + "codons" + "\n" + dic_3_quadro[nome] + "\n")