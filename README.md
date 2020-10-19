# Backend - Postgres

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
git checkout devekop
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
You must have 2 containers running, like this:
```shell
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                           NAMES
7ae2b4012dd5        dpage/pgadmin4      "/entrypoint.sh"         5 seconds ago       Up 4 seconds        443/tcp, 0.0.0.0:8080->80/tcp   pgadmin
3e47966ab167        postgres            "docker-entrypoint.s…"   7 seconds ago       Up 5 seconds        0.0.0.0:5432->5432/tcp          database
```

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
 
