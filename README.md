# Museu da Pessoa Backend 

The Museu da Pessoa backend is part of the Museu da Pessoa project and is responsible for saving the users' data such as name, email, text, audio and video

[![Build Status](https://travis-ci.org/Museu-da-Pessoa-XP/backend.svg?branch=develop)](https://travis-ci.org/Museu-da-Pessoa-XP/backend)

## Install docker on Linux (ubuntu flavors)
```shell
sudo apt-get update
sudo apt-get install docker
sudo apt-get install docker-compose
```
## Clone backend repository and changing to the right branch
```shell
git clone https://github.com/Museu-da-Pessoa-XP/backend.git
cd backend
git checkout develop
git pull
```

## Start the Postgres and PGAdmin
```shell
docker-compose up -d
```

## Check the containers status
```shell
docker ps
```
You must have 3 containers running, just like this:
```shell
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                           NAMES
0e236fff79a3        dpage/pgadmin4      "/entrypoint.sh"         3 seconds ago       Up 2 seconds        443/tcp, 0.0.0.0:8080->80/tcp   pgadmin
3078fe719194        backend_backend     "bash -c 'python3 ma…"   3 seconds ago       Up 2 seconds        0.0.0.0:8000->8000/tcp          backend
62a51038295c        postgres            "docker-entrypoint.s…"   3 seconds ago       Up 2 seconds        0.0.0.0:5432->5432/tcp          database
```

## Using Django administration
1. Create a superuser on Django, as explained [here.](https://docs.djangoproject.com/en/1.8/intro/tutorial02/#creating-an-admin-user)
2. Log into the [Django administration](http://127.0.0.1:8000/admin/login/?next=/admin/) by using the superuser you created.  
3. Now you can create, edit and remove user and historia objects.  


## Access the database administration
<p>If you want to o view/edit the database, configure a new connection on <b>PgAdmin</b>:</p>

- Open your web-browser (firefox, chrome) on URL: <a href="http://localhost:8080">http://localhost:8080</a>
- Use the follow credentials:
  - <b>User:</b> diego.morais@usp.br
  - <b>Password:</b> Museu@2020 
- Righ click on <b>Servers</b>, Create > Server...
- Fill the <b>General</b> tab with the follow information:
  - <b>Name:</b> Museu-database
  - Fill the <b>Connection</b> tab with the follow information:
  - <b>Host:</b> database
  - <b>Port:</b> 5432
  - <b>Maintenance database:</b> postgres
  - <b>Username:</b> postgres
  - <b>Password:</b> Museu@2020
- Click on <b>Save</b>
