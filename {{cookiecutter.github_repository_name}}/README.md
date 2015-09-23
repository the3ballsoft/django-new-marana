
#{{cookiecutter.github_repository_name}}


# Prerequisites 
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env --no-site-packages --distribute -p /usr/local/bin/python3
source env/bin/activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize the git repository

```bash
git init
git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}.git
```

Migrate, create a superuser, and run the server:

```bash
python {{cookiecutter.app_name}}/manage.py migrate
python {{cookiecutter.app_name}}/manage.py createsuperuser
python {{cookiecutter.app_name}}/manage.py runserver
```

