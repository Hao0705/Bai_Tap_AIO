def selection_sort(my_list):

    length = len(my_list)

    for i in range(length):
        min_value = my_list[i]
        index = i

        for j in range(i, length):
            if min_value > my_list[j]:
                min_value = my_list[j]
                index = j

        if index != i:
            my_list[i], my_list[index] = my_list[index], my_list[i]

    return my_list

my_list = [10, 0 , 9 , 11, 5, 7, 4]
my_list = selection_sort(my_list)
print(my_list)
