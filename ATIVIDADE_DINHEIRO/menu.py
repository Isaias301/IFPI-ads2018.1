# packet to manipulate system
import os
from functions import *


def main():
    while True:
        menu = '***** CADASTRO DE VEICULOS *****\n' \
               '1 - Novo veiculo\n' \
               '2 - Lista veiculo por?\n' \
               '3 - Filtrar veiculo por?\n' \
               '4 - Exibier veiculo por placa\n' \
               '5 - Buscar por parte do nome\n' \
               '0 - Sair\n'

        opcao = int(input(menu))

        if opcao != 0:
            veiculos = ""
            if opcao == 1:
                placa = input("Placa: ")
                nome = input("Nome: ")
                marca = input("Marca: ")
                ano = input("Ano: ")
                valor = input("Valor: ")
                veiculos = novo_veiculo(placa, nome, marca, ano, valor)
                print(veiculos)
            elif opcao == 2:
                por = input("Listar por: ")
                lista_veiculos_por(por)
            elif opcao == 3:
                por = input("Filtrar por: ")
                condicao = int(input("1 - =\n2 - <\n3 - >\n"))
                valor = input("Valor: ")
                filtrar_veiculos_por(por, condicao, valor)
            elif opcao == 4:
                placa = input("Placa: ")
                exibir_veiculo_por_placa(placa)
            elif opcao == 5:
                parte_nome = input("Placa: ")
                buscar_por_parte_do_nome(parte_nome)
        elif opcao == 0:
            break
        else:
            print("Opção inválida")

        # limpar a tela
        input('Enter para continuar...')
        os.system('clear')



if __name__ == '__main__':
    main()
