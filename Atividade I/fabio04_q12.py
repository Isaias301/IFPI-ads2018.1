def main():
    cont1 = 0
    cont2 = 0
    while True:
        jogador1 = int(input())
        cont1 += jogador1
        if cont1 == 21 and cont1 % cont2 >= 2:
            break
        elif cont1 > 21 and cont1 % cont2 > 2:
            break
        jogador2 = int(input())
        cont2 += jogador2
        if cont2 == 21 and cont2 % cont1 >= 2:
            break
        elif cont2 > 21 and cont2 % cont1 > 2:
            break
    print(cont1)
    print(cont2)


if __name__ == '__main__':
    main()