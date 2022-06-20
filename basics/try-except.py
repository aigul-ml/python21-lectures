list_ = [1, 2, 3, 4]
# list_[100]   - IndexError: list index out of range
# list_.pop(199)  - IndexError: pop index out of range 


# KeyError 
# исключение, которое выходит, когда мы обращаемся по несуществующему ключу 
dict_ = {'a': 1}
# dict_.pop['b']   - KeyError: 'b'
print(dict_.get('b'))   # не ошибка, выйдет None если ключа нет 

# ValueError: когда мы пытаемся распаковать какую-то последовательность, где количество переменных и элементов в последовательности не совпадает
# когда мы в функцию передаем некорректный для нее тип данных 

# a, b, c = 'ab'
# ValueError - not enough values to unpack (expected 3, got 2)
# int('abcds')
# ValueError: invalid literal for int() with base 10: '10d'


# TypeError 
# когда мы пытаемся использовать методы не свойственные данному типу данных 
# или когда мы пытаемся передать в функцию больше или меньше аргументов чем принимает функция 

# for i in 12345:
# TypeError: 'int' object is not iterable

# 5 + '5' TypeError 

# hash('abcdsssdfdfdfdfs')
# hash([1, 2, 3, 4])
# TypeError: unhashable type 'list'  


# IndentationError 
# неправильное использование отступов 

# TabError
# неправильное использование пробелов

# ZeroDivisionError 
# при делении на ноль 

"===================== Обработка исключений ==============================="
# чтобы код не прекращал свою работу при некорректных данных
# try:
    #num = int(input())
    # код, который может вызвать ошибку

# except ValueError:
    # print('Please enter number.')
    # Ошибка которая может возникнуть
    # код, который сработает если ошибка не вышла в try

# finally:
    # код, который сработает в любом случае

try:
    num = int(input())
except ValueError:
    print('Enter number.')
else:
    print('number', num)
# если в input придет число - выведется то что мы прописали в else
# если в input придет нечисло - выведется то что мы прописали в except 

# raise - вызвать ошибку
try: 
    raise NameError
except ValueError:
    print('ValueError')
except KeyError:
    print('KeyError')

# 
num = int(input())
res = num + 10 
print(res + 20)

# 
try:
    print('hello')
except:
    print('except')
else:
    print('else')

