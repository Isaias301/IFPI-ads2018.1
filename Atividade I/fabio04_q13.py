def main():
    soma_salario_atual = 0
    soma_salario_reajuste = 0
    while True:
        salario = float(input())
        if salario == 0:
            break
        soma_salario_atual += salario
        soma_salario_reajuste += calcular_novo_salario(salario)
    print("Soma dos salarios atual: {}\nSoma dos salarios reajustado: {}".format(soma_salario_atual, soma_salario_reajuste))


def calcular_novo_salario(salario):
    if salario > 0 and salario <= 2999.99:
        return ((25/100)*salario) + salario
    elif salario >= 3000 and salario <= 5999.99:
        return ((20/100) * salario) + salario
    elif salario >= 6000 and salario <= 9999.99:
        return ((15/100) * salario) + salario
    elif salario > 10.000:
        return ((10 / 100) * salario) + salario


if __name__ == '__main__':
    main()