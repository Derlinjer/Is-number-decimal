import sys

x = input('Введите начальное значение списка: ')

n = input('Введите конечное значение списка: ')

if "." in x:
	print('Введите 0 или натуральноe число: ')
	sys.exit()

if x == '':
	print('Введите 0 или натуральноe число: ')
	sys.exit()

if int(x) < 0:
	print('Введите 0 или натуральноe число: ')
	sys.exit()

if "." in n:
	print('Введите 0 или натуральное число: ')
	sys.exit()

if n == '':
	print('Введите число: ')
	sys.exit()

if int(n) < 0:
	print('Введите 0 или натуральное число: ')
	sys.exit()

if int(n) < int(x):
	print('Введите число, превышающее первое введённое число: ')
	sys.exit()

fibonacci_array = [0, ]

def fibonacci_number(n):
	a = 0
	b = 1
	for i in range(int(n)):
		a, b = b, a + b 
		fibonacci_array.append(a)

print(fibonacci_number(n))

print(fibonacci_array[int(x): int(n)])