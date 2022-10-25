from fastapi import FastAPI

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


@app.get("/students")
async def get_all_students():
    return STUDENTS


@app.get("/students/{student_id}")
async def get_student_by_id(student_id: int):
    return STUDENTS[student_id]


@app.post("/students/")
async def add_student(first_name: str, last_name: str, date_of_birth: str, email: str, phone: str, favorite_sports: str):
    STUDENTS.append({
        "id": 3,
        "firstName": first_name,
        "lastName": last_name,
        "dateOfBirth": date_of_birth,
        "email": email,
        "phone": phone,
        "favoriteSports": favorite_sports
    })
    return "The student successfully added"


@app.put("/students/{student_id}")
async def update_student(student_id: int, first_name: str, last_name: str, date_of_birth: str, email: str, phone: str, favorite_sports: str):
    STUDENTS[student_id-1] = {
        "id": student_id,
        "firstName": first_name,
        "lastName": last_name,
        "dateOfBirth": date_of_birth,
        "email": email,
        "phone": phone,
        "favoriteSports": favorite_sports
    }
    return STUDENTS


@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    STUDENTS.pop(student_id)
    return "The student successfully deleted"


@app.delete("/students/")
async def delete_all_students():
    STUDENTS.clear()
    return "The student successfully deleted"
