# django-auth-template
The template with Django authentication features.

### Features with e-mail authentication -
1. Sign In 
1. Sign Up
1. Sign Out
1. Change Password
1. Forgot password
   

## Installation

Download project by entering command on git

```
git clone https://github.com/rajatrawal/elevator-system.git
```

After cloning setup and activate virtual environment.

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
Run python file named `` secret_key.py `` to genrate new secret key.

```
python secret_key.py

Output --> <SECRET_KEY>
```
Now paste above key in settings.py file
```
SECRET_KEY =  <SECRET_KEY>
```
Now change SMTP settings by creating 
Now run django server.

```
python manage.py runserver
```
