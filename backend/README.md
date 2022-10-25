Python, FastAPI, Pydantic, Swagger, SQLAlchemy, Alembic, Docker



Add Python virtual env in IntelliJ IDEA

```shell
pip list
python.exe -m pip install --upgrade pip
pip install virtualenv
cd .\venv\Scripts\
activate
deactivate
pip install fastapi[all]
uvicorn students:app --reload
pip install alembic
alembic init alembic
```
Swagger documentation 
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/openapi.json

GET - get all students / get student by id  
POST - add new student / add twenty students  
PUT - edit the student  
DELETE - remove a student / remove all students  