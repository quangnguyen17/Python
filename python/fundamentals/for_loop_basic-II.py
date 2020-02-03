
# 1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".


def biggie_size(list):
    for i in range(0, len(list)):
        list[i] = "big" if list[i] > 0 else list[i]

    return list


# print(biggie_size([-1, 3, 5, -5]))

# 2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
def count_positives(list):
    positives = 0

    for i in range(0, len(list)):
        if list[i] > 0:
            positives += 1

    list[len(list) - 1] = positives
    return list


# print(count_positives([-1, 1, 1, 1]))
# print(count_positives([1, 6, -4, -2, -7, -2]))

# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
def sum_total(list):
    sum = list[0]

    for i in range(1, len(list)):
        sum += list[i]

    return sum


# print(sum_total([1, 2, 3, 4]))
# print(sum_total([6, 3, -2]))

# 4. Average - Create a function that takes a list and returns the average of all the values.
def average(list):
    sum = list[0]
    count = 1

    for i in range(1, len(list)):
        sum += list[i]
        count += 1

    return sum / count


# print(average([1, 2, 3, 4]))

# 5. Length - Create a function that takes a list and returns the length of the list.
def length(list):
    length = 0

    for i in range(0, len(list)):
        length += 1

    return length


# print(length([37, 2, 1, -9]))
# print(length([]))

# 6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(list):
    if len(list) < 1:
        return False

    min = list[0]
    for i in range(1, len(list)):
        if list[i] < min:
            min = list[i]

    return min


# print(minimum([37, 2, 1, -9]))
# print(minimum([]))

# 7. Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
def maximum(list):
    if len(list) < 1:
        return False

    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]

    return max


# print(maximum([37, 2, 1, -9]))
# print(maximum([]))

# 8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(list):
    return {"sumTotal": sum_total(list), "average": average(list), "minimum": minimum(list), "maximum": maximum(list), "length": len(list)}


# print(ultimate_analysis([37, 2, 1, -9]))

# 9. Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
def reverse_list(list):
    for i in range(0, int(len(list) / 2)):
        list[i], list[len(list) - i - 1] = list[len(list) - i - 1], list[i]

    return list


print(reverse_list([37, 2, 1, -9]))
