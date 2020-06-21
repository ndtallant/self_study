# Django Postgres App

1. Create the Dockerfile, an explanation is in the file.

2. Create a `docker-compose.yml` in your project directory.
The `docker-compose.yml` file describes the services that make your app.
In this example those services are a web server and database.
The compose file also describes which Docker images these services use,
how they link together, any volumes they might need mounted inside the containers.
Finally, the docker-compose.yml file describes which ports these services expose.

3. Run:
```
sudo docker-compose run web django-admin startproject composeexample .
```

4. Change `settings.py` so the database description matches the compose file.

5. Run `docker-compose up` and watch the magic.
