def giaiThua(x):
    giaiThua = 1
    if x == 0:
        return giaiThua
    for i in range(1, x+1):
        giaiThua = giaiThua * i

    return giaiThua

def sin(x, n):
    sum = 0
    for i in range(n+1):
        sum = sum + pow(-1, i) * pow(x, 2*i + 1) / giaiThua(2*i +1)
    return sum

def cos(x, n):
    sum = 0
    for i in range(n+1):
        sum = sum + pow(-1, i) * pow(x, 2*i) / giaiThua(2*i)

    return sum
def sinh(x, n):
    sum = 0
    for i in range(n+1):
        sum = sum + pow(x, 2*i + 1) / giaiThua(2*i +1)
    return sum

def cosh(x, n):
    sum = 0
    for i in range(n+1):
        sum = sum + pow(x, 2*i) / giaiThua(2*i)

    return sum

try:
    x = int(input("Nhap x: "))
    n = int(input("Nhap n: "))
except:
    print("Nhap sai")

phepToan = input("Nhap ham muon tinh sin, cos, sinh, cosh: ")

if(phepToan == "sin"):

    sin_x = sin(x, n)
    print("sin({}) = {}".format(x, sin_x))
elif(phepToan == "cos"):

    cos_x = cos(x, n)
    print("cos({}) = {}".format(x, cos_x))
elif(phepToan == "sinh"):

    sinh_x = sinh(x, n)
    print("sinh({}) = {}".format(x, sinh_x))
elif(phepToan == "cosh"):

    cosh_x = cosh(x, n)
    print("cosh({}) = {}".format(x, cosh_x))
else:

    print("Nhap dung ten ham")

    