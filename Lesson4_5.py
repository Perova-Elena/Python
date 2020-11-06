from functools import reduce
def multiplication(el_1, el_2):
    return el_1 * el_2
list = [el for el in range(100, 1001) if el % 2 == 0]
print(list)
print(reduce(multiplication, list))

