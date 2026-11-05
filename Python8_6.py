
# Criando lista para estrutura de dados
peptideos = []

# Lendo as informações do arquivo gerado
with open("Python_08.translated.aa", "r") as info:
    for linha in info:
        linha = linha.rstrip()

        if linha[0] == ">":  # Separando as informações de cada tradução
            nome, nada = linha.split()
            quadro = nome.split("(Quadro")
            registro = quadro[0]
            numero_quadro = quadro[1].replace(")", "")

        else:  # Iniciando busca pelos peptídeos
            proteina = linha
            inicio = 0

            while inicio < len(proteina):
                inicio_m = proteina.find("M", inicio)

                if inicio_m == -1:
                    break

                fim = proteina.find("*", inicio_m)

                if fim == -1:
                    break

                peptideo = proteina[inicio_m:fim]

                peptideos.append((peptideo, registro, numero_quadro))

                inicio = inicio_m + 1


# Criando o arquivo com os maiores peptídeos
with open("Python_08.translated-longest.aa", "w") as saida:
    registros = []

    for peptideo, registro, numero_quadro in peptideos:
        if registro not in registros:
            registros.append(registro)

    for registro in registros:
        maior = ""

        for peptideo, nome_registro, numero_quadro in peptideos:
            if nome_registro == registro:
                if len(peptideo) > len(maior):
                    maior = peptideo
                    quadro_maior = numero_quadro

        saida.write(">" + registro + "(Quadro" + quadro_maior + ") mais_longo:\n")
        saida.write(maior + "\n")
