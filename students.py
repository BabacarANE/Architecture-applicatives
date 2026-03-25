from collections.abc import Iterable, Iterator


class Student:
    """Représente un étudiant avec un nom et 3 notes dans 3 matières."""

    def __init__(self, name: str, grade1: float, grade2: float, grade3: float):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def average(self) -> float:
        """Calcule la moyenne des 3 matières."""
        return (self.grade1 + self.grade2 + self.grade3) / 3

    def __repr__(self):
        return (
            f"Student(name={self.name!r}, "
            f"grade1={self.grade1}, grade2={self.grade2}, grade3={self.grade3}, "
            f"average={self.average():.2f})"
        )


def add_grade4(grade4_value: float):
    """Décorateur de classe qui ajoute une 4ème matière à tous les étudiants."""
    def decorator(cls):
        original_init = cls.__init__

        def new_init(self, name: str, grade1: float, grade2: float, grade3: float):
            original_init(self, name, grade1, grade2, grade3)
            self.grade4 = grade4_value

        cls.__init__ = new_init
        return cls
    return decorator


@add_grade4(0.0)
class Student(Student):
    pass


class StudentIteratorMatter1(Iterator):
    """Itérateur qui parcourt les étudiants du meilleur au plus mauvais pour la matière 1."""

    def __init__(self, students: list):
        self._sorted_students = sorted(students, key=lambda s: s.grade1, reverse=True)
        self._index = 0

    def __next__(self) -> Student:
        if self._index >= len(self._sorted_students):
            raise StopIteration
        student = self._sorted_students[self._index]
        self._index += 1
        return student


class StudentIteratorMatter2(Iterator):
    """Itérateur qui parcourt les étudiants du meilleur au plus mauvais pour la matière 2."""

    def __init__(self, students: list):
        self._sorted_students = sorted(students, key=lambda s: s.grade2, reverse=True)
        self._index = 0

    def __next__(self) -> Student:
        if self._index >= len(self._sorted_students):
            raise StopIteration
        student = self._sorted_students[self._index]
        self._index += 1
        return student


class StudentIteratorMatter3(Iterator):
    """Itérateur qui parcourt les étudiants du meilleur au plus mauvais pour la matière 3."""

    def __init__(self, students: list):
        self._sorted_students = sorted(students, key=lambda s: s.grade3, reverse=True)
        self._index = 0

    def __next__(self) -> Student:
        if self._index >= len(self._sorted_students):
            raise StopIteration
        student = self._sorted_students[self._index]
        self._index += 1
        return student


class SchoolClass(Iterable):
    """Représente une classe d'étudiants."""

    def __init__(self):
        self._students: list[Student] = []

    def add_student(self, student: Student) -> None:
        """Ajoute un étudiant à la classe."""
        self._students.append(student)

    def __iter__(self) -> StudentIteratorMatter1:
        """Retourne un itérateur triant les étudiants par matière 1."""
        return StudentIteratorMatter1(self._students)

    def iter_matter_2(self) -> StudentIteratorMatter2:
        """Retourne un itérateur triant les étudiants par matière 2."""
        return StudentIteratorMatter2(self._students)

    def iter_matter_3(self) -> StudentIteratorMatter3:
        """Retourne un itérateur triant les étudiants par matière 3."""
        return StudentIteratorMatter3(self._students)

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

    print("=== Vérification grade4 ajouté par le décorateur ===")
    for student in school_class:
        print(f"{student.name} -> grade4={student.grade4}")

    print("\n=== Classement Matière 1 (via __iter__) ===")
    for student in school_class:
        print(student)

    print("\n=== Classement Matière 2 (via iter_matter_2) ===")
    for student in school_class.iter_matter_2():
        print(student)

    print("\n=== Classement Matière 3 (via iter_matter_3) ===")
    for student in school_class.iter_matter_3():
        print(student)