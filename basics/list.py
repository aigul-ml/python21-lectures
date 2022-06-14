"============================ lists ================================="
# списки - изменяемые, индексируемый, упорядоченный, итерируемый тип данных предназначенный для хранения всех типов данных в определенном порядке. 

list1 = [1, 2, 3, 4, 'hello', [0, 1, 2, 3], {'a': 3}]

list1[1]     # 2 
list1[4]     # [0, 1, 2, 3]
list1[4][0]  # 0 
list1[4][0]  # h
list1[-1]['a'] # 3
str(list1[4][0])

"=================== создание списков ==========================================="
list1 = [1, 2]
list2 = list('hello')        # ['h', 'e', 'l', 'l', 'o']
''.join(list2)     # hello 

"=================== list methods ==========================================="
dir(list)

# append 
list3 = []
list3.append(1)
print(list3)     # 1 

list3.append('hello')
print(list3)    #[1, 'hello']

list3.append([1, 2, 3, 4])
print(list3)    # [1, 2, 3, 4]

list3.append(1, 2, 3)     # TypeErro: append() takes exactly one argument (3 given)

# clear - очищает список 
list3.clear()
print(list3)     # [] empty list 


# count - counts requested element in our list 
list4 = [1, 2, 3, 4, 1, 1, 1]
list4.count(1)     # 4
list4.count(2)     # 1 

# len method counts number of elements in our list 
list5 = ['hello', 'hello', 'hello']
list5.count('h')   # 0 
list5.count('hello')   # 3 
len(list5)      # 3 number of objects not letters separately 

list6 = [1, 2 [3, 4, 5], 6, 7, [8, 9, 10]]
len(list6)     # 6 

# extend - расширяет один список - merges elements of first list into second changing only first list 
list7 = [1, 2, 3]
list8 = [4, 5, 6]
list7.extend(list8)
print(list7)     # [1, 2, 3, 4, 6]
print(list8)     # [4, 5, 6]   remains the same unchanged 

# index - to get index of certain element in our list 
list8.index(3)      # 3 

list9 = [1, 2, 3, 4, 1, 2, 3, 5, 4, 1]
list9.index(1)     # 0 index of requested value 1 is 0 


# insert добавляет элемент по индексу list.insert(index, obj)

# methods lets us to include value into our dictionary from any location versus append method that works only from the last value 

list10 = [ 1, 2, 3]
list10.insert(0, 'hello')    # inserts 'hello' under index 0 which means in the first place 
print(list10)     # ['hello', 1, 2, 3]
list10.insert(2, 10)     # ['hello', 1, 10, 2, 3] - inserts value 10 under index 2 
list10.insert(100, 'bye')  # ['hello', 1, 10, 2, 3, 100]  since there is no index 100 insert method includes the value in the last place 


# pop returns value of deleted value in list 
# in other words pop removes elements following their index and prints it out 

list0 = [1, 2, 3, 4, 5, 6, 7]
popped = list0.pop()     # deletes last element in list 
print(list0, popped)      # [1, 2, 3, 4, 5, 6] 7

popped = list0.pop(1)
print(list0, popped)     # [1, 3, 4, 5, 6]  2 

print([1, 2, [3, 4, [5, 6]]].pop(2).pop(2).pop(1))

# remove method
remlist = [1, 2, 3, 4, 4, 5, 6, 7]
remlist.remove(2)
print(remlist)     # removes first element with value 2 

# map function returns our string into integers becasue we requested int map(int, str)
print(list(map(int, str(list).replace(', 2', '').replace(',', '').replace('[', '').replace(']', '').replace(' ', '').split(''))))


# reverse method - reverses values in our list in a reversed order 
list00 = [1, 2, 3, 4, 5]
print(list00.reverse())      # None
print(list00)                # [5, 4, 3, 2, 1]
new_list00 = list00[::-1]    # [1, 2, 3, 4, 5]

# sort method - sorts values in our list [values/ elements must be of the same type i.e. strings and strings; int and int]
list000 = [2, 1, 5, 6, 3, 0]
list00.sort()
print(list00)      # [0, 1, 2, 3, 5, 6]

# reverse=True cортирует по убыванию
list000 = [2, 1, 5, 6, 3, 0]
list00.sort(reverse=True)     # [6, 5, 3, 2, 1, 0]   





 
