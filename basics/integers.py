"=======================Переменные========================"
# Variables/ переменные - ссылки на ячейки памяти, где хранятся какие-то данные 

a = 4
b = 4

a + b 
print(id(a), a)
print(id(b))


"======================Ввод и вывод данных===================================="
# print - функция вывода данных в терминал

a = 4
print(a)

# input function - функция ввода данных с терминала
a = input()
print("Введенное число", a, b)

"===============Числа===================================="
# integers - целые числа 
# float - вещественные (с плавающей точкой) 
b = 0.2

# decimal - точное вещественное число 
# чтобы использовать decimal необходимо импортировать:
from decimal import Decimal
c = Decimal(0.1)

# complex - комплексные числа 
b = complex(1,5)
print(b)

a = 5
a = 6
a = 7
print(a)

# =================Операции над числами===============================
1 + 2 # сложение 
1 * 2 # умножение  
1 / 2 # деление 
1 // 2 # целочисленное деление (int 7)
1 % 2 # остаток от деления (int 1)
1 ** 2 # возведение в степень
25 ** 0.5  # квадратный корень числа 

# модуль числа - из отрицательного числа сделать положительное 
# |-5| = 5 
abs(-5)   # 5 
abs(10)  # 10
abs(-2.4)  # 2.4 

# pov: 
# 1. возводит число в определенную степень
# 2. возвращает остаток от деления результата 1го действия на третье число 

pow(2, 3)   # 8 = 2 ** 3 
pow(2, 3, 4)  # 8 % 4 = 0 
# (2 ** 3) % 4  = 0 

# divmod - функция, которая принимает 2 числа и возвращает 2 числа, где первое - это целая часть от деления, а второе - остаток от деления 
divmod(15, 2)  # 7, 1 
divmod(9, 3)  # 3, 0

# round - функция, которая округляет число 
round(5.6)   # 6
round(3.5)  # 4
round(3.49)  # 3 (берет первое число после точки)
round(4.5095, 2)  # мы указали 2 цифры после запятой оставить при округлении 

# sqrt - функция для нахождения корня числа - для работы необходимо импортировать из библиотеки math 
from math import sqrt
sqrt(36)    # 6 
sqrt(25)   # 5 