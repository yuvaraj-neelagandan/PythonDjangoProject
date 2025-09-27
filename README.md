
# 🧾 Employee Manager (Django + Heroku + HTML)

## 📌 Features
- Full CRUD REST API for Employees
- Salary filter API with optional param
- HTML frontend with JS
- Heroku-ready deploy (PostgreSQL)

## 🧪 Local Setup

```bash
pip install -r requirements.txt
cp .env.sample .env
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## ☁️ Heroku Deploy

```bash
heroku login
heroku create your-app-name
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set SECRET_KEY=your-secret
git push heroku master
heroku run python manage.py migrate
heroku open
```

## 🌐 Frontend (index.html)

Change the JS `url` to match your Heroku backend URL.

