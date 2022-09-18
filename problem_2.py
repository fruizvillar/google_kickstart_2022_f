from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, n):
        self.n = n
        self._c_conn = None  # type: Optional[Node]
        self.level = None
        if self.n == 1:
            self.level = 1

    def pipes(self, o: 'Node'):
        self._c_conn = o
        self.refresh_level()

    def refresh_level(self):
        if self.level is not None:
            return True

        try:
            self.level = self._c_conn.level + 1

            return True
        except (TypeError, AttributeError):
            return False

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self._c_conn:
            return f'|({self.n}), l={self.level}, <-({self._c_conn.n})|'
        else:
            return f'|({self.n}), l={self.level}, <-({self._c_conn})|'


def test():
    # Read integers N (# nodes) and Q (# queries) from the standard input.
    (n, q) = tuple(map(int, input().split()))

    # Read N-1 connections
    pipes = [tuple(map(int, input().split())) for _ in range(n - 1)]

    # Read q queries
    queries = [int(input()) for _ in range(q)]

    # Creating tree
    nodes = [Node(i) for i in range(1, n + 1)]
    for n_from, n_to in pipes:
        nodes[n_from - 1].pipes(nodes[n_to - 1])
        nodes[n_to - 1].pipes(nodes[n_from - 1])

    while True:
        if all(n.refresh_level() for n in nodes):
            break

    levels = defaultdict(list)
    for n in nodes:
        levels[n.level].append(n)

    n_levels = len(levels.keys())

    filled = 0
    n_liters = len(queries)
    for level in range(1, n_levels + 1):
        n_containers_this_level = len(levels[level])

        if n_liters >= n_containers_this_level:
            n_liters -= n_containers_this_level
            filled += n_containers_this_level
        else:
            break

    print(filled)


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
