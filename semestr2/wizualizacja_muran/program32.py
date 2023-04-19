list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Co bedzie wynikiem list1+list2?
wynik = list1 + list2
#print(wynik)


months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
months.sort()
#print(months)

def get_month_number(month_name):
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    return months.get(month_name, None)

def filter_names(names, letter):
    filtered_names = [name for name in names if name[0] > letter]
    return filtered_names

names = ['John', 'Jane', 'Alice', 'Bob', 'Adam',]
letter = 'B'

print(filter_names(names,letter))


def filter_long_names(names):
    filtered_names = [name for name in names if len(name) > 4]
    return filtered_names

print(filter_long_names(names))

def is_palindrome(word):
    return word == word[::-1]

#print(is_palindrome("radar"))
#print(is_palindrome("python"))

def is_sorted_descending(numbers):
    return all(numbers[i] >= numbers[i+1] for i in range(len(numbers)-1))

#print(is_sorted_descending([10, 5, 3]))  # True
#print(is_sorted_descending([3, 5, 10]))  # False

def cube_list(numbers):
    return [num ** 3 for num in numbers]

#print(cube_list([1, 2, 3]))
#print(cube_list([-1, -2, 0]))

# def func(list,n1,n2):
#     for i in list:
#         if i == n1:
#             print("nassz_i",i,"koniec")
#             list[i] = n2
#
#
#     return list

def func(lista, n1, n2):
    for i in range(len(lista)):
        if lista[i] == n1:
            lista[i] = n2
    return lista
lista = [1.5,2,3.7,4,5,6,7,5,8,5]
#print(func(lista,5,0))

import math
def func1(lista, n1, n2):
    for i in range(len(lista)):
        if math.isclose(lista[i], n1):
            lista[i] = n2
    return lista

lista = [1.5,2,3.7,4.9999999999,5,6,7,5,8,5]
print(func1(lista,5,0))

