#!/usr/bin/env bash

echo "Installing dependencies..."

pip install django
pip install djangorestframework
pip install django-cors-headers
pip install mysqlclient
pip install Pillow

echo "Relocating Files..."
for file in "__init__.py" "settings.py" "urls.py" "wsgi.py";
do
    if test -f PairWise/$file;
    then
	cp PairWise/$file ./
        rm -f PairWise/$file
    fi
done

if test -f ./manage.py;
then
    rm -f ./manage.py
fi

echo "Initializing project..."
django-admin startproject PairWise .

for file in "__init__.py" "settings.py" "urls.py" "wsgi.py";
do
    if test -f ./$file;
    then
	cp ./$file PairWise
        rm -f ./$file
    fi
done
