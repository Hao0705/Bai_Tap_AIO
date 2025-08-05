d1 = {'a': [1, 2], 'b': 5}
d2 = d1.copy()

d2['b'] = 6
print(d2)
print(d1)

d3 = {int(i): i for i in range(10)}
d4 = d3.copy()
d4[0] = 10

print(d3)
print(d4)
