def main():
    verbo = input()
    a = "."
    b = a.join(verbo)
    c = b.split(".")
    c.pop(len(c) - 1)
    d = ""
    print(d.join(c))


if __name__ == '__main__':
    main()