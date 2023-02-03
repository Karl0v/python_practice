"""13. Нумерологія)
Складність: 1/5
Параметри:
	ціле число
Повертає: суму цифр числа
Наприклад:
	function(252) -> 9
	function(2022) -> 6"""

#number = int(input("Input your number -> "))


def thirteen(number):
    suma = 0
    while number > 0:
        digit = number % 10
        suma = suma + digit
        number = number // 10
    return suma

print(thirteen(1234))


def twelve(file):
    cod = file[file.rfind('.')+1:]
    return cod

print(twelve('path/to/archive.docx.zip'))


def first(y: list, cut_number: int, left=True):
    if left:
        x = y[:cut_number]
    else:
        x = y[-cut_number:]
    return x


y = [5, 6, 3, 2, 1, 5, 8, 9]
print(first(y, 10, left=False))
print(first(y, 1, left=True))
print(first([5, 6, 3, 2, 1], 2, left=True))
print(first([5, 6, 3, 2, 1], 2, left=False))
print(first([5, 6, 3, 2, 1], 10, left=False))

'''. Таймер (покращена версія)
Складність: 3/5
Параметри:
	datetime.timedelta об'єкт
Повертає: повідомлення кожної секунди скільки часу залишилось та повідомлення коли час вийшов
Наприклад:
	function(timedelta(minutes=2, seconds=30)):
		2м30с
		2м29с
		2м28с
		...
		0м01с
		Тум-тум, 2 хвилини 30 секунд вже пройшло!
Підказка: клас timedelta з модулю datetime'''

