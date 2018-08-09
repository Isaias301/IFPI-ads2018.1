from importacao import *
from funcionalides import *
import os


def main():
    # importar o arquivo
    jogos = importar()

    menu = '***** FIFA 1930 -- 2014 *****\n' \
           '1 - Quantidade de Jogos\n' \
           '2 - Exibir jogos de forma amigavel\n' \
           '3 - Imprimir total de partidas\n' \
           '4 - Jogos por seleção\n' \
           '5 - Listar todos os Jogos de Final de Copa do Mundo\n' \
           '6 - Listar Jogos por Placar\n' \
           '7 - Média de Gols em Finais\n' \
           '8 - Média de Gols dado um Ano de Copa do Mundo\n' \
           '9 - Listar todos os jogos por parte do nome de um dos time ordenados ano (desc.)\n' \
           '0 - Sair\n'

    opcao = int(input(menu))

    # loop do Menu de opcões
    while opcao != 0:
        if opcao == 1:
            total_jogos(jogos)
        elif opcao == 2:
            exibir_jogos(jogos)
        elif opcao == 3:
            imprimir_total_de_partidas(jogos)
        elif opcao == 4:
            selecao_casa_ou_fora = input("Selecao de casa ou fora? ")
            selecao = input("Digite a selecao desejada: ")
            jogos_selecao_especifica(jogos, selecao, selecao_casa_ou_fora)
        elif opcao == 5:
            todos_jogos_final_copa_do_mundo(jogos)
        elif opcao == 6:
            placar = input("Digite o placar(Ex: 3x1 ou 1x3): ")
            jogos_por_placar(jogos, placar)
        elif opcao == 7:
            media_gols_em_finais(jogos)
        elif opcao == 8:
            ano = input("Ano da copa: ")
            media_gols_dado_ano_copa_do_mundo(jogos, ano)
        elif opcao == 9:
            time = input("Nome(Ex: USA = US):")
            jogos_por_parte(jogos, time)
            print("Terminado...olhe o código")
        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('clear')  # se Windows: 'cls'

        # pedir nova opcao
        opcao = int(input(menu))


if __name__ == '__main__':
    main()
