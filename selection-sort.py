def selection_sort(list_to_sort):
    for i in range(0, len(list_to_sort) - 1):
        index_of_min_value = i
        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[j] < list_to_sort[index_of_min_value]:
                index_of_min_value = j
        if index_of_min_value != i:
            list_to_sort[i], list_to_sort[index_of_min_value] = list_to_sort[index_of_min_value], list_to_sort[i]


if __name__ == "__main__":
    print(selection_sort([9,6,2]))
