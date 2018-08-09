# lista de veiculos global
veiculos = []


# cadastrar novo veiculo
def novo_veiculo(placa, nome, marca, ano, valor):
    veiculos.append({"placa": placa, "nome": nome, "marca": marca, "ano": ano, "valor": valor})
    return veiculos


# listar veiculos
def listar_veiculos():
    if len(veiculos) == 0:
        print("Você não tem veiculo cadastrado")
    else:
        for i in range(len(veiculos)):
            print(veiculos[i])


def busca_veiculo(placa):
    if len(veiculos) == 0:
        print("Você não tem veiculo cadastrado.")
    else:
        cont = 0
        for i in range(len(veiculos)):
            if veiculos[i]["placa"] == placa:
                return veiculos[i]


# atualiza veiculo
def atulizar_veiculo(guarda_placa, opcao_campo, novo_dado):
    if len(veiculos) == 0:
        print("Você não tem veiculo cadastrado.")
    else:
        for i in range(len(veiculos)):
            # \n1 - Placa\n2 - Nome\n3 - Marca\n4 - Ano\n5 - Valor\n"
            if opcao_campo == 1:
                if veiculos[i]["placa"] == guarda_placa:
                    veiculos[i]["placa"] = novo_dado
                    print("Veiculo alterado com sucesso!\n", veiculos[i])
            elif opcao_campo == 2:
                if veiculos[i]["placa"] == guarda_placa:
                    veiculos[i]["nome"] = novo_dado
                    print("Veiculo alterado com sucesso!\n", veiculos[i])
            elif opcao_campo == 3:
                if veiculos[i]["placa"] == guarda_placa:
                    veiculos[i]["marca"] = novo_dado
                    print("Veiculo alterado com sucesso!\n", veiculos[i])
            elif opcao_campo == 4:
                if veiculos[i]["placa"] == guarda_placa:
                    veiculos[i]["ano"] = novo_dado
                    print("Veiculo alterado com sucesso!\n", veiculos[i])
            elif opcao_campo == 5:
                if veiculos[i]["placa"] == guarda_placa:
                    veiculos[i]["valor"] = novo_dado
                    print("Veiculo alterado com sucesso!\n", veiculos[i])
