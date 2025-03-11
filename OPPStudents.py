class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
        self.attendance = {}  

    def add_grade(self, grade):
        if isinstance(grade, Grade): 
            self.grades.append(grade)

    def get_average(self):
        if not self.grades:  # Avoiding division by zero
            return 0
        total = sum(grade.score for grade in self.grades)  
        return total / len(self.grades)

    def add_attendance(self, date, present):
        self.attendance[date] = present


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def is_passing(self):
        return self.score >= self.minimum_passing

#---------------

# Examples
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

# Adding grades
pieter.add_grade(Grade(100))
pieter.add_grade(Grade(80))
pieter.add_grade(Grade(90))

# Checking average
print(f"{pieter.name}'s average grade: {pieter.get_average()}")

# Was he present?
pieter.add_attendance("2024-12-20", True)
print(f"Attendance record for {pieter.name}: {pieter.attendance}")
