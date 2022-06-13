"======================== Dictionaries =================================="

# словарь - изменяемый, итерируемый, неиндексируемый и неупорядоченный тип данных, в котором значения хранятся в парах (ключ: значение)

dict = {'a': 'Hello', 'b': 2, 'c': 3}
print(dict['a'])    # Hello

# ключами в словаре могут являться все неизменяемые типы данных 
# значениями в словаре могут являться любые типы данных 
# ключи должны быть уникальными т.е. не повторяться 

dict_ = {
    1: 'hello',
    'a': 4,
    4.5: {'a': 5},      # to print value 5 --> print(dict_[4.5]['a'])
    # {'s': 5}: 44   --> TypeError 
}

"====================================== Методы словаря ==============================================="
dict_.clear()     # clears dictionary
print(dict_)     # {} prints empty dictionary 

dict_ = dict_.fromkeys([1, 2, 4])
print(dict_)      # {1: None, 2: None, 4: None}

dict_ = dict.fromkeys([1, 2, 4], 'hello')
print(dict_)      # {1: 'hello', 2: 'hello', 4: 'hello'}

dict_ = {'a': 2, 'a': 3, 'a': 4}
print(dict_)      # {'a': 4}

dict_['a'] = 5
print(dict_)      # {'a': 5}

dict_ = {'a': 1, 'b': 2}
dict_['a']      # 1 
dict_['c']      # KeyError

# get method used to get value of requested key 
dict_.get('a')     # 1 
dict_.get('c')     # None

dict_.get('c', 5)   # 5
dict_.get('a', 5)   # 1 

# keys 
dict_.keys()    # returns keys from values 

dict_.values()   # returns values from keys 

dict_.items()   # dict_items([('a', 1) ('b', 2)])


dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {3: 'd', 4: 'e'}
dict1.update(dict2)
# update method добавляет пары из второго словаря в первый 
print(dict1)       # {'a': 5}

# pop method удаляет пары по ключу и возвращает значение 
print(dict1.pop(3))    # d 
print(dict1)         # {1: 'a', 2: 'b', 4: 'e'}

# popitem method удаляет последнюю пару и возвращает пару 
print(dict1.popitem())

# LIFO last in first out ---> pop.items() uses this method 
# FIFO first in first out 

dict4 = {1: 'a'}
dict4[2] = 'b'
dict4[3] = 'c'
dict4[2] = 'a'
print(dict4.popitem())       # 







