#Exercício 2

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

#dividindo a sequência em códons
for nome in dic:
    nova_base = " ".join(dic[nome][i:i+3] for i in range(0, len(dic[nome]), 3))
    dic[nome] = nova_base

#escrevendo o novo arquivo de saída
with open("Python_08.codons-frame-1.nt", "w") as saida:
    for nome in dic:
        saida.write(nome + " " + "codons" + "\n" + dic[nome] + "\n")

