# # Задание 1
# # Создайте список list_ из целых чисел от 1 до 100 (включительно). Нужно использовать comprehension.
list_ = [i for i in range(1, 101)] 
print(list_)

# # Задание 2
# # Создайте список list_ из нечётных целых чисел в промежутке от 1 до 50. Нужно использовать comprehension.
list_ = [i for i in range(1, 50) if i % 2 != 0]
print(list_)

# Задание 3
# Создайте список используя
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# и запишите в новый список int_list
# только четные числа, которые больше нуля. Нужно использовать comprehension.
list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
int_list = [num for num in list_ if num % 2 == 0 and num > 0]
print(int_list)

# Задание 4
# Создайте список list_ из квадратов всех чисел от 1 до 25 (включительно). В результате, список list_ должен выглядеть так:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625] 

list_ = [ i ** 2 for i in range(1, 26)]
print(list_)

# Задание 5
# Используя данный список:
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# создайте новый список int_list, где все элементы, строки старого списка str_list, будут преобразованы в числовой тип данных:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
int_list = [int(i) for i in str_list]
print(int_list)


# Задание 6
# Создайте список list_ из чисел от 1 до 10 (включительно), заменяя четные числа - квадратом числа(число умноженное само на себя), нечетные добавьте без изменений.
# В результате должны получить:
# [1, 4, 3, 16, 5, 36, 7, 64, 9, 100] 

list_ = [i ** 2 if i % 2 == 0 else i for i in range(1, 11)]
print(list_)


# Задание 7
# Пройдитесь по промежутку чисел от 1 до 10 и запишите в список list_ True вместо числа, если число чётное и False вместо числа, если число нечетное.

# Результат будет таким: [False, True, False, True, False, True, False, True, False, True] 
# 1 - нечетное число, не делится на 2 без остатка, вместо числа записывается - False

# 2 - четное число, 2 деленное на 2, будет 1 без остатка, записывается - True

# 3 - нечетное, т.к 3 деленное на 2, даст остаток 1, значит вместо числа будет False

# и так далее . . .
list_ = [True if i % 2 == 0 else False for i in range(1, 11)]
print(list_)

# Задание 8
# Создайте список из 10 произвольных имён list_name.

# Затем пройдитесь по данному списку и если длина имени меньше или равна 4 буквам создайте список new_list имя на shorter, а если больше на longer.
# Пример:
list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# Вывод в терминале:
# ['shorter', 'shorter', 'longer', 'longer', 'shorter', 'longer', 'shorter', 'longer', 'longer', 'shorter'] 

list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
new_list = ['shorter' if len(name) <= 4 else 'longer' for name in list_name]
print(new_list)

# Задание 9
# Создайте словарь dict_ из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты. Нужно использовать comprehension.

dict_ = {num: num ** 2 for num in range(1, 11)}
print(dict_)

# Задание 10
# Запросите у пользователя число от 1 до 10 в переменную n. Затем пройдитесь по промежутку чисел от 1 до 500(включительно) и запишите в словарь dict_, только те числа, которые кратны числу n (делятся на число n без остатка), введенное пользователем. Ключом будет само число, а значением его квадрат.
# К примеру, пользователь ввел число: 9 
# Получаем словарь:
# Из списка чисел от 1 до 500, числа 9, 18, 27, 36, 45 ... и.т.д делятся на 9 без остатка, записываем их как ключи.
# {9: 81, 18: 324, 27: 729, 36: 1296, 45: 2025, 54: 2916, 63: 3969, 72: 5184, 81: 6561, 90: 8100, 99: 9801, 108: 11664, 117: 13689, 126: 15876, 135: 18225, 144: 20736, 153: 23409, 162: 26244, 171: 29241, 180: 32400, 189: 35721, 198: 39204, 207: 42849, 216: 46656, 225: 50625, 234: 54756, 243: 59049, 252: 63504, 261: 68121, 270: 72900, 279: 77841, 288: 82944, 297: 88209, 306: 93636, 315: 99225, 324: 104976, 333: 110889, 342: 116964, 351: 123201, 360: 129600, 369: 136161, 378: 142884, 387: 149769, 396: 156816, 405: 164025, 414: 171396, 423: 178929, 432: 186624, 441: 194481, 450: 202500, 459: 210681, 468: 219024, 477: 227529, 486: 236196, 495: 245025} 
# Значениями записываем квадраты(число умноженное само на себя ) - 81, т.к 9 х 9 = 81, 324, т.к 18 х 18 = 324, и.т.д

