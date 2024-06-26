﻿# Create-comments
A small application that gives you the ability to leave comments with pictures and files and also has the ability to respond to comments that are displayed in a cascading style

## DB structure
![db_structure](static/img/db_structure.jpg)

## Check it out
[Create comments on deployed to Render](https://create-comments.onrender.com)

## Getting Started
Before you begin, make sure you have the following tools and technologies installed:

- Python (>=3.6)
- Django

Install dependencies:
```shell
pip install -r requirements.txt
```

## Installing/GitHub

```
git clone https://github.com/Yevheniia-Ilchenko/Create-comments
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```
## Installing/DockerHub

Login into the Docker:
```
docker login
```
Pull the project:

```angular2html
docker pull evgeniiailchenko/create_comments-app
```


## .env file
Open file .env.sample and change environment variables to yours. Also rename file extension to .env

## Run on local server
- Install PostgreSQL, create DB and User
- Connect DB
- Run:
```
python manage.py migrate
python manage.py runserver
```
## Run with Docker
Docker should be already installed

```
docker-compose up --build
```
## Stop server

```
docker-compose down
```
## Key Features:

* Comments Creation
  
![structure](static/img/comment_form_1.jpg)
* Upload Files
* Upload Images

![structure](static/img/comment_form_2.jpg)

* Pictures and files displayed in comments
* Reply for comments in cascade style
  
![structure](static/img/comment_list.jpg)


## Getting access
You can use following:

Test user

To use our application in test mode, use the following data for a test user:
- Username: test_user
- Password: 1qazcde3

superuser:
- Username: admin
- Password: 1qazcde3
