py -3.10 -m venv .venv
.venv\Scripts\activate
python -m pip install -U pip setuptools wheel
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py makemigrations scraper
python manage.py migrate
python manage.py runserver
