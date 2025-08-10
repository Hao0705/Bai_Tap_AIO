def merger_sort(my_list):

    if len(my_list) > 1:
        mid = len(my_list) // 2

        left_list = my_list[:mid]
        right_list = my_list[mid:]

        merger_sort(left_list)
        merger_sort(right_list)

        i = j = k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                my_list[k] = left_list[i]
                i += 1
                k += 1
            else:
                my_list[k] = right_list[j]
                k += 1
                j += 1

        while i < len(left_list):
            my_list[k] = left_list[i]
            k += 1
            i += 1

        while j < len(right_list):
            my_list[k] = right_list[j]
            k += 1
            j += 1

my_list = [10, 0, 5, 3, 7, 9, 6]
merger_sort(my_list)
print(my_list)
