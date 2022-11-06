# Students.
![Alt text](/example.png "The main page")
## The task.

The task has two parts:

**First part:**  
Create a good design with a strong validation for the fields below. Also, add a JS mask to the date of birth and phone number.

Required Fields:
- First Name, [minimum three characters]
- Last Name, [minimum three characters]
- Date of Birth, [ format 01/01/2000 ]
- Email Address,
- Phone Number [ format (999) 999-9999]
- Favorite sports [checkbox]

**Second part:**  
Using any programming language [PHP preferable ] build a simple web-application that save information into the database and then manage it. Create pages to show:  

Add Page -> To add a student record to the database.  
View Page -> To Show all the records.  
Managing Page -> To Show all records, edit and/or delete records.  

Make sure to add validation to the all input fields.
After you are done, please email us the zip containing all files and the dump of the database.
# Steps
- Set up a server with Docker and MySQL (Ansible, GitHub Actions);
- Create frontend app (Vue 3, JavaScript);
- Create backend app (FastAPI, Python, Swagger, Alembic);
- Create database (MySQL 8.0);
- Create pipeline ( GitHub -> GitHub Actions -> Docker).

# How to run locally
(Requirements: Python >= 3.9, npm >= 8.11)
- Install and run MySQL 8.0 server on your computer. 
- In MySQL 8.0 create database "students" and create user "teacher" with password and all privileges.
- Add environment variables:
> TEST_SERVER_DB_PASSWORD - add database user's password  
> TEST_SERVER_HOST - 127.0.0.1   
- Download project to your computer.
- Open project folder "backend" in terminal and run next commands:
```shell
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app --reload
```
- Use suggested link to use the backend part with nested Swagger documentation(e.g. http://127.0.0.1:8000/docs).
- Open project folder "frontend" in terminal and run next commands:
```shell
npm install
npm run serve
```
- Use suggested link to use the backend part with nested Swagger documentation(e.g. http://localhost:8080/).

# How to run globally (VDS, Cloud).
(Requirements: CPU 1 x 3.3GHz, RAM 1GB, HDD > 10GB, Ubuntu 20.04)
1. Run a server with a root login and password.
2. Create a GITHUB personal access token (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
3. Generate on your local machine SSH key pair.
4. Fork GITHUB repository - https://github.com/KhitrovMaksim/students
5. In your nearly created repository add secrets (Settings -> Secrets -> Actions secrets).
> TEST_SERVER_HOST (ip address only. E.g. 87.249.54.26)  
> TEST_SERVER_LOGIN (root, early created on step 1)  
> TEST_SERVER_PASSWORD (early created on step 1)   
> TEST_SERVER_PRIVATE_KEY (early created on step 3)   
> TEST_SERVER_PUBLIC_KEY (early created on step 3)   
> TEST_SERVER_DB_PASSWORD (think up a password)   
6. Run workflows in GitHub Actions:
> "Settings up the server"   
> "Start application"
7. Open browser and go to your ip address (E.g. 87.249.54.26 - for frontend, E.g. 87.249.54.26:8080 for Swagger documentation).

# About.

## Frontend.

Vue 3 (JavaScript, Options API) with bootstrap, vue cli, router, vuex, axios ...
On local machine you may use "npm run serve" command to run or build Docker Multi-Stage Image.

In GitHub Actions you may use workflow - Auto deploy frontend  - for automatic deployment on push. Or you can run this workflow manually.   

## Backend.

FastAPI (Python 3.9) with Swagger documentation, SQLAlchemy, Alembic (migrations)...
On local machine you may use "uvicorn main:app --reload" command to run or build Docker Image.

In GitHub Actions you may use workflow - Auto deploy backend  - for automatic deployment on push. Or you can run this workflow manually.   

## CI/CD.

### GitHub Actions - Setting up the server.

Ansible installs (by roles) on your server:
 - Docker.
 - MySQL 8.0 (configuring, with adding database "students" and user "teacher").
 - SSH (this role performs some basic security configuration:
1. Install software to monitor bad SSH access (fail2ban).
2. Configure SSH to be more secure (disabling root login, requiring key-based authentication, and allowing a custom SSH port to be set).
3. Set up automatic updates.

### GitHub Actions - Start / Stop application.

Start - To start your application by Build and Push images in GitHub container registry, and then run it on your server.
Stop - To stop your application by stopping running containers and deleting images.

### GitHub Actions - Auto deploy frontend / backend.

Automatically triggered workflows "on push" in folders "frontend" or "backend".

### GitHub Actions - MySQL dump.

Run workflow manually to create dump file (dump.sql). 
