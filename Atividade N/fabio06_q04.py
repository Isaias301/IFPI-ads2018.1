def main():
    frase = input()
    nova_frase = ""
    for palavra in frase:
        nova_frase += (palavra * 2)

    print(nova_frase)


if __name__ == '__main__':
    main()