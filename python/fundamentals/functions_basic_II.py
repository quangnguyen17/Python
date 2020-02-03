
# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).


def count_down(num):
    numList = []

    for x in range(num, -1, -1):
        numList.append(x)

    return numList


# print(count_down(5))

# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.


def print_and_return(list):
    print(list[0])
    return list[1]


# print(print_and_return([1, 2]))

# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.


def first_plus_length(list):
    return list[0] + len(list)


# print(first_plus_length([1, 2, 3, 4, 5]))

# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False


def values_greater_than_second(list):
    if len(list) < 2:
        return False

    newList = []

    for i in range(0, len(list)):
        if i == len(list) - 1:
            newList.append(list[i])
        elif list[i] > list[1]:
            newList.append(list[i])

    print(len(newList))
    return newList


# print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
# print(values_greater_than_second([3]))

# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.


def length_and_value(size, value):
    list = []

    for i in range(0, size):
        list.append(value)

    return list


# print(length_and_value(4, 7))
# print(length_and_value(6, 2))
