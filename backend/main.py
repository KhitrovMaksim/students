import models
import os
import schemas

from fastapi import FastAPI, status, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from database import engine, SessionLocal

TEST_SERVER_IP = os.environ.get('TEST_SERVER_IP')

app = FastAPI(
    title='Students',
    description=f'Back to <a href="http://{TEST_SERVER_IP}/students">main page</a>.')

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/")
async def get_all_students(db: Session = Depends(get_db)):
    return db.query(models.Students).all()


@router.get("/{student_id}")
async def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student_model = db.query(models.Students).filter(models.Students.id == student_id).first()
    if student_model is not None:
        return student_model
    raise HTTPException(status_code=404, detail="Student not found")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_student(student: schemas.Student, db: Session = Depends(get_db)):
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


@router.put("/{student_id}")
async def update_student(student_id: int, student: schemas.Student, db: Session = Depends(get_db)):
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


@router.delete("/{student_id}")
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    student_model = db.query(models.Students).filter(models.Students.id == student_id).first()

    if student_model is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.query(models.Students).filter(models.Students.id == student_id).delete()

    db.commit()

    return successful_response(201)


@router.delete("/")
async def delete_all_students(db: Session = Depends(get_db)):
    db.query(models.Students).delete()
    db.commit()
    return "All students successfully deleted"


def successful_response(status_code: int):
    return {
        'status': status_code,
        'transaction': 'Successful'
    }


app.include_router(router)
