#Exercício 3

#tabela de tradução
tabela_de_traducao = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

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

# Complemento reverso do primeiro quadro, ou 4º quadro
dic_4_quadro = dic.copy()
for nome in dic_4_quadro:
    base = dic_4_quadro[nome]
    base = base.translate(str.maketrans("ATCG", "TAGC"))
    base = base[::-1]
    nova_base = " ".join(base[i:i+3] for i in range(0, len(base), 3))
    dic_4_quadro[nome] = nova_base

# Complemento reverso do segundo quadro, ou 5º quadro
dic_5_quadro = dic.copy()
for nome in dic_5_quadro:
    base = dic_5_quadro[nome]
    base = base.translate(str.maketrans("ATCG", "TAGC"))
    base = base[::-1]
    base = base[1:]
    nova_base = " ".join(base[i:i+3] for i in range(0, len(base), 3))
    dic_5_quadro[nome] = nova_base

# Complemento reverso do terceiro quadro, ou 6º quadro
dic_6_quadro = dic.copy()
for nome in dic_6_quadro:
    base = dic_6_quadro[nome]
    base = base.translate(str.maketrans("ATCG", "TAGC"))
    base = base[::-1]
    base = base[2:]
    nova_base = " ".join(base[i:i+3] for i in range(0, len(base), 3))
    dic_6_quadro[nome] = nova_base


# Traduzindo os seis quadros
quadros = [dic_1_quadro, dic_2_quadro, dic_3_quadro, dic_4_quadro, dic_5_quadro, dic_6_quadro]

quadros_aa = []

for quadro in quadros:
    dic_aa = {}
    for nome in quadro:
        proteina = ""
        for codon in quadro[nome].split():
            if len(codon) == 3:
                proteina = proteina + tabela_de_traducao[codon]
        dic_aa[nome] = proteina
    quadros_aa.append(dic_aa)

#Criando o arquivo de saída
with open("Python_08.translated.aa", "w") as saida:
    for nome in dic:
        saida.write(nome + "(Quadro1)" + " " + "traduzido" + "\n" + quadros_aa[0][nome] + "\n")
        saida.write(nome + "(Quadro2)" + " " + "traduzido" + "\n" + quadros_aa[1][nome] + "\n")
        saida.write(nome + "(Quadro3)" + " " + "traduzido" + "\n" + quadros_aa[2][nome] + "\n")
        saida.write(nome + "(Quadro4)" + " " + "traduzido" + "\n" + quadros_aa[3][nome] + "\n")
        saida.write(nome + "(Quadro5)" + " " + "traduzido" + "\n" + quadros_aa[4][nome] + "\n")
        saida.write(nome + "(Quadro6)" + " " + "traduzido" + "\n" + quadros_aa[5][nome] + "\n")