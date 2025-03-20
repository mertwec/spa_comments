# SPA-application: Comments

https://spa-comments.onrender.com

## Contents
- [SPA-application: Comments](#spa-application-comments)
  - [Contents](#contents)
  - [Dependencies:](#dependencies)
  - [Description:](#description)
    - [Instruction:](#instruction)
      - [values in environment:](#values-in-environment)

---
## Dependencies:
* Linux
* Postgresql-15
* Python (v 3.10)

---
## Description:

This is an easy-to-use application for creating messages and replying to them. In the 'text' field, you can use tags such as br, i, strong, code, and a. The application checks that tags are closed properly.

Comments can be submitted by both registered and unregistered users. Unregistered users need to enter their username, email address, and captcha to submit a comment.

*Only admin users can delete comments. The admin user login details are:


```commandline
login: pro
password: pro123456789
```

Pagination is set up so that messages are split into groups of 10 per page (excluding replies to messages).

You can sort the display by name, email, and date (ascending or descending order).

"DB-diagram.png": database structure.


---

### Instruction:

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
