# SPA-application: Comments


## Contents
1. [Dependencies](#dependencies-)
2. [Description](#description-)
3. [Instruction](#instruction-for-deploy-)

---
## Dependencies:
* Linux
* Postgresql-15
* Python (v 3.10)

---
## Description:

Easy application for create message and answer on them.

Pagination: split on 10 message higher level for page (answer to message not taken into account).

Display can be sorted by name, email and date(asc, desc).

"DB-diagram.png": database structure.

---

### Instruction for deploy:

1. Download this project: https://github.com/mertwec/spa_comments.git
2. Open directory 'spa_comments': `cd spa_comments/`

3. Initialize environment:
```commandline
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
4. Set environment variables: `vim .env`

You can set environment variables for customized configuration.

- You can specify your custom values inside `.env` file (recommended)
- Or export them directly to your shell environment (`export VAR=VALUE`)

#### values in environment:
* SECRET_KEY
* DEBUG (1 or 0, default=1 i.e.True)


* DB_USER (postgres username, default = "postgres")
* DB_PASSWORD (postgres password, default = "")
* DB_NAME (name database, default = 'SPA_database')


5. Create database:

Before install postgresql for your OS https://www.postgresql.org/download
    
    1) Enter to 'psql':  `sudo -u postgres psql`
    2) Create User (if need): `/# CREATE USER <DB_USER> WITH PASSWORD <DB_PASSWORD>;`
    3) Create database: `/# CREATE DATABASE <DB_NAME> OWNER <DB_USER>;
    4) Close psql: `\q`

6. Apply migrations
```commandline
python3 manage.py migrate
```
7. Create static files:
```commandline
python3 manage.py collectstatic
```
8. Start  test server:
```commandline
python3 manage.py runserver
```
