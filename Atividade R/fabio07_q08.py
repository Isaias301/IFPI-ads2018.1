def main():
    vetor = input().split()
    print("Maior: %i " % int(maior(vetor)))
    print("Menor: %i " % int(menor(vetor)))


def maior(vetor):
    r = 0
    for i in range(len(vetor)):
        for j in range(len(vetor)):
            if int(r) > int(vetor[j]):
                r = r
            else:
                r = vetor[j]
    return r


def menor(vetor):
    r = maior(vetor)
    for i in range(len(vetor)):
        for j in range(len(vetor)):
            if int(r) < int(vetor[j]):
                r = r
            else:
                r = vetor[j]
    return r


if __name__ == '__main__':
    main()
