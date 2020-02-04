
# Assignment: MathDojo + TDD

import unittest


class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num

        for arg in nums:
            self.result += arg

        return self

    def subtract(self, num, *nums):
        self.result -= num

        for arg in nums:
            self.result -= arg

        return self


# math_dojo = MathDojo()
# to test:
# x = math_dojo.add(2).add(2, 5, 1).subtract(3, 2).result
# print(x)  # should print 5
# run each of the methods a few more times and check the result!


class MathDojoTest(unittest.TestCase):
    def test_add(self):
        math_dojo_add_test = MathDojo()

        math_dojo_add_test.add(2, 3)
        self.assertEqual(math_dojo_add_test.result, 5)

        math_dojo_add_test.add(3, 3)
        self.assertEqual(math_dojo_add_test.result, 11)

    def test_subtract(self):
        math_dojo_subtract_test = MathDojo()
        math_dojo_subtract_test.add(10)

        math_dojo_subtract_test.subtract(2, 3)
        self.assertEqual(math_dojo_subtract_test.result, 5)

        math_dojo_subtract_test.subtract(5)
        self.assertEqual(math_dojo_subtract_test.result, 0)

    def setUp(self):
        print("running setUp")

    def tearDown(self):
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main()  # this runs our tests
