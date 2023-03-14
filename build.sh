#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt
python3 manage.py captcha_create_pool
