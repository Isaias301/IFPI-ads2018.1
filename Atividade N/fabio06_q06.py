def main():
    frase = input()
    frase_nova = ""
    numeros = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    num = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    for indice in range(len(frase)):
        valor = ord(frase[indice])
        if valor >= 48 and valor <= 57:
            for i in range(len(num)):
                if valor == num[i]:
                    frase_nova += ' ' + numeros[i]
                else:
                    frase_nova += frase[indice]
    print(frase_nova)


if __name__ == '__main__':
    main()