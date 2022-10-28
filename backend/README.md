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
uvicorn main:app --reload
pip install sqlalchemy
pip install pymysql
pip install alembic
pip install cryptography
alembic init migrations
```
Swagger documentation 
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/openapi.json

GET - get all students / get student by id  
POST - add new student / add twenty students  
PUT - edit the student  
DELETE - remove a student / remove all students 


## Run mysql on Windows 
1. Win key + R.
2. services.msc
3. Now search for MySQL service based on the version that is installed.
4. Click on 'stop', 'start' or 'restart' the service option.

## Migrations
https://medium.com/pythonistas/managing-multiple-databases-migrations-with-alembic-10025a4b3ab3
```shell
alembic revision -m "create new column"
alembic upgrade b9812ec5e377
alembic downgrade -1
alembic revision -m "Create student table"
alembic upgrade a114666a1adf
```