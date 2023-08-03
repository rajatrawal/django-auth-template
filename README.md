# django-auth-template
The template with Django authentication features.

<p align='center'>
<img src="https://img.shields.io/badge/Django-239120?logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Python-239120?logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/html5-E34F26?logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/css3-1572B6?logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/bootstrap-563D7C?logo=bootstrap&logoColor=white" />
<img src="https://img.shields.io/badge/Github-181717?logo=github&logoColor=white" />

</p>


### Features with e-mail authentication -
1. Sign In 
1. Sign Up
1. Sign Out
1. Change Password
1. Forgot password
   
## Tech Stack

**Client:** HTML, CSS, JAVASCRIPT, BOOTSTRAP 5.3

**Server:** PYTHON, DJANGO

## Installation

Download the project by entering a command on git

```
git clone https://github.com/rajatrawal/django-auth-template.git
```

After cloning create and activate virtual environment.

```
virtualenv venv
```

```
source venv/Scripts/activate
```

Install required packages.

```
pip install -r requirements.txt
```
Run a python file named `` secret_key.py `` to generate a new secret key.
```
python secret_key.py

Output --> <SECRET_KEY>
```
Now paste the above key into settings.py file
```
SECRET_KEY =  <SECRET_KEY>
```

Now get the SMTP key  by creating an account on <https://www.brevo.com/> and use it in the settings.py file
```
EMAIL_HOST = <EMAIL_HOST>
EMAIL_HOST_USER = <EMAIL_HOST_USER>
EMAIL_HOST_PASSWORD = <EMAIL_HOST_PASSWORD>
DEFAULT_FROM_EMAIL = <DEFAULT_FROM_EMAIL>
```

Now run the django server.

```
python manage.py runserver
```
*Congratulations installation process is completed.*

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file.

```
SECRET_KEY = '<SECRET_KEY>'
EMAIL_HOST = '<EMAIL_HOST>'
EMAIL_HOST_USER = '<EMAIL_HOST_USER>'
EMAIL_HOST_PASSWORD = '<EMAIL_HOST_PASSWORD>'
DEFAULT_FROM_EMAIL = '<DEFAULT_FROM_EMAIL>'
```

## Reference
+ [CCBV website](https://ccbv.co.uk/)
+ [Priyanshu Guptas Video](https://youtu.be/zecETlA00OA)
  
