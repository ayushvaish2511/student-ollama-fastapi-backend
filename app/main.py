from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.models import Student, StudentResponse, StudentSummary
from app.database import InMemoryDB
from app.services import generate_student_summary

app = FastAPI()

db = InMemoryDB()

@app.post("/students", response_model=StudentResponse)
async def create_student(student: Student):
    student_data = StudentResponse(**student.dict(), id=0) 
    created_student = db.create(student_data)
    return created_student

@app.get("/students", response_model=List[StudentResponse])
async def get_students():
    return db.get_all()

@app.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int):
    student = db.get_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=StudentResponse)
async def update_student(student_id: int, student: Student):
    existing_student = db.get_by_id(student_id)
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    updated_student = StudentResponse(**student.dict(), id=student_id)
    db.update(student_id, updated_student)
    return updated_student

@app.delete("/students/{student_id}", response_model=StudentResponse)
async def delete_student(student_id: int):
    student = db.delete(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.get("/students/{student_id}/summary", response_model=StudentSummary)
async def get_student_summary(student_id: int):
    student = db.get_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    try:
        summary = generate_student_summary(student.name, student.age, student.email)
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating summary: {str(e)}")
