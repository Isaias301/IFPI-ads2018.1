"""
    Funções relacionadas a importação de dados e eventuais tratamentos e conversões.
"""


def importar(arquivo='Partidas_CopaMundo_1930_2014.csv'):
    """
    https://stackoverflow.com/questions/19699367/unicodedecodeerror-utf-8-codec-cant-decode-byte

    Depois, Pref > File Encoding > "Add file e select" ISO-8859-1

    """
    fin = open(arquivo, encoding="ISO-8859-1")

    jogos = []
    fin.readline()  # titulos das colunas
    for linha in fin.readlines()[:829]:
        jogos.append(linha)

    return converter_quantidade_gols_para_inteiro(quebar_linha_no_split(jogos))


# Quebra cada linhas no ;
def quebar_linha_no_split(jogo):
    jogos = []
    for i in range(len(jogo)):
        jogos.append(jogo[i].split(";"))
    return jogos


# converte a quantidade de gols de cada seleção para int. colunas 6, 7 da planilha
def converter_quantidade_gols_para_inteiro(jogos):
    for i in range(len(jogos)):
        jogos[i][6] = int(jogos[i][6])
        jogos[i][7] = int(jogos[i][7])

    return total_gols(jogos)


def total_gols(jogos):
    for i in range(len(jogos)):
        somatorio_gols = jogos[i][6] + jogos[i][7]
        jogos[i].append(somatorio_gols)

        # verifica quem foi o vencedor ou se deu empate
        resultado_partida = ""
        if jogos[i][6] > jogos[i][7]:
            resultado_partida = "VENCEDOR_CASA"
        elif jogos[i][6] < jogos[i][7]:
            resultado_partida = "VENCEDOR_FORA"
        else:
            resultado_partida = "EMPATE"

        # adiciona novas colunas na matriz
        jogos[i].append(jogos[i][6] + jogos[i][7])
        jogos[i].append(resultado_partida)
    return jogos
