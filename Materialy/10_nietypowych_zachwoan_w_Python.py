from datetime import datetime

# Atrybuty klasowe
# class A:
#     a = 1

# class B(A):
#     pass

# class C(A):
#     pass

# B.a = 10
# print(A.a, B.a, C.a)
# A.a = 20
# print(A.a, B.a, C.a)


# Wartość domyślna funkcji

# def ddeby(blog=[]):
#     blog.append('Python')
#     print(blog)

# print(ddeby())
# print(ddeby())
# print(ddeby())

# Scope zmiennych 

# num = 5
# data = ['ddeby']

# def ddeby():
#     data.append('blog')
#     print(data)


# def blog():
#     num += 5
#     print(num)


# def dawid():
#     data += ['Python']


# print(ddeby())    
# print(blog())    
# print(dawid())


# Metoda __str__

# name = 'ddeby'
# num = 5

# print(name.__str__())
# print(num.__str__())
# print('ddeby'.__str__())
# print(5.__str__())

# Inicjalizacja funkcji

# def get_today(now=datetime.today()):
#     return now

# print(get_today())
# print(get_today())
# print(get_today())

# Dodawanie liczb rzeczywsitych

# print(0.1 + 0.1)
# print(0.2 + 0.2)
# print(0.1 + 0.2)

# Definicja tupli

# a_list = [1, 2]
# b_list = [1]
# a_tuple = (1, 2)
# b_tuple = (1)

# print(type(a_list))
# print(type(b_list))
# print(type(a_tuple))
# print(type(b_tuple))


# warunek z in

# 1 in [1]
# print(1 in [1] is True)

# Operatory logiczne

# print(False or 'python')
# print('ddeby' or False)
# print('ddeby' and 'python')
# print(False and 'python')
# print(True and 'python')

# edycja listy

# data = ['blog'] * 3
# ddeby = [['blog'] * 3] * 3

# data[1] = 'python'
# ddeby[1][1] = 'python'

# print(data)
# print(ddeby)

print(type(False) is bool)
print(type(False) is int)

print(isinstance(False, bool))
print(isinstance(False, int))