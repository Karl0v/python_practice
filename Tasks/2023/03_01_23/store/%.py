import time
from random import randint, choices


class Schedule:
    def __init__(self, data: str, subject: list, duration: list):
        self.data = data
        self.subject = subject
        self.duration = duration

    def __str__(self):
        return f'at {self.data} {self.subject} passes {self.duration} min.'

    def subject_duration_list(self):
        s_list = list()
        for s, d in zip(self.subject, self.duration):
            s_list.append((s,d))
        return s_list


class Student:

    def __init__(self, name: str, subjects: set):
        self.name = name
        self.subjects = subjects

    def __str__(self):
        return f'{self.name}: {self.subjects}'

    def study(self, schedule: Schedule):
        print(f'{self.name} schedule:')
        for subject, hours in zip(schedule.subject, schedule.duration):
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
    monday = Schedule(subject=['algebra', 'geometry', 'physic'], duration=[4,5,6], data='monday')

    for student in students:
        student.study(monday)

    """monday = Subject(subject={'algebra', 'geometry', 'physic'}, duration={4,5,6})
    #print(monday.subject_duration_list(subject={'algebra', 'geometry', 'physic'}, duration={4,5,6}))
    print(monday)"""


