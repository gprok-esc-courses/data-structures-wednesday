
class Student:
    def __init__(self, name, grades) -> None:
        self.name = name
        self.grades = grades

    
a = Student("Mike", [23, 45, 62])
b = Student(a.name, list(a.grades))

b.name = "Paul"
b.grades.append(44)

print(a.name)
print(a.grades)