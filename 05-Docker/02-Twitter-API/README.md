# Twitter API - Containerization

The goal of this exercise is to continue the work on Wednesday's and Thursday's exercises: **Twitter API**.

We have already set up an web application and a database, and today we will focus on containerizing this stack locally, to be able to develop on it, and run our tests inside containers.

---

## 0. Setup

We're going to continue from yesterday's correction :
:point_right: [github.com/ssaunier/twitter-api](https://github.com/ssaunier/twitter-api)

Start from the following code (using the `docker` branch):

```bash
cd ~/code/<user.github_nickname>
git clone git@github.com:ssaunier/twitter-api.git twitter-api-docker
cd twitter-api-docker
git checkout docker  # get these branch before changing the remote
git remote rm origin
```

Go to [github.com/new](https://github.com/new) and create a _public_ repository under your _personal_ account, name it `twitter-api-docker`.

```bash
git remote add origin https://github.com/<user.github_nickname>/twitter-api-docker.git
git push -u origin master
```

---

## 1. Sanity check - non-containerized stack

The stack is not containerized yet. But let's make a sanity check to verify that everything is working. This also acts as a reminder of the two previous days on this challenge !

### 1.a. Install the packages locally

```bash
pipenv install --dev
```

### 1.b. Make sure the tests are passing locally

```bash
pipenv run nosetests
```

### 1.c. Make sure the web server can be run + show Swagger documentation

```bash
FLASK_ENV=development pipenv run flask run
```

:point_right: Go to [localhost:5000](http://localhost:5000/). Is everything fine ? Do you see the Swagger documentation ?

---

## 2. Containerization - development mode

When containerizing our app, we generally do not use `pipenv` anymore. We prefer having the requirements listed in a static file (typically named `requirements.txt`) and use `pip` directly (as we do not need a virtual environment) to install them.

We say "generally", because with Docker you can install and build pretty much anything, so we _could_ still use it. But here, we will use the common `requirements.txt` method.

:point_right: Run the following commands:

```
pipenv lock --requirements > requirements.txt
```

and

```
pipenv lock --requirements --dev > requirements-dev.txt
```

After running them, these files should have been created in your folder and filled in with python dependencies.

---

### 2.1 Dockerfile - Flask app

Let's first Dockerize our Flask app: build an image, run a container and check all is fine.
And for simplicity, **let's adopt a pure "development" point of view**: we build an image for development use, and generalize to other environments (test, CI, production) down the road. But let's start small !

:point_right: Create an empty Dockerfile

```bash
touch Dockerfile
```

:point_right: Copy paste the following code in it, and save it

```dockerfile
FROM python:3.8-alpine as base

RUN apk update && apk add postgresql-dev gcc musl-dev
RUN pip install --upgrade pip

WORKDIR /code
COPY . /code

RUN pip install -r requirements-dev.txt

ENV DATABASE_URL postgres://localhost/twitter_api_flask
ENV FLASK_APP wsgi.py
ENV FLASK_ENV development

CMD ["flask", "run", "--host", "0.0.0.0"]
```

Do you understand the instructions ? If we decompose them, we see that:

* we start from the Python 3.8 image, and more specifically its `alpine` version. Alpine Linux is a Linux distribution known for its light weight, but still complete toolbox
* we install a few packages required for our image to build
* we create a workspace directory (in the containers that will be run) called `/code`
* we copy our local code folder into this container workspace directory
* we install the requirements (in development mode for this challenge)
* we setup some environment variables for the container to run properly
* we setup a command to be run when the container is run

🤔 Why do we have --host 0.0.0.0 in the `CMD` instruction ?

<details><summary markdown='span'>View solution</summary>

We do not want to only bind to `localhost` interface as we did before: we bind to `0.0.0.0` so the container can be accessible from the outside (especially accessible from your docker host, which is your laptop !)

</details>


:point_right: Now, build this image and tag it as `twitter-api`

<details><summary markdown='span'>Hint</summary>

There is an example for building and tagging an image in the same command, in the previous exercise (`Docker-101`).

</details>

<details><summary markdown='span'>View solution</summary>

```bash
docker build -t twitter-api .
```

</details>

Done ? Perfect ! Now let's run a container from this image, and check that our application is working.
A few specs for this run:

* name it `twitter-api-docker`
* you need to map a host port to the container port of your application, in order to access it from your host: add the `-p 5000:5000` option to your command. This way, the app will run in the container on port 5000, and you will be able to access it on your host (your machine) on port 5000 as well.
* add the `--rm` option to your `docker run` command to automatically remove the container once it exits.

<details><summary markdown='span'>View solution</summary>

```bash
docker run --name twitter-api -p 5000:5000 --rm twitter-api
```

</details>

You now have a container running.

:point_right: Let's check http://localhost:5000/ to see if it worked: does it ?

<details><summary markdown='span'>View solution</summary>

It should ! If not, double check the command you have run and if the problem still persists, please ask a TA !

</details>


:point_right: What happens with http://localhost:5000/tweets ? Why ?

<details><summary markdown='span'>View solution</summary>

When we hit this endpoint, it's crashing. Indeed, we are trying to make a call to our database, but it's not set up ! So our Flask app would not find its database ready for new connections, and it raises a `sqlalchemy.exc.OperationalError` exception.

So let's setup our database - and dockerize it at the same time to make the development and testing flow easier !

</details>

:point_right: Hit `CTRL-C` to stop and remove your container.

---

### 2.2 Containerize our database service

We need to add a DB and we will use `docker-compose` for this.
We have seen in lecture that `docker-compose` was used to define multiple services, and bring up the application stack with the `docker-compose up` command.

:point_right: Once again, let's start small, and create an empty `docker-compose.yml` file.

```bash
touch docker-compose.yml
```

:point_right: Copy and paste the following content in it: here we define a single service: `web`, for our Flask app. It is mostly based on the Dockerfile previously created, through the `build` keyword.

```yaml
version: '2.2'

services:
  web:
    build: .
    volumes:
      - .:/code
    ports:
      - 5000:5000
```

:point_right: Bring up the stack by running

```bash
docker-compose up
```

:point_right: Browse to http://localhost:5000

Here, we have not changed much, as we only have one service (web) in our `docker-compose.yml` file, that relies on our previously defined `Dockerfile`.
So in a way, we have only changed - so far - the way to run our container ! But we will do more now ...

:point_right: You can now exit your container using `CTRL-C`


Remember that the idea is to add a database service to it. So let's add our Postgres database ! For this, we are going to do the following:

a. update our `Dockerfile` accordingly
b. adjust our `docker-compose.yml` to account for the database service


#### 2.2.a Update our existing Dockerfile
:point_right: Update your `Dockerfile` with the following:

```dockerfile
FROM python:3.8-alpine as base

RUN apk update && apk add postgresql-dev gcc musl-dev
RUN pip install --upgrade pip

WORKDIR /code
COPY . /code

RUN pip install -r requirements-dev.txt

ENV FLASK_APP wsgi.py
```

#### 2.2.b Adjust our docker-compose.yml
:point_right: Update your `docker-compose.yml` file with the following:

```yaml
version: '2.2'

services:
  db:
    image: postgres:12-alpine
    container_name: db
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=flask_password
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  web:
    build: .
    container_name: web
    depends_on:
      db:
        condition: service_healthy
    command: flask run
    volumes:
      - .:/code
    ports:
      - 5000:5000
    environment:
      - DATABASE_URL=postgres://postgres:flask_password@db:5432/twitter_api_flask
      - FLASK_RUN_HOST=0.0.0.0
      - FLASK_ENV=development

volumes:
  postgres_data:
```

The idea here it to migrate what is _configurable_ from the `Dockerfile` into the `docker-compose.yml`, and only keep what is static (such as packages, dependencies definition) in the `Dockerfile`.

So now we have two services: `web` and `db`, that are respectively based on our custom image (created earlier through the `Dockerfile`), and the `postgres` image.

👀 See the `volumes` keyword here ? In a few words - just to introduce the concept:

* In order to be able to save (persist) data and also to share data between containers, Docker came up with the concept of **volumes**
* Quite simply, volumes are directories (or files) that  live "outside" the container, on the host machine (in our case, your laptop)
* From the container, the volume acts like a folder which you can use to store and retrieve data. It is simply a _mount point_ to a directory on the host
* In other words: here the `/var/lib/postgresql/data/` directory from the `db` container "points towards" the `postgres_data` volume on your host. All the database data will end up in this volume
* **But why ?** 🤔 Well if you stop and remove your container, you do not want its persistent data to be lost as well. So it is kept safe on the docker host, and you can re-attach the volume to any new container you would like to run !



Let's perform a few initial steps to setup the containers and databases we will need:


:point_right: Bring up the stack (and run containers in the background): ```docker-compose up -d``` 🛠

:point_right: Let's create our databases for development and testing now
* connect to the `db` container: `docker exec -it db psql -U postgres`
* create databases for development and test environments: in the `psql` prompt, type:
  * `CREATE DATABASE twitter_api_flask;`
  * `CREATE DATABASE twitter_api_flask_test;`
  * Exit the `psql` prompt: `\q` + **Enter**
  
:point_right: Eventually, run your migrations: ```docker-compose run web python manage.py db upgrade```
  
⚠️ Note that is not something that we usually automate for **development** and **test** environments as we want to be able to play with migrations manually. But for **CI** and **production**, these commands would be scripted to be run programmatically. You would not have to manually enter the command and run it.

If you run `docker ps`, you should see two containers running: `web` and `db`.


Now our endpoints are fixed:

:point_right: Visit http://localhost:5000 and http://localhost:5000/tweets

<details><summary markdown='span'>View solution</summary>

You should see: the Swagger documentation as usual for the first endpoint, and an empty list for the second endpoint (you do not have any data yet !)

</details>

Some details about what just happened:

* Calling `docker-compose up` will launch `db` and `web`
* `web` depends on `db` to be up and healthy (see the `condition: service_healthy` ? It relies on `db`'s `healthcheck`)
* once `db` is up and healthy, `web` can be run
* our database is secured by a user/password, that Flask knows (we pass it throught the `DATABASE_URL` environment variable that you already know from yesterday)

⚠️ Note that we have **hard-coded** a dummy **database password** ("_flask_password_") here: we would of course do better going live (such as using an environment variable, or a secret from a Vault). But remember that we are industrializing our stack progressively: of course all our iterations are not perfect, but we are aiming at something robust in the end !

---

### 2.3 Interact using data

#### 2.3.a Add data using Postman !

* Open your Postman app

* Create some data: make a `POST` request to `http://localhost:5000/tweets`, with a JSON body:

```json
{
    "text": "Hey this is a new tweet!"
}
```

* Create another tweet (use the text you want, and send the request)

#### 2.3.b Check your data using the API

Now that you have some data in your database, check the list of tweets through the GET `tweets` endpoint: make a `GET` request to `http://localhost:5000/tweets`

#### 2.3.c Check your data using the database directly

Another way to see the data would be to connect to the **development** database directly.
That's convenient because you have a container for it.

:point_right: Similarly to what we did in the previous exercise, run:

```
docker exec -it db psql -U postgres twitter_api_flask
```

You will get a `psql` prompt where you can write SQL.

* :bulb: **Tip** typing `\d+` and hitting **Enter** will show you the list of available tables in the database
* Running `SELECT * FROM tweets;` would display all your data
* Exit the `psql` prompt: `\q` + **Enter**

---

## 3. Containerization - test mode

Let's adjust our `docker-compose.yml` so we have a command to test locally and on Travis CI.
Add the following paragraph to it:

```yaml
version: '3.8'

services:
  ...

  web:
    ...

    environment:
      - DATABASE_URL=postgres://postgres:flask_password@db:5432/twitter_api_flask
      - FLASK_RUN_HOST=0.0.0.0
      - FLASK_ENV=development

  test:
    build: .
    container_name: test
    depends_on:
      db:
        condition: service_healthy
    command: nosetests -s --exe
    volumes:
      - .:/code
    environment:
      - DATABASE_URL=postgres://postgres:flask_password@db:5432/twitter_api_flask
      - FLASK_ENV=test

volumes:
  postgres_data:
```

👉 Run `docker-compose up test` to launch the test suite locally.

Your tests should all pass:

* you have not changed any python code, and it worked with the local setup at the beginning of the challenge
* so the only reason it could fail would be docker-based ! If you have an issue with your test suite, please ask a TA !


🎉 That's it for our local setup: we now have a standard way to develop our app and run our test suite on it. 
It might not seem super useful but trust us: **it is** !  
With this kind of setup:

* you will not have any compatibility issues
* you will be able to develop and test in a standardized way, 
* you will be able to contribute with other developers on the exact same setup (that is now super easy to kick-off)

---

## I'm done! 🎉

Clean up your docker host by running ```docker-compose down``` to stop and remove the containers used above.

And that's it for this challenge ! Before you jump to the next challenge (`03-Background-Jobs`), let's mark your progress with the following:

```bash
cd ~/code/<user.github_nickname>/reboot-python
cd 05-Docker/02-Twitter-API
touch DONE.md
git add DONE.md && git commit -m "05-Docker/02-Twitter-API"
git push origin master
```
