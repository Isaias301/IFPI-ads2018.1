def main():
    file = open('enem2014_nota_por_escola.txt')
    result = read_file(file)
    menu(result)


# funcao para ler o aquivo do senso
def read_file(file):
    senso = []
    for line in file:
        line_file = line.strip()
        senso.append(line_file.split(";"))
    return senso


# Top N Brasil (todas as áreas)
def print_senso_all(senso):
    for i in range(len(senso)):
        print(senso[i])


# Top N por Estado
def print_senso_estadual(senso, estado):
    for i in range(len(senso)):
        if senso[i][3] == estado.upper():
                print(senso[i])


# Top N por Estado e Rede(publica ou privada)
def print_senso_estadual_privado_ou_publica(senso, estado, publica_ou_privada):
    for i in range(len(senso)):
        if senso[i][3] == estado.upper() and senso[i][4] == "Privada":
                print(senso[i])


# Media Nacional por Área
def print_media_nacional_por_area(senso, area):
    media_nacional = 0
    materia = ""
    cont = 0
    for i in range(len(senso)):
        if area.lower() == "linguagens":
            media_nacional += float(senso[i][8])
            materia = "linguagens"
            cont += 1
        elif area.lower() == "matemática":
            media_nacional += float(senso[i][9])
            materia = "matemática"
            cont += 1
        elif area.lower() == "ciencias_natureza":
            media_nacional += float(senso[i][10])
            materia = "ciencias_natureza"
            cont += 1
        elif area.lower() == "humanas":
            media_nacional += float(senso[i][11])
            materia = "humanas"
            cont += 1
        elif area.lower() == "redacao":
            media_nacional += float(senso[i][12])
            materia = "redacao"
            cont += 1
    return materia, media_nacional/cont


# Melhor escola por Área e Estado ou BR
def print_melhor_escola_por_area_e_estado_ou_br(senso, opcion):
    pass


# Busca escola específica por Nome
def print_busca_escola_especifica_por_nome(senso, nome):
    for i in range(len(senso)):
        if nome in senso[i][1]:
                print(senso[i])


# function menu senso
def menu(senso):
    print("****************SENSO****************\nDigite a opção deseja:\n")
    print("1 - Senso Brasil (todas as áreas): ")
    print("2 - Senso por estados: ")
    print("3 - Senso por Estado e Rede(publica ou privada): ")
    print("4 - Media Nacional por Área(linguagens, matemática, ciencias_natureza, humanas, redacao): ")
    print("6 - Busca escola específica por Nome: \n---------------------------")

    opcion = int(input())
    if opcion == 1:
        print_senso_all(senso)
    elif opcion == 2:
        estado = input("Digite o estado(Ex: PI): ")
        print_senso_estadual(senso, estado.upper())
    elif opcion == 3:
        estado = input("Digite o estado(Ex: PI): ")
        publica_ou_privada = input("Rede publica ou privada? ")
        print_senso_estadual_privado_ou_publica(senso, estado, publica_ou_privada)
    elif opcion == 4:
        area = input("Matéria: ")
        media_nacional = print_media_nacional_por_area(senso, area)
        print("A média nascional da materia %s é %.2f" % (media_nacional[0], media_nacional[1]))
    # elif opcion == 5:
    #     pass
    elif opcion == 6:
        escola = input("Digite o nome da escola: ")
        print_busca_escola_especifica_por_nome(senso, escola)
    else:
        print("Opcão inválida")


if __name__ == '__main__':
    main()
