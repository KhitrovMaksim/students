# Students

## The task

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
- Set up a server with Docker and MySQL (Ansible, GitHub Actions)
- Creat frontend app (VueJS, JavaScript)
- Creat backend app (FastAPI, Python)
- Creat pipeline ( -> GitHub -> GitHub Actions -> Docker)
# Server setup
Host - in the email  
## Ansible role Docker
An Ansible Role that installs Docker and Docker Compose on the server.
## Ansible role MySQL
Installs and configures MySQL 8.0 on the server.  
DB Name - Students  
DB User - teacher  
DB Password - in the email  
## Ansible role SSH
This role performs some basic security configuration on the server. It attempts to:
- Install software to monitor bad SSH access (fail2ban)
- Configure SSH to be more secure (disabling root login, requiring key-based authentication, and allowing a custom SSH port to be set)
- Set up automatic updates