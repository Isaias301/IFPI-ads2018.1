def main():
    texto = input()
    palavras = texto.split()
    print("O texto possue {} palavras".format(len(palavras)))


if __name__ == '__main__':
    main()