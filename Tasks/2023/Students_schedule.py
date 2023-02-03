import time
from random import randint, choices


class Schedule:
    def __init__(self, data: str, allow_subjects: list):
        self.data = data
        self.subjects = list()
        self.durations = list()
        self.schedule = list()
        self.allow_subjects = set(allow_subjects)

    def __str__(self):
        return f'at {self.data} {self.subjects} passes {self.durations} min.'


    def add_item(self, subject: str, duration: int):
        if (subject in self.allow_subjects or subject == 'rest') and 0 < duration <= 6:
            self.schedule.append((subject,duration))
            self.subjects.append(subject)
            self.durations.append(duration)

        else:
            print(f'{self.data}Somthing go wrong in add_item {subject} {duration}')


class Student:
    def __init__(self, name: str, subjects: set):
        self.name = name
        self.subjects = subjects

    def __str__(self):
        return f'{self.name}: {self.subjects}'

    def study(self, schedule: Schedule):
        print(f'{self.name} schedule:')
        for subject, hours in zip(schedule.subjects, schedule.durations):
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
        students.append(Student(name=name, subjects=set(choices(subjects, k=student_subjects_count))))
        print(students[-1])
    subjects.append('rest')
    monday = Schedule(data='monday', allow_subjects=subjects)
    monday.add_item('algebra', 2)
    monday.add_item('geometry', 2)
    monday.add_item('rest', 1)
    monday.add_item('physics', 4)

    for student in students:
        student.study(monday)