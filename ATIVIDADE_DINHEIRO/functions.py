# lista de veiculos global
veiculos = []


# cadastrar novo veiculo
def novo_veiculo(placa, nome, marca, ano, valor):
    veiculos.append({"placa": placa, "nome": nome, "marca": marca, "ano": ano, "valor": valor})
    return veiculos


# listar veiculos por condicao
def lista_veiculos_por(por):
    if len(veiculos) == 0:
        print("Você não tem veiculos cadastrado")
    else:
        for i in range(len(veiculos)):
            print(veiculos[i][por])


# exibir veiculo por placa
def exibir_veiculo_por_placa(placa):
    if len(veiculos) == 0:
        print("Você não tem veiculos cadastrado")
    else:
        for i in range(len(veiculos)):
            if veiculos[i]["placa"] == placa:
                print(veiculos[i])


# filtrar veiculos por condicao
def filtrar_veiculos_por(por, condicao, valor):
    if len(veiculos) == 0:
        print("Você não tem veiculos cadastrado")
    else:
        for i in range(len(veiculos)):
            if condicao == 1:
                if veiculos[i][por] == valor:
                    print(veiculos[i])
            elif condicao == 2:
                if veiculos[i][por] < valor:
                    print(veiculos[i])
            elif condicao == 3:
                if veiculos[i][por] > valor:
                    print(veiculos[i])
            else:
                print("Condição inválida.")


# buscar veiculo por parte do nome
def buscar_por_parte_do_nome(parte_nome):
    if len(veiculos) == 0:
        print("Você não tem veiculos cadastrado")
    else:
        for i in range(len(veiculos)):
            if parte_nome in veiculos[i]["nome"]:
                print(veiculos[i])
