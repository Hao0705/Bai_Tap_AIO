def insertion_sort(my_list):

    length = len(my_list)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if my_list[j] < my_list[j-1]:
                my_list[j], my_list[j-1] = my_list[j-1], my_list[j]

    return my_list

my_list = [10, 0, 2, 7, 5, 8]
my_list = insertion_sort(my_list)
print(my_list)
