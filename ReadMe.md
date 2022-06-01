# Demo: Your Python URL Shortener
In this tutorial, you’ll build a URL shortener with Python and FastAPI. URLs can be extremely long and not user-friendly. This is where a URL shortener can come in handy. A URL shortener reduces the number of characters in a URL, making it easier to read, remember, and share.

By following this step-by-step project, you’ll build a URL shortener with Python and FastAPI. At the end of this tutorial, you’ll have a fully functional API-driven web app that creates shortened URLs that forward to target URLs.

In this tutorial, you’ll learn how to:

Create a REST API with FastAPI
Run a development web server with Uvicorn
Model an SQLite database
Investigate the auto-generated API documentation
Interact with the database with CRUD actions
Optimize your app by refactoring your code
This URL shortener project is for intermediate Python programmers who want to try out FastAPI and learn about API design, CRUD, and interaction with a database. To follow along, it’ll help if you’re familiar with the basics of handling HTTP requests. If you need a refresher on FastAPI, Using FastAPI to Build Python Web APIs is a great introduction.


# Project Overview
Your URL shortener Python project will provide API endpoints that are capable of receiving different HTTP request types. Each endpoint will perform an action that you’ll specify. Here’s a summary of your URL shortener’s API endpoints:

Endpoint	HTTP Verb	Request Body	Action
/	GET		Returns a Hello, World! string
/url	POST	Your target URL	Shows the created url_key with additional info, including a secret_key
/{url_key}	GET		Forwards to your target URL
/admin/{secret_key}	GET		Shows administrative info about your shortened URL
/admin/{secret_key}	DELETE	Your secret key	Deletes your shortened URL

# Prerequisites
To get the most out of this tutorial, you should be comfortable with the following concepts:

Object-Oriented Programming (OOP) in Python 3
Working with JSON data
Python Type Checking
Handling HTTP requests


# Dependencies
FastAPI web framework to build the API
# fastapi==0.75.0 

# uvicorn==0.17.6
To run the API, you need a web server. That’s what uvicorn is for. Uvicorn is a web server implementation for Python that provides an Asynchronous Server Gateway Interface (ASGI). Web Server Gateway Interfaces (WSGI) specify how your web server communicates with your web application.

# sqlalchemy==1.4.32
SQLAlchemy is a Python SQL tool kit that helps you communicate with your database. Instead of writing raw SQL statements, you can use SQLAlchemy’s Object-Relational Mapper (ORM). The ORM provides a more user-friendly way for you to declare the interactions of your application and the SQLite database that you’ll use.

# Environment Variable 
# python-dotenv==0.19.2
The python-dotenv package helps you read key-value pairs from an external file and set them as environment variables.

# URLs Validator
# validators==0.18.2
This package helps validate a URL