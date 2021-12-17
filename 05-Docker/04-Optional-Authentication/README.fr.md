# Optionnel - Authentification

Pour cet exercice, nous n'utiliserons **pas** Docker et nous travaillerons sur l'authentification sur notre **structure locale** (comme nous l'avons fait les jours précédents). En effet, il est plus facile de traiter ce sujet sans la complexité de la conteneurisation dans un premier temps.

---

Revenons à notre API Twitter d'hier. Vous pouvez commencer par le code suivant (en utilisant la branche `sqlalchemy`) :

```bash
cd ~/code/<user.github_nickname>
git clone git@github.com:ssaunier/twitter-api.git twitter-api-authentication
cd twitter-api-authentication
git checkout sqlalchemy  # récupérer cette branche avant de changer la version distante

git remote rm origin
```

Allez sur [github.com/new](https://github.com/new) et créez un repository _public_ sur votre compte _personnel_, nommez-le `twitter-api-authentication`.

```bash
git remote add origin git@github.com:<user.github_nickname>/twitter-api-authentication.git
git push -u origin sqlalchemy
```

Maintenant que vous avez le repo, vous devez créer le virtualenv et installer les paquets :

```bash
pipenv install --dev
```

Let's set the DB:

```bash
touch .env
```

```bash
# .env
DATABASE_URL="postgresql://postgres:<password_if_necessary>@localhost/twitter_api_flask_authentication"
```

```bash
winpty psql -U postgres -c "CREATE DATABASE twitter_api_flask_authentication"

pipenv run python manage.py db upgrade
```

Si vous obtenez un `sqlalchemy.exc.OperationalError`, vérifiez votre `DATABASE_URL`. Votre mot de passe ne doit pas contenir les symboles `<`, `>`.

```bash
# Exemple valide
DATABASE_URL="postgresql://postgres:root@localhost/twitter_api_flask_authentication"

# Exemple invalide
DATABASE_URL="postgresql://postgres:<root>@localhost/twitter_api_flask_authentication"
```

Tous les points d'entrée de l'API sont accessibles à tous. Rien n'est protégé. Pourtant, nous devons appliquer quelques règles de sécurité de base comme :

- Un utilisateur doit être "connecté" à l'API pour créer un tweet.
- Seul un utilisateur peut supprimer son tweet
- etc.

## Authentification par clé

Vous devriez avoir un modèle `User`. Si vous n'en avez pas, ajoutez-en un.

<details><summary markdown='span'>Voir la solution
</summary>

```python
# models.py
# pylint: disable=missing-docstring

from datetime import datetime
from sqlalchemy.schema import ForeignKey

from app import db

class Tweet(db.Model):
    __tablename__ = "tweets"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(280))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    user = db.relationship("User", back_populates="tweets")

    def __repr__(self):
        return f"<Tweet #{self.id}>"

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(200))
    tweets = db.relationship('Tweet', back_populates="user")

    def __repr__(self):
        return f"<User {self.username}>"
```
</details>

<br />

Ajoutez une nouvelle colonne à votre modèle : `api_key`. Le but est de stocker une clé d'accès (token) longue, unique et aléatoire pour un utilisateur à la création. Vous pouvez y parvenir en utilisant [`uuid` lib et `sqlalchemy.dialects.postgresql.UUID` sur votre déclaration de champ](https://stackoverflow.com/a/49398042).

Une fois qu'un utilisateur a une `clé API`, implémentez la logique pour vous assurer qu'un utilisateur valide peut créer un tweet / seulement un auteur de tweet peut supprimer son tweet.

La clé API peut être utilisée dans l'en-tête de requête HTTP `Authorization` ou dans un argument de strings `?api_key=...`. Un paquet pratique pour implémenter cette fonctionnalité est [`flask-login`](https://flask-login.readthedocs.io/en/latest/).

Nous voulons protéger les trois routes API suivantes derrière une authentification utilisateur (car un tweet ne peut être manipulé que par son créateur)

- `POST /tweets/` (nous avons besoin d'un utilisateur connecté pour le lier au nouveau tweet)
- `PATCH /tweets/1` (seul l'auteur du tweet peut le modifier)
- `DELETE /tweets/1` (seul l'auteur du tweet peut le supprimer)


## OAuth avec un exemple de code

```bash
pipenv install "requests-oauthlib<1.2.0"
pipenv install flask-oauthlib
```

Prenons l'API officielle de Twitter ou l'API de GitHub. Toutes deux fournissent une authentification par le biais d'OAuth, ce qui signifie qu'elles permettent aux développeurs tiers de laisser leurs utilisateurs se connecter à Twitter/GitHub et d'accorder l'accès dans un "périmètre" donné de leur API.

Comme nous créons nous-mêmes une API, nous pouvons vouloir la protéger en utilisant le même type de mécanisme. Au lieu d'avoir une clé d'API pour chaque utilisateur stockée dans la base de données, nous pouvons fournir aux développeurs tiers qui veulent utiliser notre API un service OAuth. Ainsi, ils laisseront les utilisateurs de notre service se connecter via notre serveur OAuth et généreront une clé qui leur permettra d'utiliser et d'interroger l'API.

- [Twitter OAuth](https://developer.twitter.com/en/docs/basics/authentication/overview/oauth.html)
- [GitHub OAuth](https://developer.github.com/apps/building-oauth-apps/)

Avant de passer au code du serveur, vous voudrez peut-être vous faire passer pour un développeur tiers d'une API utilisant OAuth. Vous pouvez le faire avec celui de GitHub !

1. Allez sur [github.com/settings/applications/new](https://github.com/settings/applications/new) et enregistrer une nouvelle application OAuth
1. Téléchargez [ce code](https://github.com/lepture/flask-oauthlib/blob/master/example/github.py) à un fichier `./github.py` dans votre projet
1. Mettez à jour la `consumer_key` et la `consumer_secret` avec la valeur réelle que vous avez obtenue à l'étape 1.
1. Lancez le serveur avec : `pipenv run python github.py`

Maintenant, ouvrez le navigateur et allez sur `localhost:5000`. Que se passe-t-il ?

1. Vous êtes redirigé vers une page GitHub où vous, en tant qu'utilisateur de GitHub, décidez d'accorder (ou non) à ce service `github.py` un accès (avec un **score** donné) à vos informations GitHub
1. Une fois accepté, vous êtes redirigé vers votre service local. Le code stocke _en session_ (qui pourrait être dans la DB !) le `github_token`.
1. Avec cette clé, le code est capable d'effectuer des requêtes à l'API GitHub **au nom de l'utilisateur**.

Comment mettre à jour le `twitter-api` pour utiliser cette passerelle OAuth de GitHub au lieu d'une authentification basée sur une clé ?


---

## J'ai fini! 🎉

C'est tout pour aujourd'hui ! Indiquez vos progrès avec les éléments suivants :

```bash
cd ~/code/<user.github_nickname>/reboot-python
cd 05-Docker/04-Optional-Authentication
touch DONE.md
git add DONE.md && git commit -m "05-Docker/04-Optional-Authentication terminé"
git push origin sqlalchemy
```
