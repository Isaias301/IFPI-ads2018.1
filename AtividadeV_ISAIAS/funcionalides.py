"""
Escreva suas funções aqui:
 - Tanto funcoes para funcionalidades do Menu;
 - Quanto funções auxiliares a estas.
"""


# ##### FUNCIONALIDADES MENU #####

def total_jogos(jogos):
    print(cabecalho('Total de Jogos'), "Jogos FIFA: {}".format(len(jogos)))


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** FIFA 1930 -- 2014 *****\n'
            ' >> {} <<\n'.format(titulo))


# Imprimir total de partidas
def imprimir_total_de_partidas(jogos):
    cont = 0
    for i in range(len(jogos)):
        cont += 1
    print("Total de partidas {}".format(cont))


# Imprimir total de partidas pythonico
def imprimir_tota_de_partidas_pythonico(jogos): return len(jogos)


# 4. Crie uma funções para Exibir de forma mais amigável os jogos
def exibir_jogos(jogos):
    for i in range(len(jogos)):
        print(jogos[i][3:])


# def exibir_jogos_pythonico(jogos):
#     [print(jogos[i][3:]) for i in range(len(jogos))]


# b. Listar todos os jogos de uma seleção Específica. (Busca por nome Exato)
def jogos_selecao_especifica(jogos, selecao, selecao_casa_ou_fora):
    cont = 0
    for i in range(len(jogos)):
        if selecao_casa_ou_fora == "casa":
            if jogos[i][5] == selecao:
                print(jogos[i])
                cont += 1
        elif selecao_casa_ou_fora == "fora":
            if jogos[i][8] == selecao:
                print(jogos[i])
                cont += 1
    print("Total: {}".format(cont))


# c. Listar todos os jogos por parte do nome de um dos time ordenados ano (desc.)
def jogos_por_parte(jogos, time):
    # 5, 8
    cont = 0
    for i in range(len(jogos)):
        if time in jogos[i][5] or time in jogos[i][8]:
            print(sorted(jogos[i][5:], key=ordenar, reverse=False))
            cont += 1
    print("Total: {}".format(cont))


# numero da ordenação
def ordenar(jogos):
    return jogos[0]


# numero da ordenação
# def ordenar_pythonico(jogos): return jogos[0]


# d. Listar todos os Jogos de Final de Copa do Mundo
def todos_jogos_final_copa_do_mundo(jogos):
    contador = 0
    for i in range(len(jogos)):
        if jogos[i][2] == "Final":
            print(jogos[i])
            contador += 1
    print("Total: {}".format(contador))


# e. Listar Jogos por Placar
def jogos_por_placar(jogos, placar):
    # 6, 7
    placar_em_lista = placar.split("x")
    contador = 0
    for i in range(len(jogos)):
        if jogos[i][6] == int(placar_em_lista[0]) and jogos[i][7] == int(placar_em_lista[1]) or jogos[i][6] == int(placar_em_lista[1]) and jogos[i][7] == int(placar_em_lista[0]):
            print(jogos[i][4:])
            contador += 1
    if contador == 0:
        print("Placar inexistente.")


# f. Média de Gols em Finais
def media_gols_em_finais(jogos):
    soma_jogos = 0
    total_jogos = 0
    for i in range(len(jogos)):
        if jogos[i][2] == "Final":
            soma_jogos += jogos[i][6] + jogos[i][7]
            total_jogos += 1
    media = soma_jogos/total_jogos
    print("Media de gols em finais: %.1f" % media)


# g. Média de Gols dado um Ano de Copa do Mundo
def media_gols_dado_ano_copa_do_mundo(jogos, ano):
    soma_jogos = 0
    total_jogos = 0
    for i in range(len(jogos)):
        if int(jogos[i][0]) == int(ano):
            soma_jogos += jogos[i][6] + jogos[i][7]
            total_jogos += 1
    media = soma_jogos/total_jogos
    print("Media de gols na copa de %s: %.1f" % (ano, media))
