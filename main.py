class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.lecturer_grades = {}

    def __str__(self):
        a = 0
        b = 0
        for key in self.lecturer_grades.keys():
            print(self.lecturer_grades[key])
            a += sum(self.lecturer_grades[key])
            b += len(self.lecturer_grades[key])
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {a / b}
                   """

    def lc_grades(self):
        a = 0
        b = 0
        for key in self.lecturer_grades.keys():
            print(self.lecturer_grades[key])
            a += sum(self.lecturer_grades[key])
            b += len(self.lecturer_grades[key])
        return a / b

    def __lt__(self, lecturer):
        return self.lc_grades() < lecturer.lc_grades()


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def grade_mentor(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        a = 0
        b = 0
        for key in self.grades.keys():
            a += sum(self.grades[key])
            b += len(self.grades[key])
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {a / b}
Курсы в процессе изучения: {" ".join(self.courses_in_progress)}
Завершенные курсы: {" ".join(self.finished_courses)}"""

    def st_grades(self):
        a = 0
        b = 0
        for key in self.grades.keys():
            a += sum(self.grades[key])
            b += len(self.grades[key])
        return a / b

    def __lt__(self, student):
        return self.st_grades() < student.st_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}  """


# Создание 2 экземпляров каждого класса
# Student
best_student = Student('Ruoy', 'Eman', 'your_gender')
simple_student = Student('Bill', 'Clingon', 'minbar')
# Rewiewer
cool_mentor = Reviewer('Some', 'Buddy')
simple_mentor = Reviewer('Ambassador', 'Kosh')
# Lecturer
cool_lecturer = Lecturer('John', 'Doe')
simple_lecturer = Lecturer('Londo', 'Molary')

# Methods
# Courses
# Rewiewers
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['SQL']
simple_mentor.courses_attached += ['Java']
simple_mentor.courses_attached += ['C']
# Students
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['SQL']
simple_student.courses_in_progress += ['Java']
simple_student.courses_in_progress += ['C']
# Lecturer
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['SQL']
simple_lecturer.courses_attached += ['Java']
simple_lecturer.courses_attached += ['C']
# Grades
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
simple_mentor.rate_hw(simple_student, 'Java', 10)
simple_mentor.rate_hw(simple_student, 'Java', 9)
simple_mentor.rate_hw(simple_student, 'Java', 10)
cool_mentor.rate_hw(best_student, 'SQL', 10)
cool_mentor.rate_hw(best_student, 'SQL', 8)
cool_mentor.rate_hw(best_student, 'SQL', 10)
simple_mentor.rate_hw(simple_student, 'C', 10)
simple_mentor.rate_hw(simple_student, 'C', 10)
simple_mentor.rate_hw(simple_student, 'C', 10)
best_student.grade_mentor(cool_lecturer, 'Python', 10)
best_student.grade_mentor(cool_lecturer, 'Python', 8)
best_student.grade_mentor(cool_lecturer, 'Python', 10)
best_student.grade_mentor(cool_lecturer, 'SQL', 10)
best_student.grade_mentor(cool_lecturer, 'SQL', 8)
best_student.grade_mentor(cool_lecturer, 'SQL', 10)
best_student.grade_mentor(cool_lecturer, 'Java', 10)
best_student.grade_mentor(cool_lecturer, 'Java', 8)
best_student.grade_mentor(cool_lecturer, 'Java', 9)
best_student.grade_mentor(cool_lecturer, 'C', 10)
best_student.grade_mentor(cool_lecturer, 'C', 8)
best_student.grade_mentor(cool_lecturer, 'C', 10)

print(best_student.grades)
print(best_student)
print(cool_lecturer)

lis_st = [best_student, simple_student]
list_lecturer = [cool_lecturer, simple_lecturer]


def middle_st(lis, course):
    a = 0
    for i in lis:
        if course in i.courses_in_progress and isinstance(i.grades[course][0], int):
            a = sum(i.grades[course]) / len(i.grades[course])
    return a


def middle_lc(lis, course):
    a = 0
    for i in lis:
        if course in i.courses_attached and isinstance(i.lecturer_grades[course][0], int):
            a = sum(i.lecturer_grades[course]) / len(i.lecturer_grades[course])
    return a


print(middle_st(lis_st, 'SQL'))
print(middle_lc(list_lecturer, 'Python'))
