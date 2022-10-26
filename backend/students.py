from fastapi import FastAPI, status, Depends, HTTPException
from typing import Optional
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models
from pydantic import BaseModel, Field

app = FastAPI()

STUDENTS: list = [
    {
        "id": 1,
        "firstName": "Maksim",
        "lastName": "Khitrov",
        "dateOfBirth": "24/06/1985",
        "email": "khitrov.maksim@reqres.in",
        "phone": "(111) 111-1111",
        "favoriteSports": "Football, Tennis"
    },
    {
        "id": 2,
        "firstName": "Michael",
        "lastName": "Lawson",
        "dateOfBirth": "12/10/1970",
        "email": "michael.lawson@reqres.in",
        "phone": "(999) 999-9999",
        'favoriteSports': "Golf"
    }
]

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Student(BaseModel):
    first_name: str = Field(description="First name [ minimum three characters ]")
    last_name: str = Field(description="Last name [ minimum three characters ]")
    date_of_birth: str = Field(description="Date of Birth [ format 01/01/2000 ]")
    email: str = Field(description="Email [ format email@email.com ]")
    phone: str = Field(description="Phone number [ format (999) 999-9999 ]")
    favorite_sports: Optional[str] = Field(description="Favorite sports [ checkbox ]")


@app.get("/")
async def check_connection():
    return {"Connected!"}


@app.get("/students")
async def get_all_students(db: Session = Depends(get_db)):
    return db.query(models.Students).all()


@app.get("/students/{student_id}")
async def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student_model = db.query(models.Students).filter(models.Students.id == student_id).first()
    if student_model is not None:
        return student_model
    raise HTTPException(status_code=404, detail="Student not found")


@app.post("/students/", status_code=status.HTTP_201_CREATED)
async def add_student(student: Student, db: Session = Depends(get_db)):
    student_model = models.Students()

    student_model.first_name = student.first_name
    student_model.last_name = student.last_name
    student_model.date_of_birth = student.date_of_birth
    student_model.email = student.email
    student_model.phone = student.phone
    student_model.favorite_sports = student.favorite_sports

    db.add(student_model)
    db.commit()

    return successful_response(201)


@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student, db: Session = Depends(get_db)):
    student_model = db.query(models.Students).filter(models.Students.id == student_id).first()

    if student_model is None:
        raise HTTPException(status_code=404, detail="Student not found")

    student_model.first_name = student.first_name
    student_model.last_name = student.last_name
    student_model.date_of_birth = student.date_of_birth
    student_model.email = student.email
    student_model.phone = student.phone
    student_model.favorite_sports = student.favorite_sports

    db.add(student_model)
    db.commit()

    return successful_response(200)


@app.delete("/students/{student_id}")
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    student_model = db.query(models.Students).filter(models.Students.id == student_id).first()

    if student_model is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.query(models.Students).filter(models.Students.id == student_id).delete()

    db.commit()

    return successful_response(201)


@app.delete("/students/")
async def delete_all_students():
    STUDENTS.clear()
    return "The student successfully deleted"


def successful_response(status_code: int):
    return {
        'status': status_code,
        'transaction': 'Successful'
    }
