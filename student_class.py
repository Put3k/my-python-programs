class Student:
    # Write your code here.
    students_dict ={}
    all_students =[]

    def __init__(self, name: str, grade: int or float):

        self.name = name

        #Chceck if value range is valid in initalization
        if not 0 <= grade <= 100:
            raise ValueError("Invalid value. Grade must be between 0 and 100!")
        self._grade = grade

        Student.students_dict[self.name] = {"name": self.name, "grade": self._grade, "object": self}
        Student.all_students.append(self.name)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Invalid value. Grade must be between 0 and 100!")
        self._grade = value
        Student.students_dict[self.name]['grade'] = value

    @staticmethod
    def calculate_average_grade(students):
        if len(students) == 0:
            return -1

        grade_sum = 0
        counter = 0

        for i in students:
            grade_sum += i.grade
            counter += 1

        average_grade_value = grade_sum/counter
        return average_grade_value

    @classmethod
    def get_average_grade(cls):
        if len(cls.all_students) == 0:
            return -1

        grade_sum = 0
        counter = 0

        for i in cls.all_students:
            grade = Student.students_dict.get(i,{}).get("grade")
            grade_sum += grade
            counter += 1
        
        average_grade = grade_sum/counter
        return average_grade

    @classmethod
    def get_best_student(cls):

        if len(cls.students_dict) == 0:
            return None

        best_student = None
        best_grade = 0

        for i in cls.students_dict.values():
            if i['grade'] > best_grade:
                best_grade = i["grade"]
                best_student = i["object"]
        return best_student

students = [
            Student("Simon", 69),
            Student("Alex", 55),
            Student("James", 8),
]

test1 = Student.calculate_average_grade(students)
print(test1)