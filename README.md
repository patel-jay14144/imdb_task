# IMDB Task

A minimalistic implementation of IMDB clone using Flask application

## Table of Contents

-   [Prerequisites](#prerequisites)
-   [Installation](#installation)
-   [Database Setup](#database-setup)
-   [Environment Variables](#environment-variables)
-   [Usage](#usage)

## Prerequisites

Before you begin, ensure you have met the following requirements:

-   Python (version 3.9)
-   Pipenv (for managing Python dependencies)
-   MySQL (version X.X)

## Installation

1. Clone this repository:

    ```shell
    git clone https://github.com/patel-jay14144/imdb_task.git
    ```

2. Install project dependencies using Pipenv:
    ```shell
    pipenv install
    ```

## Database Setup

1. Ensure that you have MySQL installed and running.

2. Create two databases for your project: one for development and one for testing. You can use the following commands in the MySQL shell:

    ```shell
    CREATE DATABASE imdb;
    CREATE DATABASE imdb_test;
    ```

## Environment Variables

Update the .env file with your database credentials:

```.env
FLASK_APP=app.py
FLASK_DEBUG=1
SQLALCHEMY_DATABASE_URI=mysql+pymysql://username:password@localhost:3306/imdb
SQLALCHEMY_DATABASE_URI_TEST=mysql+pymysql://username:password@localhost:3306/imdb_test
JWT_SECRET_KEY=some-randomly-generated-string
```

Replace username and password with your MySQL credentials.

## Usage

Refer Makefile to ease out the usage. Some examples are given below

### Running Server:

```bash
make run
```

### Running Tests:

```bash
make test
```

### Create New DB migrations after changes in Flask-SQLAlchemy models:

```bash
make db-makemigrations
```

### Apply DB Migrations:

```bash
make db-upgrade
```
