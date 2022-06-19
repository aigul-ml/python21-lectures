# Задание 1
# Создайте список name_of_friends с именами пяти друзей.
# Выведите эти имена по одному, обращаясь к каждому элементу списка.
# Задание 14, 13, 3, 7

# from hashlib import new
# name_of_friends = ['Anna', 'Daniel', 'Linda', 'Tamara', 'Lena']
# for name in name_of_friends:
#     print(name)

# Задание 2
# Выберите свой любимый вид транспорта (например, мотоциклы или машины) и создайте список labels с марками этого вида транспорта.
# Используя цикл for, выведите утверждения о каждом из элементов списка labels.
# К примеру, если ваш список выглядит так: ['Honda', 'Kawasaki']
# Вывод должен быть: I like brand Honda 
#                    I like brand Kawasaki

# labels = ['Honda', 'Kawasaki']
# for label in labels: 
#     print(f'I like brand {label}')

# Задание 3
# Дан список name_of_list в котором хранится строка.
# Разрежьте ее на две равные части.
# Если длина строки нечетная, то длина первой части должна быть на один символ больше.
# Переставьте эти две части местами, при этом каждый символ должен являться отдельной строкой.
# Результат запишите в новый список new_list и выведите на экран.
# Например, если список выглядит так: ['Helloworld!'] 
# то, в результате получим: ['o', 'r', 'l', 'd', '!', 'H', 'e', 'l', 'l', 'o', 'w'] 

name_of_list = ['Helloworld']
string_ = name_of_list.pop()

# part1 = len(string_) + 
# if len(string_) % 2 == 0




# Задание 4
# Создайте список list_, состоящий ровно из двух строк.
# Переставьте эти строки местами.
# Результат запишите в новый список new_list и выведите в консоль получившийся результат
# Например, если list_ выглядит так: ['world', 'hello'] 
# результат будет: ['hello', 'world']
# list_ = ['world', 'hello']
# new_list = list_.reverse()
# print(list_)


# Задание 5
# Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст: suitcase = []. Однако он может вместить всего 5 вещей.

# Положите 5 вещей в чемодан с помощью метода append()
# Вы передумали, и решили убрать последнюю вещь. Вспомните, какой метод помогает удалить последний элемент.
# Вы решили положить в чемодан другую вещь, только в первое место (т.е. по индексу 0). Вспомните метод, который ставит элементы по индексу.
# Распечатать чемодан
# Пример:
# положили 5 вещей 
# ['футболка', 'шорты', 'сланцы', 'очки', 'кепка'] 
#решили убрать последнюю 
# ['футболка', 'шорты', 'сланцы', 'очки'] 
#в начале, добавили новую вещь 
# ['панама', 'футболка', 'шорты', 'сланцы', 'очки'] 

# suitcase = []
# suitcase.append('футболка')
# suitcase.append('шорты')
# suitcase.append('сланцы')
# suitcase.append('очки')
# suitcase.append('кепка')
# suitcase.pop()
# suitcase.insert(0, 'панама')
# print(suitcase)



# Задание 6
# Создать список чисел nums.
# Используя цикл и метод списка, запишите все числа меньше 5 в новый список.
# Результат запишите в переменную res и выведите в терминал. nums выглядит так:
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# результат будет: res = [1, 1, 2, 3]
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = [num for num in nums if num < 5]
# print(res)


# Задание 7
# Вы принимаете от пользователя последовательность чисел, разделенных запятой в переменную.
# Создайте список list_ и кортеж tuple_ с этими числами и распечатайте их.
# Для проверки, введите числа через запятую(без пробелов) в поле во вкладке INPUT.
# Например, для чисел введенных как 1,2,3,4 вывод будет: ['1', '2', '3', '4'] ('1', '2', '3', '4') 
# values = input()
# int_as_strings = values.split(',')
# ints = map(int, int_as_strings)
# lst = list(ints)
# tup = tuple(lst)
# print(lst, tup)


# Задание 8
# Создайте список чисел list_.
# Пройдитесь по элементам списка и преобразуйте все числа в строку.
# Результат запишите в новый список new_list и выведите в терминал.
# К примеру, если в list_: [1, 2, 3, 4, 5]
# то в new_list получим: ['1', '2', '3', '4', '5'] используйте встроенную функцию str()
# list_ = [1, 2, 3, 4, 5]
# new_list = [str(x) for x in list_]
# print(new_list)



# Задание 9
# Создайте список чисел list_.
# Переберите элементы циклом и вместо четных чисел, поставьте строку четное, а вместо нечетных нечетное.
# Результат записать в новый список new_list и вывести в терминал.
# К примеру, если в списке хранятся такие числа: [1, 2, 3, 4, 5]
# результат будет: ['нечетное', 'четное', 'нечетное', 'четное', 'нечетное']
# list_ = [1, 2, 3, 4, 5]
# new_list = ['четное' if x % 2 == 0 else 'нечетное' for x in list_]
# print(new_list)



# Задание 10
# Используя функцию range() создайте список list_ из 20 произвольных чисел.
# Распечатайте результат
# Примерный вывод: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 
# list_ = [i for i in range(20)]
# print(list_)

# Задание 11
# При помощи функции range() создайте список list_ из чётных чисел от 0 до 100 (включительно).
# Распечатайте результат.
# Примерный вывод: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100] 
# list_ = [i for i in range(0, 101) if i % 2 == 0]
# print(list_)


# Задание 12
# Создайте два списка list1, list2 со случайным набором чисел.
# Объедините эти списки.
# Затем, выведите сумму всех чисел в консоль.
# К примеру, если в перемнных хранятся такие списки: [11, 23, 45, 7, 9] [21, 4, 16, 8, 10] 
# Объединив их и распечатав сумму всех чисел, получим: 154 
# list1 = [11, 23, 45, 7, 9]
# list2 = [21, 4, 16, 8, 10] 
# list1.extend(list2)
# total = sum(list1)
# print(total)


# Задание 13
# Написать программу, которая будет принимать от пользователя числа через запятую, без пробелов.
# числа поместить в список list_ и вывести в отсортированном виде.
# Числа переданные во вкладке INPUT сохраняются в строковом типе данных.
# Поэтому, к примеру, для чисел 15,364,27,2 отсортированный список будет выглядеть так: ['15', '2', '27', '364']
# list_ = input().split(',')
# list_.sort()
# print(list_)


# Задание 14
# Создать три числа в списке list_.
# Вывести на экран yes, если среди них есть одинаковые, иначе вывести ERROR.
# Например, для списка [1, 1, 3], вывод будет: yes 
# а для списка [1, 2, 3]: ERROR 
# list_ = [1, 1, 3]
# list_ = [1, 1, 3]



# Задание 15
# Записать в список list_ все числа в промежутке от 54 до 9184 делящиеся на 5 без остатка.
# Распечатайте результат.
# Вывод должен быть: [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, ... ... ... ... ...  ... ... ... ... ... ... , 9125, 9130, 9135, 9140, 9145, 9150, 9155, 9160, 9165, 9170, 9175, 9180] 
# list_ = [i for i in range(55, 9184) if i % 5 == 0]
# print(list_)





