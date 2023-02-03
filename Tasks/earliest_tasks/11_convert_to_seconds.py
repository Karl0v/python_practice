"""
11. Секунди у дні/години/хвилини
Складність: 3/5
Параметри:
	ціле число
Повертає: словник з ключами days, hours, minutes, seconds та їх відповідними значеннями
Наприклад:
	function(60 * 60 + 30) -> {"days": 0, "hours": 1, "minutes": 0, "seconds": 30}
	function(60 * 60 * 25) -> {"days": 1, "hours": 1, "minutes": 0, "seconds": 0}
	function(60 * 20 + 15) -> {"days": 0, "hours": 0, "minutes": 20, "seconds": 15}
Підказка: метод divmod та таблиця конвертацій
	1 день = 24 години
	1 година = 60 хвилин
	1 хвилина = 60 секунд
"""


def convert_seconds(seconds):
    original_seconds = seconds
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return original_seconds, {"days": days, "hours": hours, "minutes": minutes, "seconds": seconds}


if __name__ == '__main__':
    orig, resp = convert_seconds(62)
    print(orig)
    print(resp)
    print(convert_seconds(62))
    print(convert_seconds(60 * 59 + 59))
    print(convert_seconds(60 * 62 + 59))
    print(convert_seconds(60 * 60 * 25))
    print(convert_seconds(60 * 60 * 75 + 60 * 4 + 30))

