- `isinstance ()` - проверяет, является ли объект (первый аргумент) экземпляром или подклассом класса classinfo (второй аргумент).

	```
	numbers = [1, 2, 3, 4, 2, 5]
	result = isinstance(numbers, list)
	print(result)
	>>> True

- `lambda` - это небольшая анонимная функция. Лямбда-функция может принимать любое количество аргументов, но может иметь только одно выражение.
Синтаксис: lambda arguments : expression

	```
	x = lambda a : a + 10
	print(x(5))
	>>> 15

	x = lambda a, b : a * b
	print(x(5, 6))
	>>> 30

- `map()` - выполняет указанную функцию для каждого элемента в итерируемом объекте. Элемент отправляется функции в качестве параметра.
Синтаксис: map(function, iterables)

	```
	def double(n):
	    return n * 2

	my_list = [1, 2, 3, 4, 5]
	result = map(double, my_list)
	print(list(result))
	>>> [2, 4, 6, 8, 10]

- `filter()` - это функция высшего порядка в Python, которая позволяет фильтровать элементы итерируемого объекта на основе заданного условия.

	```
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	even_numbers = filter(lambda x: x % 2 == 0, numbers)
	print(list(even_numbers))
	>>> [2, 4, 6, 8, 10]

	def is_even(x):
	    return x % 2 == 0

	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	even_numbers = filter(is_even, numbers)
	print(list(even_numbers))
	>>> [2, 4, 6, 8, 10]
