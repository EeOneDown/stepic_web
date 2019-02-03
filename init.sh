#!/usr/bin/env bash

sudo pip3 install -r requirements.txt

sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/test-wsgi
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django
sudo /etc/init.d/gunicorn restart
# sudo gunicorn -c test-wsgi -b 0.0.0.0:8080 hello:app &
# cd ask
# gunicorn -c ../etc/gunicorn-django.conf -b 0.0.0.0:8000 ask.wsgi:application
sudo gunicorn -c test-django -b 0.0.0.0:8000 ask.wsgi:application
