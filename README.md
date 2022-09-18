# Company API

This is a simple API used to manage company data

## Table of Contents

1. [Problem Statement Code](#problem-statement-code)
2. [Features](#features)
3. [Technology Stack to be used](#technology-stack-to-be-used)
4. [GitHub Repository Structure](#github-repository-structure)
5. [Getting Started](#getting-started)
    1. [Fork, clone locally and create a branch](#fork-clone-locally--create-a-branch)
    1. [Setting Environment First Time](#setting-environment-first-time)
        1. [Basic Requirements](#basic-requirements)
        1. [Creating Virtual Environment](#creating-virtual-environment)
        1. [Installing Requirements](#installing-requirements)
        1. [Migrating Database](#migrating-database)
        1. [Create Superuser](#create-superuser)
    1. [Starting Development Server](#starting-development-server)
    1. [Leaving the virtual environment](#leaving-the-virtual-environment)
    1. [Update requirements file](#update-requirements-file-critical)
    1. [Update Database](#update-database)
6. [API Reference](#api-reference)

## Features

1. JWT Authentication.
2. Create a Company.
3. Create a Team (Should have company ID in path).
4. Get Company object from ID.
5. Search company by name.
6. Get All teams (Return all teams as an array grouped within company object)

## Technology Stack to be used:

-   **Backend**: Django, Django Rest Framework
-   **IDE**: VS Code
-   **API Testing & Documentation**: Postman, Swagger
-   **Version Control**: Git and GitHub
-   **Database**: SQLite
-   **Containerization**: Docker

### Getting Started

### Fork, clone locally & create a branch

Fork [Jan Dhan Darshak Backend](https://github.com/rudrakshi99/Jan-Dhan-Darshak) repository and clone at your local

-   Fork and Clone the repo using

```
$ git clone https://github.com/rudrakshi99/Jan-Dhan-Darshak.git
```

### Setting Environment First Time

#### Basic Requirements

1. [Python](https://www.python.org/downloads/)
1. [pip](https://pip.pypa.io/en/stable/installation/)

#### Creating [Virtual Environment](https://docs.python.org/3/library/venv.html)

A virtual environment is a tool that helps keep dependencies required and the project isolated. If you wish to install a new library and write

```
pip install name_of_library
```

on the terminal without activating an environment, all the packages will be installed globally which is not a good practice if you’re working with different projects on your computer.

If this sounds a bit complicated, don’t worry so much because a virtual environment is just a directory that will contain all the necessary files for our project to run.

**Installing venv (required once)**

**Windows**

```
py -m pip install --user virtualenv
py -m venv env
```

**Linux**

```
python3 -m pip install --user virtualenv
python3 -m venv env
```

You have to start virtual environment everytime you start new terminal -

**Windows**

Using gitbash

```
. env/Scripts/activate
```

Using Powershell

```
. env\Scripts\activate
```

**Linux**

```
source env/bin/activate
```

### For Quick start using Docker ( Docker should be installed in your machine)

```
sudo docker-compose up
```

-   your API will run on http://127.0.0.1:8000/ after running above command and you can jump to [API Reference](#api-reference) .

#### Installing Requirements

**Windows**

```
pip install -r requirements/base.txt
pip install -r requirements/local.txt
```

**Linux**

```
pip install -r requirements/base.txt
pip install -r requirements/local.txt
```

#### Migrating Database

**Windows**

```
py manage.py migrate
```

**Linux**

```
python3 manage.py migrate
```

#### Create Superuser

**Windows**

```
py manage.py createsupeser
```

**Linux**

```
python3 manage.py createsupeser
```

### Starting Development Server

**Windows**

```
py manage.py runserver
```

**Linux**

```
python3 manage.py runserver
```

### Leaving the virtual environment

```
deactivate
```

### Update requirements file (Critical)

If you have installed new dependency, the pip freeze command lists the third-party packages and versions installed in the environment.

**Windows**

```
pip freeze > requirements/local.txt
```

**Linux**

```
pip3 freeze > requirements/local.txt
```

### Update Database

Everytime you change db models, you need to run makemigrations and migrate to update on database.

**Windows**

```
py manage.py makemigrations
py manage.py migrate
```

**Linux**

```
python3 manage.py makemigrations
python3 manage.py migrate
```

##

## API Reference

### Get auth token

```http
  POST /api/token/
```

Headers

```
  {
 "Accept": "*/*",
 "Content-Type": "application/json"
}
```

Request body (JSON)

```
{
  "username":"hacktom",
  "password":"ayush123"
}
```

Response

```
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MzY3MDMzNCwiaWF0IjoxNjYzNDk3NTM0LCJqdGkiOiJjY2I5ODcwNzUyZTE0ODIyYWI5M2FhOTViZDg2MjU2NSIsInVzZXJfaWQiOjF9.maYq02xrWYb7_4nXCC9ev2lntWOnJZ7YEgyTbNrhEj4",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzNTAxMTM0LCJpYXQiOjE2NjM0OTc1MzQsImp0aSI6ImQ4MWZiNzJiNzNmMTQ3M2NhNTUzNzFmZjcwNjk4MDNjIiwidXNlcl9pZCI6MX0.B0mhY7fDHqkxzyC5EEICEYk-pAZJfUOI_V7TwC7yBlI"
}
```

### Create Company

```http
  POST /api/company/
```

Headers :

```

  {
 "Accept": "*/*",
 "Authorization": `Bearer ${Token}`,
 "Content-Type": "application/json"
}
```

Request body :

```
{
  "company_name":"Respo",
  "company_ceo":"hacktom",
  "company_address":"shkb",
  "inception_date":"2022-12-12"
}
```

Response :

```
{
  "data": {
    "uuid": "5b1f3676-9fb7-4910-85ac-2e33e64626cb",
    "company_name": "Respo",
    "company_ceo": "hacktom",
    "company_address": "shkb",
    "inception_date": "2022-12-12"
  },
  "success": "True"
}
```

### Create Team

```http
  POST /api/team/?id=<company_id>
```

Headers :

```

  {
 "Accept": "*/*",
 "Authorization": `Bearer ${Token}`,
 "Content-Type": "application/json"
}
```

Query Parameter
| Parameter | Type | Description |
| :-------- | :------- | :------------------------- |
| `id` | `string` | **Required**. company_id |

Request body :

```
{
  "team_lead_name":"parth"
}
```

Response :

```
{
  "data": {
    "uuid": "6e8f8ca7-bdae-41d6-9a92-f34ac43f003c",
    "team_lead_name": "parth",
    "company": "5b1f3676-9fb7-4910-85ac-2e33e64626cb"
  },
  "success": "True"
}
```

### Get company by company name

```http
  POST /api/company_detail/
```

Headers :

```

  {
 "Accept": "*/*",
 "Authorization": `Bearer ${Token}`,
 "Content-Type": "application/json"
}
```

Request body :

```
{
  "company_name":"Respo"
}
```

Response :

```
{
  "data": [
    {
      "uuid": "5b1f3676-9fb7-4910-85ac-2e33e64626cb",
      "company_name": "Respo",
      "company_ceo": "hacktom",
      "company_address": "shkb",
      "inception_date": "2022-12-12"
    }
  ],
  "success": "True"
}
```

### Get company by company id

```http
  GET /api/company_detail/company_id=<company_id>
```

Headers :

```

  {
 "Accept": "*/*",
 "Authorization": `Bearer ${Token}`,
}
```

Response :

```
{
  "data": {
    "uuid": "5b1f3676-9fb7-4910-85ac-2e33e64626cb",
    "company_name": "Respo",
    "company_ceo": "hacktom",
    "company_address": "shkb",
    "inception_date": "2022-12-12"
  },
  "success": "True"
}
```

### Get All teams (Return all teams as an array grouped within company object)

```http
  GET /api/team/
```

Headers :

```
  {
 "Accept": "*/*",
 "Authorization": `Bearer ${Token}`,
}
```

Response :

```
{
  "data": [
    {
      "company_name": "Respo",
      "company_ceo": "hacktom",
      "company_address": "shkb",
      "inception_date": "2022-12-12",
      "teams": [
        {
          "uuid": "6e8f8ca7-bdae-41d6-9a92-f34ac43f003c",
          "team_lead_name": "parth",
          "company": "5b1f3676-9fb7-4910-85ac-2e33e64626cb"
        }
      ]
    }
  ],
  "success": "True"
}
```

![Uses Git](https://forthebadge.com/images/badges/uses-git.svg)
![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)
![Built with love](https://forthebadge.com/images/badges/built-with-love.svg)
