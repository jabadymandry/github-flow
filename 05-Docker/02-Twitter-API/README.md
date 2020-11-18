# Twitter API - Containerization

Start with a clean folder => retrieve it [here]()

A good practice when it comes to building docker app is to have a requirements.txt file:
run the following commands

```
pipenv lock --requirements > requirements.txt
```

```
pipenv lock --requirements --dev-only > requirements-dev.txt
```

---



Let's first Dockerize our Flask app.
Use this Dockerfile, and build the image, and run the container !

We will start from a pure "development" point of view, to have our whole stack locally dockerized. Then we will generalize to other environments (test, CI, prod). But let's start small !


```dockerfile
FROM python:3.8-alpine as base

RUN apk update && apk add postgresql-dev gcc musl-dev
RUN pip install --upgrade pip

WORKDIR /code

COPY requirements.txt /code
COPY requirements-dev.txt /code
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

ENV DATABASE_URL postgres://localhost/twitter_api_flask
ENV FLASK_APP wsgi.py
ENV FLASK_ENV development

COPY app /code/app
COPY config.py /code
COPY wsgi.py /code

CMD ["flask", "run", "--host", "0.0.0.0"]
```

Build it
Details: let's check the container to better understand.

We when run our container -> check http://localhost:5000/ (we mapped our host port to the container port): it's working!
But what happens if you check http://localhost:5000/tweets ? It breaks ! Do you know why ?

---

We need to add a DB: we will use docker-compose

```yaml
version: '3.8'

services:
  web:
    build: .      
    command: flask run
    volumes:
      - .:/code
    ports:
      - 5000:5000
    environment:
      - DATABASE_URL=postgres://localhost/twitter_api_flask
      - FLASK_RUN_HOST=0.0.0.0
      - FLASK_ENV=development
```

What do you see ?

___

Now let's add Postgres




--- 

Query your postgres DB directly !


---

Now let's clean up our files a bit to make it CI and production ready


