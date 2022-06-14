list_student = []
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        list_student.append(self)
        
        
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def gpa(self):
        self.all_grade = []
        for self.gr in self.grades.values():
            self.all_grade.extend(self.gr) #Список всех оценок
        return round(sum(self.all_grade)/len(self.all_grade), 2)  #Среднее всех оценок
    
    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname} \nСредняя оценка за лекции: {self.gpa()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершённые курсы: {", ".join(self.finished_courses)}')
        return res
    
    #     добавим возможность сравнения студентов 
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student!')
            return
        return self.gpa() < other.gpa()
    
        
    
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'
 

list_lector = []
class Lecturer(Mentor):
    def __init__(self, name, surname, ):
        super().__init__(name, surname, )
        self.courses_attached = []
        self.grades = {}
        list_lector.append(self)
        
    def gpa(self):
        self.all_grade = []
        for self.gr in self.grades.values():
            self.all_grade.extend(self.gr) #Список всех оценок
        return round(sum(self.all_grade)/len(self.all_grade), 2)  #Среднее всех оценок
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname} \nСредняя оценка за лекции: {self.gpa()}'
        return res
    
        #     добавим возможность сравнения Lectorov 
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lector!')
            return
        return self.gpa() < other.gpa()
        
        
               
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
        

def gpa_student(cours): #средняя оценка студентов по курсу
    list_grade = []
    for d in list_student:
        #print(d.grades)
        for key, value in d.grades.items():
            if key == cours:
                list_grade.extend(value)
    #print(list_grade)
    if len(list_grade) == 0:
        return 'нет такого курса'
    return round((sum(list_grade)/len(list_grade)), 1)

def gpa_lector(cours): #средняя оценка лекторов по курсу
    list_grade = []
    for d in list_lector:
        #print(d.grades)
        for key, value in d.grades.items():
            if key == cours:
                list_grade.extend(value)
    #print(list_grade)
    if len(list_grade) == 0:
        return 'нет такого курса'
    return round((sum(list_grade)/len(list_grade)), 1)
            



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['Java']

better_student = Student('Djo', 'Bidonovich', 'Somsing')
better_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['C++']
lec1 = Lecturer('Bob', 'Bobovich')
lec1.courses_attached += ['Python']
lec1.courses_attached += ['C++']

lec2 = Lecturer('Barak', 'Barakovich')
lec2.courses_attached += ['Python']

better_student.rate_lec(lec2, 'Python', 1)
better_student.rate_lec(lec2, 'Python', 2)

best_student.rate_lec(lec1, 'Python', 8)
best_student.rate_lec(lec1, 'Python', 7)
best_student.rate_lec(lec1, 'C++', 5)
best_student.rate_lec(lec1, 'C++', 2)
best_student.rate_lec(lec1, 'C++', 1)
best_student.rate_lec(lec1, 'C++', 2)

rev1 = Reviewer('Ivan', 'Petrov',)
rev1.courses_attached += ['Python']
rev1.courses_attached += ['C++']

rev1.rate_hw(best_student, 'Python', 10)
rev1.rate_hw(best_student, 'Python', 10)
rev1.rate_hw(best_student, 'C++', 5)

rev1.rate_hw(better_student, 'Python', 2)
rev1.rate_hw(better_student, 'Python', 3)
 
# print(best_student.courses_in_progress)
# print(best_student.grades)
# print(rev1.name)

print(lec1)
print(lec2)
print (lec1 > lec2)
# print(rev1)
# print(lec1)
# print (best_student.grades)
print (best_student)

# print (better_student.grades)
print (better_student)
print(best_student > better_student)
# print(str(list_student))

print(gpa_student('Python'))  
print(gpa_lector('C++')) 

 

