def main():
    vetor = []
    for i in range(20):
        vetor += [int(input())]

    a = []
    for i in range(10, len(vetor)):
        a += [vetor[i]]

    b = []
    t = len(a)-1
    while t >= 0:
        b += [a[t]]
        t -= 1

    c = []
    for i in range(10):
        c += [vetor[i]]

    s = 0
    for k in range(10):
        s += c[k] + b[k]
    print(s)
    

if __name__ == '__main__':
    main()
