def bubble_sort(list_to_sort):
    # Run through the array
    # the -1 is for array indexing since indices start at 0
    for i in range(0, len(list_to_sort) - 1):
        # Run through the array again
        #  -1 again for indexing
        # and -i to exclude the current item since it's already well-placed
        for j in range(0, len(list_to_sort) - 1 - i):
            # perform the swap of the item at the current position is greater than the next item
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
    return list_to_sort


if __name__ == "__main__":
    # Replace the print with your own list
    print(bubble_sort([5, 7, 3, 2, 1, 9, 0]))
