# SPA-приложение: Комментарии


## Contents
1. [Dependencies](#dependencies-)
3. [Setup environment](#initialize-environment)
4. [Setup database](#create-database)
5. [Start server](#start-server)


---
## Dependencies:
* Postgresql
* Python (v 3.10)

---
## Initialize environment
```commandline
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---
## Set environment variables
You can set environment variables for customized configuration.

- You can specify your custom values inside `.env` file
- Or export them directly to your shell environment (`export VAR=VALUE`)

#### values in environment:
* SECRET_KEY
* DEBUG


* DB_USER (postgres username, default = "postgres")
* DB_PASSWORD (postgres password, default = "")
* DB_NAME (name database, default = 'SPA_database')

---
## Create database
Before install postgresql for your OS https://www.postgresql.org/download
1) Enter to 'psql':  `sudo -u postgres psql`
2) Create User (if need): `/# CREATE USER <DB_USER> WITH PASSWORD <DB_PASSWORD>;`
3) Create database: `/# CREATE DATABASE <DB_NAME> OWNER <DB_USER>;`











---
## Start server
* run test server
```commandline
./manage.py runserver
```
