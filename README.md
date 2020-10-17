# Museu da Pessoa Backend 

The Museu da Pessoa backend is part of the Museu da Pessoa project and is responsible for saving the users' data such as name, email, text, audio and video

## Installation
1. Download the Museu da Pessoa backend repository: ```https://github.com/Museu-da-Pessoa-XP/backend.git```

2. On the terminal, access the repository directory: ```cd backend```

3. Run ```pip3 install -r requirements.txt```

4. Execute ```python3 manage.py makemigrations``` and ```python3 manage.py migrate```

In order to run the project, execute ```python3 manage.py runserver```

## Using as an administrator
2. Create a superuser on Django, as explained [here.](https://docs.djangoproject.com/en/1.8/intro/tutorial02/#creating-an-admin-user)

3. Log into the [Django administration](http://127.0.0.1:8000/admin/login/?next=/admin/) by using the superuser you created.  

4. Now you can create, edit and remove user and historia objects.  