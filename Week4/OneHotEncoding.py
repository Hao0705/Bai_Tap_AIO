def one_hot_encoding(my_list):

    set_value = set(my_list)
    new_list = list(set_value)
    length = len(new_list)

    arr = [[0 for _ in range(length)] for _ in range(length)]

    for row in range(length):
        for col in range(length):
            if row == col:
                arr[row][col] = 1
    my_dict = {}

    for i in range(length):
        my_dict[new_list[i]] = arr[i]

    return my_dict

my_list = ['a', 'b', 'c', 'd', 'a']
my_dict = one_hot_encoding(my_list)

print(my_dict)