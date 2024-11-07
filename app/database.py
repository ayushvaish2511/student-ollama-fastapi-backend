from typing import List, Optional
from app.models import StudentResponse

class InMemoryDB:
    def __init__(self):
        self.students = {}
        self.counter = 1

    def create(self, student: StudentResponse) -> StudentResponse:
        student.id = self.counter
        self.students[self.counter] = student
        self.counter += 1
        return student

    def get_all(self) -> List[StudentResponse]:
        return list(self.students.values())

    def get_by_id(self, student_id: int) -> Optional[StudentResponse]:
        return self.students.get(student_id)

    def update(self, student_id: int, student: StudentResponse) -> Optional[StudentResponse]:
        if student_id in self.students:
            self.students[student_id] = student
            return student
        return None

    def delete(self, student_id: int) -> Optional[StudentResponse]:
        return self.students.pop(student_id, None)
