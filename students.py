class Student:
    

    def __init__(self, name: str, grade1: float, grade2: float, grade3: float):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def average(self) -> float:
        
        return (self.grade1 + self.grade2 + self.grade3) / 3

    def __repr__(self):
        return (
            f"Student(name={self.name!r}, "
            f"grade1={self.grade1}, grade2={self.grade2}, grade3={self.grade3}, "
            f"average={self.average():.2f})"
        )


class SchoolClass:
    

    def __init__(self):
        self._students: list[Student] = []

    def add_student(self, student: Student) -> None:
        
        self._students.append(student)

    def rank_matter_1(self) -> list:
        
        return sorted(self._students, key=lambda s: s.grade1, reverse=True)

    def rank_matter_2(self) -> list:
        
        return sorted(self._students, key=lambda s: s.grade2, reverse=True)

    def rank_matter_3(self) -> list:
        
        return sorted(self._students, key=lambda s: s.grade3, reverse=True)

    def __repr__(self):
        return f"SchoolClass({self._students!r})"


if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print("=== Classement Matière 1 ===")
    for student in school_class.rank_matter_1():
        print(student)

    print("\n=== Classement Matière 2 ===")
    for student in school_class.rank_matter_2():
        print(student)

    print("\n=== Classement Matière 3 ===")
    for student in school_class.rank_matter_3():
        print(student)