# example 1 
a = [1, 2, 3, 4]
b = []
numbers = ''

def func(a):
    for i in a: 
        if i > 1: 
            b.append(i)
    global numbers
    for i in b: 
        numbers += str(i)
func(a)
print(numbers)


# example with comprehensions 
d = {
    k: v for k, v in zip(range(10), range(10, 21))
}
print('d: ', d)
# d:  {0: 10, 1: 11, 2: 12, 3: 13, 4: 14, 5: 15, 6: 16, 7: 17, 8: 18, 9: 19}


# example 
list_ = [1, 2, 3, 4, 5, 6, 7]

list2 = [i**2 if i >3 else i for i in list_ if i % 2 != 0]
print(list2)  # [1, 3, 25, 49]


# example
d2 = {
    None: 20
}
print(d2)
# {None: 20}


# example 

d4 = {
    k if k % 2 == 0 else None: v if v % 2 == 1 else v ** 2 for k, v in zip(range(10), range(10, 21)) if k % 2 == 0
}
print(d4)
# {0: 100, 2: 144, 4: 196, 6: 256, 8: 324}


# example
d3 = {}
for k, v in zip(range(10), range(10, 21)):
    if k % 2 == 0: 
        if v ==3:
            key = k if k % 2 == 0 else None
            value = v if v % 2 == 1 else v ** 2
            d3[key] = value
print(d3)