
def selection_sort(list):
    sorted_list = []

    while len(list) > 0:
        min = list[0]
        minIndex = 0

        for index in range(0, len(list)):
            num = list[index]
            if num < min:
                min = num
                minIndex = index

        list.pop(minIndex)
        sorted_list.append(min)

    return sorted_list


print(selection_sort([5, 5, 9, 6, 2, 1, 8]))
