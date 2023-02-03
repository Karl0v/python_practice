class Students:

    def __init__(self, name: str, subject: set):
        self.name = name
        self.subject = subject

    def __str__(self):
        return f'{self.name}: {self.subject}'


if __name__ == "__main__":
    jhon = Students(name='Jhon', subject={'geometry', 'hystory', 'algebra'} )
    osvald = Students(name='Oswald', subject={'geometry', 'algebra'})
    anna = Students(name='Anna', subject={'physics', 'literature'})
    alex = Students(name='Alex', subject={'algebra', 'geometry'})
    nino = Students(name='Nino', subject={'physics'})
    julia = Students(name='Julia', subject={'algebra'})
    inga = Students(name='Inga', subject={'geometry'})
    orest = Students(name='Orest', subject={'literature'})
    olga = Students(name='Olga', subject={'geometry'})
    clint = Students(name='Clint', subject={'literature'})
    dorothy = Students(name='Dorothy', subject={'algebra'})

    students = [jhon, osvald, anna]


    ask = input('Input subject what you interested -> ').lower()
    for student in students:
        if ask in student.subject:
            print(f'{student.name} learns {ask}')


