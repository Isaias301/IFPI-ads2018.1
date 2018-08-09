# packet to manipulate system
import os


def main():
    while True:
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

        if opcao != 0:
            print("ok")
        elif opcao == 0:
            break
        else:
            print("Opção inválida")

        # limpar a tela
        input('Enter para continuar...')
        os.system('clear')



if __name__ == '__main__':
    main()