n = input('Введите число от 1 до 10: ')

dict_ = {i: i ** 2 for i in range(1, 501) if i % int(n) == 0}
print(dict_)


# Задание 11
# Дан словарь a в котором значениями являются целые числа. Пройдитесь по элементам и запишите в dict_ значения на список чисел от 1 до числа, которое является значением. Нужно использовать comprehension.

a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
dict_ = {k: [v for v in range(1, v+1)] for k, v in a.items()}
print(dict_)


# Задание 12
# Создайте словарь dict_ где ключами будут строки, а значениями произвольные числа. Затем пройдитесь по элементам и запишите в a вместо значения строку 'even', если значение четное, а если нет то 'odd'.

# Например, если у нас есть словарь:
# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# То результатом будет: {'first': 'odd', 'second': 'even', 'third': 'odd'}

dict_ = {'first': 1, 'second': 2, 'third': 3} 

a = {k: ('even' if v % 2 == 0 else 'odd') for (k, v) in dict_.items()}
print(a)

# Задание 13
# Дано предложение
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# Получите список чисел list_ из этого предложения. Вывод будет таким: ['1984', '13', '1000'] 

string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
list_ = [word for word in string_.split() if word.isdigit()]
print(list_)

# Задание 14
# Дан вложенный словарь dict_ (словарь состоящий из других словарей) в котором ключом является имя студента, а значением словарь с его оценками по 3 предметам.

# Распечатайте новый словарь, где вместо оценкок будет название предмета, по которому студент имеет высший балл. Нужно использовать comprehension.

# Например: dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91}, 'Olga': {'history': 92, 'math': 96, 'literature': 81}, 'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# Результат: {'Timur': 'math', 'Olga': 'math', 'Nik': 'literature'}

dict_ = {
    'Timur': {'history': 90, 'math': 95, 'literature': 91}, 
    'Olga': {'history': 92, 'math': 96, 'literature': 81}, 
    'Nik': {'history': 84, 'math': 85, 'literature': 87}}

new_dict = {key1: key2 for key1, val1 in dict_.items() for key2, val2 in val1.items() if key2 == max(val1, key = val1.get)}

print(new_dict)


# Задание 15
# Дан словарь my_dict значениями в котором являются другие словари.

# Создайте новый словарь dict_, оставив те же ключи, но заменив значения, значениями внутренних словарей.

# Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
#dict_ = {'first': 1, 'second': 2} 

my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
dict_ = {key1: val2 for key1, val1 in my_dict.items() for key2, val2 in val1.items()}
# ????????????????????????????????#################################################
# EXPLAIN: part about [key2, val2 in val1.items()]
print(dict_)

# Экстра задание 1
# Создайте список list_ от 0 до 10 включительно c помощью специальной функции которая генерирует последовательно чисел,
# отфильтруйте список оставив в нем только четные элементы,
# затем разделите каждый элемент на 2 и выведите результат,
# нужно работать только с одним списком, нельзя создавать доп. списки.
# Необходимо использовать list comprehension
# Распечатайте результат.

# ????????????????????????????????#################################################
# EXPLAIN: VS code gives an error but platform accepted as correct  
# list_ = [i / 2 i for i in range(0, 11) if i % 2 == 0]
# print(list_)



# Экстра задание 2
# Создайте словарь dict_ в котором ключами будут числа, а значениями строки. Перебирите словарь циклом:

# если ключ четный, нужно заменить его значение на длину этого значения
# если ключ нечетный то возвести длинну его значения в 3 степень
# Распечатайте dict_. Нужно работать только с одним словарем, нельзя создавать доп. словарь. Необходимо использовать dict comprehension.


# Экстра задание 3
# Создайте 2 сета set1 и set2 из 10 рандомных элементов
# Затем объедините их (специальным методом) в перменную full_set,
# И если их длина меньше 20, то вы должны вывести сообщение:
# "В этом сете было 3 повторения, его длина составляет 17",
# 3 это количество элементов, которые были не уникальны,
# Если же длина равна 20 то выведите сообщение "Ваш обьединенный сет полностью уникальный!"
# Необходимо использовать set comprehension, на этапе создания сетов.
# Так же используйте генератор последовательности в comprehension чтобы создать множества из 10 элементов.
# Необходимо использовать set comprehension, на этапе создания сетов.
# Например после использования set comprehension в set1 храниться множество: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# B set2: {8, 9, 10, 11, 12, 13, 14, 15, 16, 17}
# Результат работы программы будет следующий:
# "В этом сете было 2 повторения, его длинна составляет 18"





