def main():
    frase = input()
    print("Palindroma" if frase == frase[::-1] else "Não e palindroma")


if __name__ == '__main__':
    main()