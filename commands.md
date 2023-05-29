# Tools used

 - ubuntu 20.04 LTS
 - PyCharm
 - `MySQL` vi the `MySQL Workbench v8.0.32` tool
 - Python 3.8.10

# Useful commands

---
python3 manage.py migrate                   # Apply migrations
python3 manage.py makemigrations            # Create tables in the database
python3 manage.py runserver                 # Launch the server
python3 manage.py migrate <APP> zero        # Unapply migrations
python3 manage.py createsuperuser           # Create superuser for the admin panel
---
pip freeze > file_name                      # Create the requirements
pip install -r requirements.txt             # Download the requirements
python3 -m venv <environment_name>
source ../../<venv folder>/<environment_name>/bin/activate
---
python3 manage.py startapp <app_name>
django-admin startproject <project_name>
---
