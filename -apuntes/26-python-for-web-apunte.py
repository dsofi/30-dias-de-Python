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
'''
# let's import the flask
from flask import Flask
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return '<h1>About us</h1>'


if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
'''

# To run the flask application, write python app.py in the main flask application directory.
# After you run python app.py check local host 5000.
# Let us add additional route. Creating about route

# Now, we added the about route in the above code. How about if we want to render an HTML file instead of string? It is possible to render HTML file using the function render_templae. Let us create a folder called templates and create home.html and about.html in the project directory. Let us also import the render_template function from flask.



# Creating templates
# Create the HTML files inside templates folder.

# home.html (return render_template('home.html'))
# about.html (return render_template('about.html'))

# As you can see to go to different pages or to navigate we need a navigation. Let's add a link to each page or let's create a layout which we use to every page.
'''
<ul>
  <li><a href="/">Home</a></li>
  <li><a href="/about">About</a></li>
</ul>
'''


# Now, we can navigate between the pages using the above link. Let us create additional page which handle form data. You can call it any name, I like to call it post.html.

# We can inject data to the HTML files using Jinja2 template engine.


# Creating a layout
# In the template files, there are lots of repeated codes, we can write a layout and we can remove the repetition. Let's create layout.html inside the templates folder. After we create the layout we will import to every file.

# Serving Static File
# Create a static folder in your project directory. Inside the static folder create CSS or styles folder and create a CSS stylesheet. We use the url_for module to serve the static file.

# layout.html

# Now, lets remove all the repeated code in the other template files and import the layout.html. The href is using url_for function with the name of the route function to connect each navigation route.

# home.html
# about.html


# Request methods, there are different request methods(GET, POST, PUT, DELETE) are the common request methods which allow us to do CRUD(Create, Read, Update, Delete) operation.

# In the post, route we will use GET and POST method alternative depending on the type of request, check how it looks in the code below. The request method is a function to handle request methods and also to access form data. app.py


# Deployment
# Creating Heroku account
# Heroku provides a free deployment service for both front end and fullstack applications. Create an account on heroku and install the heroku CLI for you machine. After installing heroku write the following command

# Login to Heroku
# asabeneh@Asabeneh:~$ heroku login
# heroku: Press any key to open up the browser to login or q to exit:
# Let's see the result by clicking any key from the keyboard. When you press any key from you keyboard it will open the heroku login page and click the login page. Then you will local machine will be connected to the remote heroku server. If you are connected to remote server, you will see this.

# asabeneh@Asabeneh:~$ heroku login
# heroku: Press any key to open up the browser to login or q to exit:
# Opening browser to https://cli-auth.heroku.com/auth/browser/be12987c-583a-4458-a2c2-ba2ce7f41610
# Logging in... done
# Logged in as asabeneh@gmail.com
# asabeneh@Asabeneh:~$
# Create requirements and Procfile
# Before we push our code to remote server, we need requirements

# requirements.txt
# Procfile
# (env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
# Click==7.0
# Flask==1.1.1
# itsdangerous==1.1.0
# Jinja2==2.10.3
# MarkupSafe==1.1.1
# Werkzeug==0.16.0
# (env) asabeneh@Asabeneh:~/Desktop/python_for_web$ touch requirements.txt
# (env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze > requirements.txt
# (env) asabeneh@Asabeneh:~/Desktop/python_for_web$ cat requirements.txt
# Click==7.0
# Flask==1.1.1
# itsdangerous==1.1.0
# Jinja2==2.10.3
# MarkupSafe==1.1.1
# Werkzeug==0.16.0
# (env) asabeneh@Asabeneh:~/Desktop/python_for_web$ touch Procfile
# (env) asabeneh@Asabeneh:~/Desktop/python_for_web$ ls
# Procfile          env/              static/
# app.py            requirements.txt  templates/
# (env) asabeneh@Asabeneh:~/Desktop/python_for_web$
# The Procfile will have the command which run the application in the web server in our case on Heroku.

# web: python app.py
# Pushing project to heroku
# Now, it is ready to be deployed. Steps to deploy the application on heroku

# git init
# git add .
# git commit -m "commit message"
# heroku create 'name of the app as one word'
# git push heroku master
# heroku open(to launch the deployed application)