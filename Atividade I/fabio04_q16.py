def main():
    imprestimo = float(input())
    parcela = 200
    cont = 1
    while parcela != imprestimo:
        parcela += 200
        cont += 1
    print(cont)


if __name__ == '__main__':
    main()
