class Seed:
    N = 0

    def __init__(self, q, mature_l, v):
        self.n = self.N + 1
        self.q = q
        self.mature_l = mature_l
        self.v = v

        Seed.N = self.n

    def __repr__(self):
        return f'{self.n}: q={self.q}, ml={self.mature_l}, v={self.v}'


def test():
    # Read integers N and M from the standard input.
    (d, n, x) = tuple(map(int, input().split()))

    seeds = [Seed(*map(int, input().split())) for _ in range(n)]
    s_seeds = sorted(seeds, key=lambda s: (s.v, -s.mature_l), reverse=True)

    harvest = 0
    for day in range(1, d + 1):
        x_day = x

        non_dying_seeds_avail = [s for s in s_seeds if (day + s.mature_l <= d) and s.q]

        non_dying_seeds_avail_sorted_expiry = sorted(non_dying_seeds_avail, key=lambda s: d - day - s.mature_l != 0)
        for s in non_dying_seeds_avail_sorted_expiry:
            n_s = min(s.q, x_day)
            s.q -= n_s
            x_day -= n_s
            # print(f'{day=}. Planted {n_s} of {s.n=} {s.v=} ({s.mature_l=}). Value={n_s*s.v=}')
            harvest += n_s * s.v
            if not x_day:
                break

    print(harvest)


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
