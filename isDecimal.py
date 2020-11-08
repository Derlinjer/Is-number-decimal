from random import random
import sys


#функция для выявления десятичной дроби
def is_decimal(x):
	for i in x:
		if i == '.':
			return True
	return False


#находит период числа после точки, отбрасывая не повторяющуюся часть
def find_period_without_not_period_part(part_after_point_a):
	i = 0
	a_string = part_after_point_a
	while not(find_period(a_string)) and i < len(part_after_point_a):
		i += 1
		a_string = part_after_point_a[i: len(part_after_point_a)]
	if i < len(part_after_point_a):
		return [part_after_point_a[:i], find_period(a_string)]
	return None
	
	
# слайсит переменную по длине
def slice_by_N(fractional_part, length_substring):
	array = []
	j = len(fractional_part) // length_substring
	for i in range(1, j + 1):
	 	z = fractional_part[(i * length_substring) - length_substring: i * length_substring]
	 	array.append(z)
	return array


#проверяет первый элемент массива на равность с остальнымыми элементами массива
def is_substring_same_in_array(sub_string_array):
	for i in range(1, len(sub_string_array)):
		if sub_string_array[0] != sub_string_array[i]:
			return False
	return True


#используется для проверки на какое количество строк можно разделить наше число
def find_denominator(a):
	array = []
	i = a - 1
	while i > 0:
		if  a % i == 0:
			array.append(i)
		i -= 1
	return array


def find_period(strin):
	denominators = find_denominator(len(strin))
	stroka = []
	for i in range(len(denominators)):
		if is_substring_same_in_array(slice_by_N(strin, denominators[i])):
			stroka.append(slice_by_N(strin, denominators[i])[0])
	return stroka[-1] if len(stroka) > 0 else ''


x = input(str('Введите число: '))

your_number = is_decimal(x)

if not(your_number):
	print('Ваше число не является десятичной дробью')
	sys.exit()

y = x.split('.')

part_after_point = y[1]

if find_period_without_not_period_part(part_after_point) is None :
	print('Введённая вами дробь не имеет периода.')
	sys.exit()

z = find_period_without_not_period_part(part_after_point)

first_part = z[0]

second_part = z[1]

print(y[0] + '.' + first_part + '(' + second_part + ')') if len(second_part) > 0 else print('Введённая вами дробь не имеет периода.')