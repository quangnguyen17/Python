
import unittest

# 1. reverseList - Write a function that reverses the values in the list (without creating a temporary array).


def reverse_list(list):
    for i in range(int(len(list) / 2)):
        list[i], list[len(list) - 1 - i] = list[len(list) - 1 - i], list[i]

    return list


# 2. isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backward).


def is_palindrome(word):
    wordBackward = ''
    for i in range(len(word) - 1, -1, -1):
        wordBackward += word[i]

    return wordBackward == word


# 3. coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.


def coins(cents):
    remainder = cents

    quarters = int(cents / 25)
    remainder -= (quarters * 25)

    dimes = int(remainder / 10)
    remainder -= (dimes * 10)

    nickels = int(remainder / 5)
    return [quarters, dimes, nickels, remainder]


# 4. BONUS - factorial - Write a recursive function that returns the factorial of a given number. Remember that the factorial of a number is the product of all the numbers between 1 and the given number (eg. 4! = 4*3*2*1).

# def factorial(num):
#     return num if num == 1 else factorial()

# 5. BONUS - fibonacci - Write a recursive function that accepts a number, n, and returns the nth Fibonacci number from the sequence. The first two Fibonacci numbers are 0 and 1. Every number after that is calculated by adding the previous 2 numbers from the sequence. (i.e. 0, 1, 1, 2, 3, 5, 8, 13, 21 ...)


class TestingClass(unittest.TestCase):
    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 3, 5]), [5, 3, 1])
        self.assertEqual(reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_list([1, 3, 10]), [10, 3, 1])
        self.assertEqual(reverse_list([1, 3, 6]), [6, 3, 1])
        # Add at least 3 other test cases

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("racecar"), True)
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("rabcr"))
        # Add at least 5 other test cases

    def test_coins(self):
        self.assertEqual(coins(87), [3, 1, 0, 2])
        # Add at least 5 other test cases

    def setUp(self):
        print("running setUp")

    def tearDown(self):
        print("running tearDown tasks")


if __name__ == '__main__':
    # this runs our tests
    unittest.main()
