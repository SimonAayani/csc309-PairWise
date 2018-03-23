#!/usr/bin/env bash

PROJECT_DIR="PairWise_Server"

echo "Installing dependencies..."

pip install django==2.0.2
pip install djangorestframework
pip install django-cors-headers
pip install mysqlclient
pip install Pillow

echo "Relocating Files..."
for file in "__init__.py" "settings.py" "urls.py" "wsgi.py";
do
    if test -f $PROJECT_DIR/$file;
    then
        cp $PROJECT_DIR/$file ./
        rm -f $PROJECT_DIR/$file
    fi
done

if test -f ./manage.py;
then
    rm -f ./manage.py
fi

echo "Initializing project..."
django-admin startproject $PROJECT_DIR .

for file in "__init__.py" "settings.py" "urls.py" "wsgi.py";
do
    if test -f ./$file;
    then
        cp ./$file $PROJECT_DIR
        rm -f ./$file
    fi
done
