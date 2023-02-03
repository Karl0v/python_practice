"""class Dots:

    def __init__(self, dot_x: int, dot_y: int):
        self.dot_x = dot_x
        self.dot_y = dot_y"""


"""a1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a2 = list()
for i in a1:
    if i < 5:
        a2.append(i)
print(a1[:4])
print(a2)"""

"""a1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a1:
    if i < 5:
        print(i)"""


"""a2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
"c2 = list()"
for i in a2:
    if i not in b2:
        b2.append(i)
c2 = sorted(b2, reverse=True)
b2.sort(reverse=True)
print(c2)
print(b2)"""


"""dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {5: 500, 6: 60}
r = {**dict_a, **dict_b, **dict_c}
print(r)"""

"""dict_a = {'d': 500, 'b': 5874, 'c': 560, 'a': 400, 'e': 5874, 'f': 20}
result = sorted(dict_a, key=dict_a.get, reverse=True)[:3]


print(result)"""