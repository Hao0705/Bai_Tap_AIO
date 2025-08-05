def charters(_str):
    kytu = {}

    for i in _str:
        if i == " ":
            continue
        if i in kytu:
            kytu[i] += 1
        else:
            kytu[i] = 1
    return kytu

_str = input("Nhap chuoi:")
kytu = charters(_str)
print(kytu)
