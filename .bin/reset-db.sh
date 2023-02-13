#!/bin/sh
rm -rf db.sqlite3
python manage.py migrate
python manage.py loaddata ./backend/books/fixture/user.json
python manage.py loaddata ./backend/books/fixture/master.json
