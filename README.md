![](https://img.shields.io/github/license/regiapriandi012/plagiarism-checker-flask)
![](https://img.shields.io/github/v/release/regiapriandi012/plagiarism-checker-flask)
![](https://github.com/regiapriandi012/plagiarism-checker-flask/actions/workflows/main.yml/badge.svg)
![](https://github.com/regiapriandi012/plagiarism-checker-flask/actions/workflows/python-app.yml/badge.svg)
![](https://github.com/regiapriandi012/plagiarism-checker-flask/actions/workflows/codeql.yml/badge.svg)
![](https://github.com/regiapriandi012/plagiarism-checker-flask/actions/workflows/dependency-review.yml/badge.svg)
![](https://github.com/regiapriandi012/plagiarism-checker-flask/actions/workflows/docker-image.yml/badge.svg)
![](https://github.com/regiapriandi012/plagiarism-checker-flask/actions/workflows/docker-publish.yml/badge.svg)


# Plagiarism Checker Flask
Plagiarism Checker Flask application is an application built using the Python programming language and using the flask framework technology. This application was built with the aim of assisting in checking the plagiarism of a document or writing. Praise God, this application can be released with the latest version ![](https://img.shields.io/github/v/release/regiapriandi012/plagiarism-checker-flask).

## Requirements Package
```
beautifulsoup4==4.11.1
click==8.1.3
Flask==2.2.2
google==3.0.0
importlib-metadata==5.0.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
PyPDF2==2.11.1
soupsieve==2.3.2.post1
typing-extensions==4.4.0
Werkzeug==2.2.2
zipp==3.10.0
```

## Algorithm
<p align="center">
<img width="604" alt="image" src="https://user-images.githubusercontent.com/69528812/204430811-de3edf9a-e384-4979-9394-adee8f182214.png">
</p>

## How to Use the App
  - #### Insert a Document or Write a Text
  <img width="944" alt="image" src="https://user-images.githubusercontent.com/69528812/201468315-fc0a91a0-d2d8-41f4-8b5a-85a765c47b81.png">
  
  - #### Wait for a Moment for a Result
  <img width="945" alt="image" src="https://user-images.githubusercontent.com/69528812/201468374-91ec77de-d694-425c-86a6-872a3640cf16.png">

## Clone Repository
```
$ git clone https://github.com/regiapriandi012/plagiarism-checker-flask.git
$ cd plagiarism-checker-flask
```

## Run the App
```
$ cd plagiarism-checker-flask
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ flask run
```
