# Cloud Storage Web App

## Steps to follow to make it able to run in your local

### Activate Virtual environment

```
python -m venv .venv/

Windows PowerShell: ./.venv/scripts/Activate.ps1

Unix Bash Shell: source ./.venv/bin/activate
```

### Install the dependencies.

```
pip install -r requirements.txt
```

### assign environment variables

assign variables for SECRET_KEY and DEBUG in .env file inside cloudVideo

### make Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### Run the dev server

```
python manage.py runserver
```
