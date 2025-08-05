def max_num_in_sublist(start, end, my_list):
    x = my_list[start]

    for i in range(start+1, end+1):
        if x < my_list[i]:
            x = my_list[i]

    return x

def function(my_list, num_list):

    new_list = []
    length = len(my_list)

    for i in range(num_list-1, length, 1):
        value = max_num_in_sublist(i-num_list+1, i, my_list)
        new_list.append(value)

    return new_list

raw_input = input("Nhap cac phan tu cua list: ")
my_list = list(map(int, raw_input.split()))

while True:
    num_list = int(input("Nhap chieu dai cua sublist: "))

    if 0 < num_list < (len(my_list) + 1):
        break
    else:
        print("Nhap so lon hon 1 va nho hon do dai cua list")

new_list = function(my_list, num_list)
print(new_list)