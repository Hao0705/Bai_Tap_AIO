from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade
    def describe(self):
        return f"Name_student: {self.name}, Yob_student: {self.yob}, Grade_student: {self.grade}"

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return f"Teacher_name: {self.name}, Teacher_yob: {self.yob}, Teacher_subject: {self.subject}"

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f"Doctor_name: {self.name}, Doctor_yob: {self.yob}, Doctor_specialist: {self.specialist}"

class Ward:
    def __init__(self, name):
        self.name = name
        self.list_person = []

    def add_person(self, person):
        self.list_person.append(person)

    def describe(self):
        for person in self.list_person:
            print(person.describe())
    def count_doctor(self):
        count = 0
        for person in self.list_person:
            if isinstance(person, Doctor):
                count += 1

        return count

    def sort_age(self):
        self.list_person.sort(key = lambda x: x.yob, reverse=False)

    def compute_average(self):
        sum = 0
        count = 0
        for teacher in self.list_person:
            if isinstance(teacher, Teacher):
                count += 1
                sum += teacher.yob

        if count != 0:
            return sum/count
        else:
            return None

ward = Ward("HaNoi")
student = Student("hao", 2003, 2.7)
teacher1 = Teacher("Huong", 1989, "Math")
teacher2 = Teacher("Phuong", 1985, "Physic")
doctor1 = Doctor("Khang", 1997, "doctor")
doctor2 = Doctor("Huong", 2002, "doctor")

ward.add_person(student)
ward.add_person(teacher1)
ward.add_person(teacher2)
ward.add_person(doctor1)
ward.add_person(doctor2)

ward.describe()
print("############################")
print(f"Count doctor: {ward.count_doctor()}")
print("############################")
ward.sort_age()
ward.describe()
print("############################")
print(f"Compute yob this teachers: {ward.compute_average()}")

