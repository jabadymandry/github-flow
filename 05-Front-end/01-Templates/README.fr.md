# Templates Flask

Dans cet exercice, nous allons réutiliser l'application de l'exercice `01-SQLAlchemy-Recap` d'hier  :

```bash
cd ~/code/<user.github_nickname>/flask-with-sqlalchemy
```

Assurez-vous que votre `git status` est vide (`add` et `commit` le WIP), et que votre serveur peut toujours être démarré :

```bash
FLASK_ENV=development pipenv run flask run
```

## Page d'accueil

Le but de cet exercice sera de remplacer l'action suivante :

```python
@app.route('/')
def hello():
    return "Hello World!"
```

Au lieu de renvoyer une phrase en texte brut, nous voulons construire une belle page HTML.

Nous voulons que vous construisiez deux pages :
- une page `d'accueil` avec une grille de produits (`/`)
- et une page `détail` dynamique en fonction du produit donné (`/:id`)
Lorsqu'un utilisateur navigue sur la page d'accueil, il doit pouvoir se rendre facilement sur une page "show" en cliquant sur un lien.

Prenez d'abord le temps de lire la documentation de [Flask Templates](http://flask.pocoo.org/docs/1.0/tutorial/templates/). Ceci fait partie du paquet `flask`. Prenez également le temps d'en savoir plus sur [Jinja](http://jinja.pocoo.org/docs/2.10/templates/), le langage de modélisation utilisé par Flask.

```bash
mkdir templates
touch templates/base.html
```

Commençons par le [Bootstrap template](https://getbootstrap.com/docs/4.1/getting-started/introduction/) adapté pour insérer un **bloc** Jinja.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">

    <title>Products</title>
  </head>
  <body>
    <div class="container">
      {% block content %}{% endblock %}
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
  </body>
</html>
```

Dans le contrôleur (`wsgi.py`), vous pouvez instancier :

```python
from flask import Flask, abort, request, render_template

# [...]

@app.route('/')
def home():
    products = db.session.query(Product).all()

    return render_template('home.html', products=products)
```

Essayez de naviguer vers [`localhost:5000`](http://localhost:5000) sur la page d'accueil. Quelle erreur obtenez-vous ? Que devons-nous faire ?

Nous devons créer un nouveau fichier `templates/home.html` et utiliser la variable `products` du fichier `wsgi.py` dans le fichier `home.html` grâce aux arguments `render_template`.

```bash
touch templates/home.html
```

```html
<!-- templates/home.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Products</h1>

  <ul class="list-unstyled">
    {% for product in products %}
      <li>{{ product.name }}</li>
    {% endfor %}
  </ul>
{% endblock %}
```

La classe `list-unstyled` provient de [Bootstrap] (https://getbootstrap.com/docs/4.1/content/typography/#unstyled).

Le contenu du `block content` est réinséré dans le fichier `base.html`.

## La page produit

Nous voulons maintenant implémenter une page de produit **dynamique** affichant les informations d'un seul produit. L'idée est de changer les éléments `<li>` du fichier `home.html` et de mettre des **liens** dessus :

Avant:

```html
<li>{{ product.name }}</li>
```

Après (en utilisant [`url_for`](http://flask.pocoo.org/docs/1.0/api/#flask.url_for)) :

```html
<li>
  <a href="{{ url_for('product_html', product_id=product.id) }}">{{ product.name }}</a>
</li>
```

D'abord, nous devons ajouter une nouvelle route au contrôleur (`wsgi.py`) :

```python
# [...]

@app.route('/<int:product_id>')
def product_html(product_id):
    product = db.session.query(Product).get(product_id)
    return render_template('product.html', product=product)
```

Si vous rechargez votre page d'accueil `/`, vous devriez pouvoir cliquer sur un lien de la liste. Si vous le faites, vous devriez obtenir à nouveau un `jinja2.exceptions.TemplateNotFound`, qui vous indique le fichier manquant.

:point_right: Allez-y et **créez** le fichier manquant.

<details><summary markdown="span">Voir la solution
</summary>

Vous devez exécuter:

```bash
touch templates/product.html
```

</details>


Créons la page Produit avec la variable `product` passée dans l'appel de `render_template` :

```html
<!-- templates/product.html -->

{% extends 'base.html' %}

{% block content %}
  <a href="{{ url_for('home') }}">← Back to list</a>

  <h1>{{ product.name }}</h1>

  <!-- Quelles autres colonnes avez-vous dans la table `products` ? Utilisez-les ici ! -->
{% endblock %}
```

N'oubliez pas de valider et de pousser vos modifications dans votre repository GitHub.

## C'est terminé!

Avant de passer à l'exercice suivant, sauvegardez vos progrès avec ce qui suit:

```bash
cd ~/code/<user.github_nickname>/reboot-python
cd 05-Front-end/01-Templates
touch DONE.md
git add DONE.md && git commit -m "05-Front-end/01-Templates done"
git push origin master
```
