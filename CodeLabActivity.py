class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I am {self.name}.")

class Student(Person):
    def study(self):
        print(f"{self.name} is reviewing lessons.")

print("--- 1. Single Inheritance Output ---")
student = Student("Jenifer")
student.introduce()
student.study()
print("-" * 35)

class Runner:
    def __init__(self, speed):
        self.speed = speed

    def run(self):
        print(f"Running at {self.speed} km/h.")

class Jumper:
    def __init__(self, height):
        self.height = height

    def jump(self):
        print(f"Jumping {self.height} meters high.")

class Athlete(Runner, Jumper):
    def __init__(self, name, speed, height):
        Runner.__init__(self, speed)
        Jumper.__init__(self, height)
        self.name = name

    def introduce(self):
        print(f"Athlete name: {self.name}")


print("--- 2. Multiple Inheritance Output ---")
athlete = Athlete("Jenifer", 20, 2)
athlete.introduce()
athlete.run()
athlete.jump()
print("-" * 35)

 
class Gadget:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Brand: {self.brand}")


class Phone(Gadget):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_model(self):
        print(f"Model: {self.model}")


class SmartPhone(Phone):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)
        self.os = os

    def show_details(self):
        self.show_brand()
        self.show_model()
        print(f"Operating System: {self.os}")


print("--- 3. Multilevel Inheritance Output ---")
phone = SmartPhone("Samsung", "S24", "Android")
phone.show_details()
print("-" * 35)

class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Working...")


class Teacher(Employee):
    def work(self):
        print(f"{self.name} is teaching students.")


class Engineer(Employee):
    def work(self):
        print(f"{self.name} is designing systems.")


print("--- 4. Hierarchical Inheritance Output ---")
teacher = Teacher("Jenifer")
engineer = Engineer("Alex")
teacher.work()
engineer.work()
print("-" * 35)


class Course:
    def __init__(self, course):
        self.course = course

    def show_course(self):
        print(f"Course: {self.course}")


class WorkingStudent(Student, Course):
    def __init__(self, name, course, job):
        Student.__init__(self, name)
        Course.__init__(self, course)
        self.job = job

    def show_info(self):
        self.introduce()
        self.show_course()
        print(f"Part-time job: {self.job}")


print("--- 5. Hybrid Inheritance Output ---")
ws = WorkingStudent("Jenifer", "Object-Oriented Programming", "Tutor")
ws.show_info()
print("-" * 35)