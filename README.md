# django-auth-template
This project is a Django-based authentication template that provides the following features with e-mail authentication:

<p align='center'>
<img src="https://img.shields.io/badge/Django-239120?logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Python-239120?logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/html5-E34F26?logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/css3-1572B6?logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/bootstrap-563D7C?logo=bootstrap&logoColor=white" />
<img src="https://img.shields.io/badge/Github-181717?logo=github&logoColor=white" />

</p>


### Features with e-mail authentication -

This project is a Django-based authentication template that provides the following features with e-mail authentication:

**Sign In**: Users can sign in using their registered e-mail and password.

**Sign Up**: New users can sign up by providing their e-mail and creating a password.

**Sign Out**: Logged-in users can sign out to securely end their session.

**Change Password**: Users have the option to change their account password.

**Forgot Password**: If users forget their passwords, they can request a password reset link via e-mail.
   
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

## Contribute to repository

1. **Fork the Repository** 🍴:
   To get started, click the "Fork" button in the top right corner of the repository page. This will create your copy of the project under your GitHub account. Yay, you have your own fork now!

2. **Clone the Repository** 📂:
   After forking, it's time to bring the code to your computer. Open your terminal and run the following command (don't forget to replace `<your_username>` with your actual GitHub username):

   ```bash
   git clone https://github.com/rajatrawal/django-auth-template.git
   ```

   You now have a local copy of the repository.

3. **Create a New Branch** 🌱:
   Let's create a branch for your contributions. This helps you keep your work separate from the main codebase. Use a descriptive name for your branch, like "my-contribution" or something else creative!

   ```bash
   cd django-auth-template
   git checkout -b my-contribution
   ```

4. **Make Your Awesome Changes** 🚀:
   Now comes the exciting part! Open up the project in your favorite code editor and make the desired changes. For "django-auth-template," focus on enhancing or adding features related to Django authentication.

5. **Test Your Changes** ✔️:
   Before you get too excited, it's essential to ensure that your changes work as expected. Run any tests provided in the project, and conduct manual testing if needed. Let's make sure everything is smooth sailing!

6. **Commit Your Work** 💬:
   Great job on the changes! Now, let's save them. Use the following commands to commit your work with a meaningful message:

   ```bash
   git add .
   git commit -m "Add feature X"  # Replace with a descriptive message
   ```

7. **Share Your Contributions** 💌:
   Time to push your work to your forked repository on GitHub:

   ```bash
   git push origin my-contribution
   ```

8. **Create a Pull Request** 🔗:
   Head over to the original repository (https://github.com/rajatrawal/django-auth-template). You'll notice a green button that says "Compare & pull request." Click it to create a pull request (PR) from your branch.

9. **Wait for Review** ⏳:
   Woohoo! You've submitted your contribution. Now, patiently wait for the maintainers to review your PR. They'll provide feedback if needed, and you may need to make some tweaks.

10. **Keep Your Branch Updated** 🔄:
   If the maintainers request changes, don't worry. Make the necessary updates, commit them, and push to your branch. The PR will automatically update.

11. **Merge Your Contribution** 🎉:
   Congratulations! Your contribution has been approved and merged into the main project. You've made the "django-auth-template" even better! 🎊



Happy contributing! 🌟
