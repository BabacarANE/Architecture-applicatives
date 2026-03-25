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

    def __repr__(self):
        return f"SchoolClass({self._students!r})"
