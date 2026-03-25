from collections.abc import Iterable, Iterator


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


class StudentIteratorMatter1(Iterator):
   

    def __init__(self, students: list):
        self._sorted_students = sorted(students, key=lambda s: s.grade1, reverse=True)
        self._index = 0

    def __next__(self) -> Student:
        if self._index >= len(self._sorted_students):
            raise StopIteration
        student = self._sorted_students[self._index]
        self._index += 1
        return student


class SchoolClass(Iterable):
    

    def __init__(self):
        self._students: list[Student] = []

    def add_student(self, student: Student) -> None:
    
        self._students.append(student)

    def __iter__(self) -> StudentIteratorMatter1:
    
        return StudentIteratorMatter1(self._students)

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

    print("=== Classement Matière 1 (via rank_matter_1) ===")
    for student in school_class.rank_matter_1():
        print(student)

    print("\n=== Classement Matière 2 ===")
    for student in school_class.rank_matter_2():
        print(student)

    print("\n=== Classement Matière 3 ===")
    for student in school_class.rank_matter_3():
        print(student)

    print("\n=== Classement Matière 1 (via __iter__) ===")
    for student in school_class:
        print(student)