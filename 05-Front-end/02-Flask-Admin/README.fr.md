# Flask Admin

Si vous souhaitez ajouter facilement un back-office à votre application, le paquet [`flask-admin`](https://flask-admin.readthedocs.io/en/latest/) peut vous aider. L'idée principale de ce paquet est de construire une application CRUD simple à partir de quelques lignes de python.

Encore une fois, nous pouvons utiliser notre application produit pour tester le paquet `flask-admin` :

```bash
cd ~/code/<user.github_nickname>/flask-with-sqlalchemy
```

Assurez-vous que votre `git status` est propre et n'oubliez pas de travailler dans une branche !

```bash
git checkout -b flask-admin
```

Installons le paquet `flask-admin` avec :

```bash
pipenv install flask-admin
```

Ouvrez votre `wsgi.py` et ajoutez la ligne suivante en haut du fichier, juste après `import Flask` :

```python
from flask_admin import Admin
```

Dans le fichier `wsgi.py`, avant la première `@app.route`, initialisez votre nouvel objet `Admin` avec :

```python
# [...]
admin = Admin(app, template_mode='bootstrap3')
# [...]
```

Si vous ne l'avez pas encore fait, démarrez votre serveur flask :

```bash
FLASK_ENV=development pipenv run flask run
```

Et maintenant, accédez à [`localhost:5000/admin`](http://localhost:5000/admin). Vous devriez voir une page d'accueil Admin vide. Il est maintenant temps de la remplir !

Dans le fichier `wsgi.py`, configurez les modèles que vous voulez ajouter à ce `/admin` :

```python
# Ceci va en haut de votre fichier, après le `from flask_admin...` par exemple
from flask_admin.contrib.sqla import ModelView

# Ceci va après `admin =` & l'importation de modèles :
admin.add_view(ModelView(Product, db.session))
```

Rechargez la page [`localhost:5000/admin`](http://localhost:5000/admin). N'est-ce pas merveilleux ?

Pour pouvoir utiliser toutes les fonctionnalités CRUD, vous devez vous assurer que votre application a une [**clé**](https://flask.pocoo.org/docs/1.0/quickstart/?highlight=secret#sessions). Pour ce faire, ouvrez le fichier `config.py` et ajoutez une ligne à votre objet `Config` :

```python
SECRET_KEY = os.environ['SECRET_KEY']
```

Vous devez également ajouter la nouvelle variable d'environnement `SECRET_KEY` à votre `.env`. Pour générer une clé secrète aléatoire, vous pouvez utiliser la technique suivante :

```bash
python -c 'import secrets; print(secrets.token_urlsafe(16))'
```

:rocket: Allez-y, essayez de créer, mettre à jour et supprimer des produits avec ce nouveau panneau d'administration !

N'oubliez pas de versionner et de pousser votre branche.

## Pour aller plus loin

Vous pourriez vous inquiéter que les utilisateurs aient accès à ce panneau d'administration, et vous devriez ! La documentation de Flask-admin contient [une section à ce sujet](https://flask-admin.readthedocs.io/en/latest/introduction/#authorization-permissions).

## J'ai fini!

Avant de passer à l'exercice suivant, sauvegardez vos progrès avec ce qui suit :

```bash
cd ~/code/<user.github_nickname>/reboot-python
cd 05-Front-end/02-Flask-Admin
touch DONE.md
git add DONE.md && git commit -m "05-Front-end/02-Flask-Admin done"
git push origin master
```
