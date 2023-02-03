import time

class Subject:
    def __init__(self, subject: str, duration: int):
        self.subject = subject
        self.duration = duration

    def __str__(self):

        return f'{self.subject} passes {self.duration} min.'

    def subject_duration_list(self):
        return f'{self.subject} - {self.duration} hours'


class Student:

    def __init__(self, name: str, subjects: list):
        self.name = name
        self.subjects = [Subject(subject, duration) for subject, duration in subjects]

    def __str__(self):
        return f'{self.name} studies: {" ".join([str(subject) for subject in self.subjects])}'

    def study(self, day: str):
        schedule = [subject.subject_duration_list() for subject in self.subjects]
        print(f'{day}: {" ".join(schedule)}')
        for subject in self.subjects:
            print(f'{self.name} study {subject.subject} for {subject.duration} hours.')
            time.sleep(subject.duration)

subjects = [('math', 3), ('physics', 2), ('geometry', 3)]
student = Student('John', subjects)
student.study('Monday')