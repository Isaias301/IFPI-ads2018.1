# packet to manipulate system
import os
from functions import *


def main():
    while True:
        menu = '***** CADASTRO DE VEICULOS *****\n' \
               '1 - Novo veiculo\n' \
               '2 - Lista veiculos\n' \
               '3 - Atualizar veiculo\n' \
               '4 - Deletar veiculo\n' \
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
                listar_veiculos()

            elif opcao == 3:
                placa = input("Digite a placa do veiculo que deseja alterar: ")
                guarda_placa = placa
                veiculo = busca_veiculo(placa)
                if veiculo:
                    print(veiculo,"\nVeiculo encontrado! Qual dado deseja altera:\n1 - Placa\n2 - Nome\n3 - Marca\n4 - Ano\n5 - Valor")
                    opcao_campo = input("Opcão: ")
                    novo_dado = input("Digite o novo dado: ")
                    atulizar_veiculo(guarda_placa, opcao_campo, novo_dado)
                else:
                    print("Veiculo não encontrado.")

        elif opcao == 0:
            break
        else:
            print("Opção inválida")

        # limpar a tela
        input('Enter para continuar...')
        os.system('clear')



if __name__ == '__main__':
    main()
