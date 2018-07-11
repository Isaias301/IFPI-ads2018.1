def main():
    frase = input().split()
    nova_frase = ""
    for palavra in frase:
        nova_frase += palavra

    print(nova_frase)


if __name__ == '__main__':
    main()