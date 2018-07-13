def main():
    import random

    r = [0]
    for i in range(23):
        r.append(random.randint(1,23))
    f = r
    for i in range(len(r)):
        print(f.count(i))


if __name__ == '__main__':
    main()
