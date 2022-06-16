"===================== comprehensions ==============================="
# comprehensions - генерация последовательностей в одну сторону, используя цикл 

# создать список состоящий из чисел
list = []
for i in range(1, 10):
    list.append(i)
#  list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

list1 = list( (i for i in range(1, 10)) )
#  list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

list2 = [i for i in range(1, 10)]
#  list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

# создать список, состоящий из четных чисел
list0 = []
for i in range(1,10):
    # if not 0 
    if not i % 2:
        list0.append(i)
# comprehensions 
list0 = [i for i in range(1, 10) if not i % 2]

list0 = [i for i in range(2, 10, 2)]    # we begin from 2 and include steps 

# list0 = [2, 4, 6, 8]

list0 = [print(i) for i in range(10)]    
# [None, None, None, None, None, None] 

# 
print([input() for i in range(10)])
# на каждой итерации запрашивает инпут 


# создать список, состоящий из чисел от 1 до 10 но вместо чисел написать 'четное' или 'нечетное'
          # тернарный оператор - 2 варианта результата
list3 = [ (i, 'нечетное' if i % 2 else 'четное') for i in range(1, 10) ]
print(list3)

# создать список из чисел list4 заменив их на четное или нечетное
list4 = [1, 'hello', 2.0, 34.0, 'print', 3434]

list4 = [ 'нечетное' if i % 2 else 'четное' 
    for i in list4 
    if type(i) == int or type(i) == float]

print(list4)
# ['нечетное', 'четное', 'четное', 'четное']

list9 = [1, 2, 3, 4, 5]
list10 = ['a', 'b', 'c', 'd', 'e', 'f', 'e']

dict0 = dict( (list9[index], list10[index] for index in range(len(list9) )

dict1 = { list9[index]: list10[index] for index in range(len(list9)) }
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# создайте копию словаря 
dict8 = {"a": 1, "b": 2, 4: "c"}
dict6 = { key: value for key, value in dict8.items() }
# dict8 = {"a": 1, "b": 2, 4: "c"}

# меняем ключи значения местами в новом словаре 
dict8 = {"a": 1, "b": 2, 4: "c"}
dict5 = { value: key for key, value in dict8.items()}
# {1: 'a', 2: 'b', 'c': 4}

# имеется словарь, где значения - список с числами - создайте новый словарь, где значения - сумма тех чисел 
dict0 = {
    'a': [1, 2, 3, 4, 5],
    'b': [1, 5, 7, 89, 90],
    'c': [45, 23, 43, 56, 87],
    'd': [56, 34, 12, 45, 45]
}

dict1 = { key: sum(value) for key, value in dict0.items() }
# {'a': 15, 'b': 34, 'c': 149, 'd': 134}

"=============== вложенные comprehensions ============================="
# создайте словарь где ключами будут числа от 1 до 10 а значениями будут списки от 1 до числа, который является ключом
# 
dict0 = { i: list(range(1, i +1)) for i in range(1, 6) } 
print(dict0)
# { 1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5] }

dict0 = { i: [j for j in range(1, i+1)] for i in range(1, 6) }
print(dict0)


# создать список, состоящий из 10 списков, в которых строка 'hello world' повторяется 5 раз 
list0 = [
    ['hello world' for i in range(5)]
    for i in range(10)
]

