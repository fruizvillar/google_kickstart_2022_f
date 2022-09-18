from typing import Any, List


class TestSuite:

    def __init__(self):
        self.t = int(input())

    @staticmethod
    def _read_integers() -> List[int]:
        return list(map(int, input().split()))

    def _solve(self) -> Any:
        raise NotImplementedError('Implement this as subclass')

    def __call__(self):
        for test_no in range(1, self.t + 1):
            # Print case number
            print("Case #%d:" % test_no, end=" ")
            # and solve each test.
            print(self._solve())

