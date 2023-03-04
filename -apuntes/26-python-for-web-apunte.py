# Python for Web
# Python is a general purpose programming language and it can be used for many places. In this section, we will see how we use Python for the web. There are many Python web frame works. Django and Flask are the most popular ones. Today, we will see how to use Flask for web development.

# Flask
# Flask is a web development framework written in Python. Flask uses Jinja2 template engine. Flask can be also used with other modern front libraries such as React.

# If you did not install the virtualenv package yet install it first. Virtual environment will allows to isolate project dependencies from the local machine dependencies.

# Folder structure
# After completing all the step, your project file structure should look like this:

# ├── Procfile
# ├── app.py
# ├── env
# │   ├── bin
# ├── requirements.txt
# ├── static
# │   └── css
# │       └── main.css
# └── templates
#     ├── about.html
#     ├── home.html
#     ├── layout.html
#     ├── post.html
#     └── result.html

# Setting up your project directory
# Follow the following steps to get started with Flask.

# Step 1: install virtualenv using the following command.
# pip install virtualenv

# Step 2:
# mkdir python_for_web
# cd python_for_web/
# python -m venv venv
# venv\Scripts\activate
# (env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
# (env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip install Flask
# (env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
# Click==7.0
# Flask==1.1.1
# itsdangerous==1.1.0
# Jinja2==2.10.3
# MarkupSafe==1.1.1
# Werkzeug==0.16.0
# (env) asabeneh@Asabeneh:~/Desktop/python_for_web$

# We created a project director named python_for_web. Inside the project we created a virtual environment venv which could be any name but I prefer to call it venv. Then we activated the virtual environment. We used pip freeze to check the installed packages in the project directory. The result of pip freeze was empty because a package was not installed yet.

# Now, let's create app.py file in the project directory and write the following code. The app.py file will be the main file in the project. The following code has flask module, os module.


# Creating routes
# The home route.