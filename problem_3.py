class Seed:
    N = 0

    def __init__(self, d, q, mature_l, v):
        self.q = q
        self.mature_l = mature_l
        self.v = v
        self.deadline = d - mature_l


def test():
    # Read integers N and M from the standard input.
    (d, n, x) = tuple(map(int, input().split()))

    seeds = [Seed(d, *map(int, input().split())) for _ in range(n)]
    s_seeds = sorted(seeds, key=lambda s: s.v, reverse=True)

    harvest = 0
    for day in range(d, 0, -1):
        x_day = x
        non_dying_seeds_avail = [s for s in s_seeds if (day <= s.deadline) and s.q]
        if not non_dying_seeds_avail:
            #print(f'Day {day}: Cannot plant anything')
            continue
        for s in non_dying_seeds_avail:
            n_s = min(s.q, x_day)
            s.q -= n_s
            x_day -= n_s

            harvest += n_s * s.v

            if not s.q:
                s_seeds.remove(s)

            if not x_day:
                break

        if not any(s.q for s in s_seeds):
            #print('No more seeds')
            pass#break

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
