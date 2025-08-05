import math

from scipy.constants import alpha


def activations(x, name_function):
    if(name_function == "sigmoid"):

        sigmoid = 1/(1+math.exp(-x))
        print("sigmoid({}) = {}".format(x, sigmoid))
    elif(name_function == "relu"):

        if x < 0:
            print("Relu = 0")
        else:
            print("Relu = {}".format(x))
    else:
        if x <= 0:
            elu = 0.01*(math.exp(x)-1)
            print("Elu = {}".format(elu))
        else:
            print("Relu = {}".format(x))



def check(x, name_function):
    if(type(x) == str):
        print("x mustbe a number")
        return False
    if(name_function == "sigmoid" or name_function == "relu" or name_function == "elu"):
        return True
    else:
        print("Nhap dung ten ham sigmoid or relu or elu")
        return False
    return True

name_function = input("Nhap ten ham: ")
try:
    x = int(input("Nhap x:"))
    if (check(x, name_function)):
        activations(x, name_function)

except:
    print("Nhap sai")

