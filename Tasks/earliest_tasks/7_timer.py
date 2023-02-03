"""7. Таймер
Складність: 2/5
Параметри:
  ціле число (секунди)
Повертає: повідомлення кожної секунди скільки часу залишилось та повідомлення коли час вийшов
Наприклад:
  function(6):
    6
    5
    4
    3
    2
    1
    Тум-тум, 6 секунд вже пройшло!
Підказка: метод sleep з модулю time"""
from time import sleep


def timer(seconds):
    seconds_passed = seconds
    while seconds_passed > 0:
        print(seconds_passed)
        sleep(1)
        seconds_passed = seconds_passed - 1
    print(f"Тум-тум, {seconds} секунд вже пройшло!")


if __name__ == '__main__':
    timer(15)