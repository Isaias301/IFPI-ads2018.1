def main():
    a = input().split()
    b = [None]*len(a)
    for i in range(len(a)):
        if int(a[i])%2 == 0:
            b[i] = 0
        else:
            b[i] = 1
    print(b)


if __name__ == '__main__':
    main()
