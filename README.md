This is an application for recording memories. The application supports authorization via social networks VK and Facebook. The project includes 2 applications app for auth by social networks and impression app. For start:
git clone https://github.com/darz10/PR
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Open browser: localhost:8000/login/
