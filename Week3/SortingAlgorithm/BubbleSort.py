def is_empty(my_list):
    if len(my_list) == 0:
        return True
    else:
        return False

def bubble_sort(my_list):

    if is_empty(my_list):
        print("List is empty.")
    else:

        for i in range(len(my_list)):
            key = True
            for j in range(len(my_list)-i-1):

                if my_list[j] > my_list[j+1]:
                    x = my_list[j]
                    my_list[j] = my_list[j+1]
                    my_list[j+1] = x

                    key = False
                else:
                    continue

            if key:
                return my_list

my_list = [0, 12, 5 ,3 ,9, 7, 10]
my_list = bubble_sort(my_list)

print(my_list)
