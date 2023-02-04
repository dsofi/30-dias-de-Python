# Python PIP - Python Package Manager
# What is PIP ?
# PIP stands for Preferred installer program. We use pip to install different Python packages. Package is a Python module that can contain one or more modules or other packages. A module or modules that we can install to our application is a package. In programming, we do not have to write every utility program, instead we install packages and import them to our applications.

# Installing PIP
# If you did not install pip, let us install it now. Go to your terminal or command prompt and copy and paste this:
# pip install pip

# Check if pip is installed by writing
# pip --version

# Let us check some of the packages used in the Python community for different purposes. Just to let you know that there are lots of packages available for use with different applications.

# Installing packages using pip
# Let us try to install numpy, called numeric python. It is one of the most popular packages in machine learning and data science community.

# NumPy is the fundamental package for scientific computing with Python. It contains among other things:
##### a powerful N-dimensional array object
##### sophisticated (broadcasting) functions
##### tools for integrating C/C++ and Fortran code
##### useful linear algebra, Fourier transform, and random number capabilities
# pip install numpy

# Let us start using numpy. Open your python interactive shell, write python and then import numpy as follows:
""" 
>>> import numpy
>>> numpy.version.version
'1.20.1'
>>> lst = [1, 2, 3,4, 5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr * 2
array([ 2,  4,  6,  8, 10])
>>> np_arr  + 2
array([3, 4, 5, 6, 7])
>>> 
"""

# Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Let us install the big brother of numpy, pandas:

# pip install pandas
# import pandas

# Let us import a web browser module, which can help us to open any website. We do not need to install this module, it is already installed by default with Python 3. For instance if you like to open any number of websites at any time or if you like to schedule something, this webbrowser module can be used.

import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://github.com/dsofi',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)


# Uninstalling Packages
# If you do not like to keep the installed packages, you can remove them using the following command.
# pip uninstall packagename

# List of Packages
# To see the installed packages on our machine. We can use pip followed by list.
# pip list

# Show Package
# To show information about a package
# pip show packagename

# If we want even more details, just add --verbose
# pip show --verbose pandas


# PIP Freeze
# Generate installed Python packages with their version and the output is suitable to use it in a requirements file. A requirements.txt file is a file that should contain all the installed Python packages in a Python project.
# pip freeze

# The pip freeze gave us the packages used, installed and their version. We use it with requirements.txt file for deployment.

# Reading from URL
# By now you are familiar with how to read or write on a file located on you local machine. Sometimes, we would like to read from a website using url or from an API. API stands for Application Program Interface. It is a means to exchange structured data between servers primarily as json data. To open a network connection, we need a package called requests - it allows to open a network connection and to implement CRUD(create, read, update and delete) operations. In this section, we will cover only reading ore getting part of a CRUD.

# Let us install requests:
# pip install requests

# We will see get, status_code, headers, text and json methods in requests module:
### get(): to open a network and fetch data from url - it returns a response object
### status_code: After we fetched data, we can check the status of the operation (success, error, etc)
### headers: To check the header types
### text: to extract the text from the fetched response object
### json: to extract json data Let's read a txt file from this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.

import requests  # importing the request module

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page


# Let us read from an API. API stands for Application Program Interface. It is a means to exchange structure data between servers primarily a json data. An example of an API:https://restcountries.eu/rest/v2/all. Let us read this API using requests module.
url = 'https://restcountries.eu/rest/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries

# We use json() method from response object, if the we are fetching JSON data. For txt, html, xml and other file formats we can use text.


# Creating a Package
# We organize a large number of files in different folders and sub-folders based on some criteria, so that we can find and manage them easily. As you know, a module can contain multiple objects, such as classes, functions, etc. A package can contain one or more relevant modules. A package is actually a folder containing one or more module files. Let us create a package named mypackage, using the following steps:

# Create a new folder named mypacakge inside 30DaysOfPython folder Create an empty init.py file in the mypackage folder. Create modules arithmetic.py and greet.py

# As you can see our package works perfectly. The package folder contains a special file called init.py - it stores the package's content. If we put init.py in the package folder, python start recognizes it as a package. The init.py exposes specified resources from its modules to be imported to other python files. An empty init.py file makes all functions available when a package is imported. The init.py is essential for the folder to be recognized by Python as a package.



# Further Information About Packages
# Database

# SQLAlchemy or SQLObject - Object oriented access to several different database systems
# pip install SQLAlchemy
# Web Development

# Django - High-level web framework.
# pip install django
# Flask - micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
# pip install flask
# HTML Parser

# Beautiful Soup - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.
# pip install beautifulsoup4
# PyQuery - implements jQuery in Python; faster than BeautifulSoup, apparently.
# XML Processing

# ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the Standard Library
# GUI

# PyQt - Bindings for the cross-platform Qt framework.
# TkInter - The traditional Python user interface toolkit.
# Data Analysis, Data Science and Machine learning

# Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
# Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
# SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
# Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
# TensorFlow: is a machine learning library built by Google.
# Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.
# Network:

# requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)
# pip install requests


