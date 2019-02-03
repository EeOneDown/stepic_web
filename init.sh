#!/usr/bin/env bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements 

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/gunicorn-django.conf
sudo /etc/init.d/gunicorn restart
sudo gunicorn -c hello.py -b 0.0.0.0:8080 hello:app
sudo gunicorn -c gunicorn-django.conf -b 0.0.0.0:8000 ask.wsgi:application
