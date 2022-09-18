class Meeting:

    def __init__(self, p, l, r):
        self.p = p
        self.l = l
        self.r = r

    def __repr__(self):
        return f'[TL {self.p}. From {self.l} to {self.r}]'


def test(test_no):
    # Read integers N and M from the standard input.
    (n, k, x, d) = tuple(map(int, input().split()))
    if test_no == 5:
        print(f'N TL: {n}. Quorum={k}. D={x}. TotalT={d}')
    m = int(input())
    # Read N integers from the standard input and save them in the list `C`.
    meetings = []

    for _ in range(m):
        meetings.append(Meeting(*map(int, input().split())))

    if test_no == 5:
        print(*meetings)
    at_most_n_busy = n - k

    to_persuade = n
    to_cancel = m
    for di in range(d - x+1):

        busy = set([m.p for m in meetings if m.r > di and m.l < di + x])
        n_busy = len(busy)
        to_persuade = n_busy - at_most_n_busy

        if to_persuade <= 0:
            print(0)
            return

        overlapping = [m for m in meetings if m.r > di and m.l < di + x]

        to_cancel_per_tl = {b: len([m for m in overlapping if m.p == b]) for b in busy}

        to_cancel_this = sum(sorted(to_cancel_per_tl.values())[:to_persuade])

        if test_no == 5:
            print(f'\tHour {di} to {di + x} {to_cancel_this=}')
            print(f'{n_busy=}')
            print(f'{to_persuade=}')

        to_cancel = min(to_cancel, to_cancel_this)

    print(to_cancel)

    if test_no == 5:
        exit(1)

def main():
    t = int(input())
    # Loop over the number of test cases.
    for test_no in range(1, t + 1):
        # Print case number
        print("Case #%d:" % test_no, end=" ")
        # and solve each test.
        test(test_no)


if __name__ == '__main__':
    main()
