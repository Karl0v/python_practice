import time
from random import randint, choices


class Student:
    def __init__(self, name: str, subjects: set):
        self.name = name
        self.subjects = subjects

    def __str__(self):
        return f'{self.subjects}: {self.name}'

    def study(self, schedule: list):
        print(f'{self.name} schedule:')
        for subject, hours in schedule:
            if subject in self.subjects:
                print(f' {self.name} studies {subject} for {hours}')
            elif subject == 'rest':
                print(f' {self.name} rests for {hours}')
            else:
                print(f' {self.name} does not study {subject}, so {self.name} rests for {hours}')
            time.sleep(hours)


if __name__ == '__main__':
    subjects = ['physics', 'geometry', 'algebra', 'politology', 'history', 'geography', 'literature', 'national culture']
    len_subjects = len(subjects)
    students = list()
    for name in ['Oleh', 'John', 'Maria', 'Elizabeth', 'Sebastian', 'Phillip']:
        student_subjects_count = randint(1, len_subjects)
        student_subjects = choices(subjects, k=student_subjects_count)
        student = Student(name=name, subjects=set(student_subjects))
        students.append(student)
        print(students[-1])

    schedule = [('algebra', 2), ('rest', 1), ('geometry', 2), ('physics', 4)]
    for student in students:
        student.study(schedule)