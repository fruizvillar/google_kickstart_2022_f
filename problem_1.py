
def test():
    # Read integers N and M from the standard input.
    n_fabrics = int(input())

    fabrics = []
    for _ in range(n_fabrics):
        c, d, u = input().split()
        fabrics.append([c, int(d), int(u)])

    f_az = list(sorted(fabrics, key=lambda x: (x[0], x[2])))
    f_19 = list(sorted(fabrics, key=lambda x: (x[1], x[2])))

    c = sum([f_az[i][2] == f_19[i][2] for i in range(n_fabrics)])
    print(c)


def main():
    t = int(input())
    # Loop over the number of test cases.
    for test_no in range(1, t + 1):
        # Print case number
        print("Case #%d:" % test_no, end=" ")
        # and solve each test.
        test()


if __name__ == '__main__':
    main()
