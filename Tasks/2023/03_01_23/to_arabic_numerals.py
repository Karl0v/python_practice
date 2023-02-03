while True:
    your_rome_number = input('Input your rome number -> ').upper()
    qty = 0
    rome_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in your_rome_number:
        qty += rome_numbers[i]

    if "IV" in your_rome_number:
        qty -= 2
    if "IX" in your_rome_number:
        qty -= 2
    if "XL" in your_rome_number:
        qty -= 20
    if "XC" in your_rome_number:
        qty -= 20
    if "CD" in your_rome_number:
        qty -= 200
    if "CM" in your_rome_number:
        qty -= 200
    print(qty)
    a = input('If you want to exit press "x", continue - any button \n -> ')
    if a == 'x':
        break
    else:
        continue

