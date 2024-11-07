from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str
    age: int
    email: EmailStr

class StudentResponse(Student):
    id: int

class StudentSummary(BaseModel):
    summary: str
