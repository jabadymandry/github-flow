# Nouvelles du client - Livecode

Nous avons construit une API REST toute la journée. Faisons le contraire : **utilisons-en** une.

Nous allons utiliser l'API [News API](https://newsapi.org/) avec la clé API suivante : `367f28d82c3b42e2bb224b79b0ef480e`. Cette API a 2 points d'entrée que nous voulons utiliser :

- `https://newsapi.org/v2/top-headlines`
- `https://newsapi.org/v2/everything`

Dans la [section HTTP de `awesome-python`](https://github.com/vinta/awesome-python#http), nous trouvons le paquet `requests` pour envoyer facilement des requêtes HTTP. Le document de [démarrage rapide](http://docs.python-requests.org/en/master/user/quickstart/) est très utile.

## Configuration

```bash
mkdir news && cd $_
pipenv --python 3.8
pipenv install requests
pipenv install nose --dev

touch main.py
mkdir client
touch client/__init__.py

mkdir -p tests
touch tests/test_news.py

# Nous pouvons maintenant exécuter :
pipenv run nosetests # => 0 tests pour le moment
```

Voici le code de démarrage pour les différents fichiers.

```python
# main.py
from client import News

def main():
    pass

if __name__ == '__main__':
    main()

```

```python
# client/__init__.py
import requests

class News:
    pass
```

```python
# tests/test_news.py
import unittest

from client import News

class NewsTest(unittest.TestCase):
    pass
```

## Codons !

Qui se porte volontaire ? Voici les différentes étapes à suivre :

- Implémentez une classe `News` pour servir de client REST, avec 2 méthodes : `headlines(country)` et `search(keyword`). Utilisez TDD pour cette étape (NB : il s'agira de tests d'intégration).
- Ouvrez le fichier `main.py` et utilisez cette nouvelle classe pour coder une console **interactive** comme celui-ci :

```bash
$ pipenv run python main.py
Country headlines [default] or Search [hit s]?
>
Country?
> us
# - Trump : `Je ne fais rien ... juste pour le profit politique`. - POLITICO
# - La fusée Falcon 9 de SpaceX a été aperçue sur l'aire de lancement 39A alors que le quatuor de lancement de décembre s'aligne - Teslarati
# - [...]

$ pipenv run python main.py
Country headlines [default] or Search [hit s]?
> s
What are you looking for?
> france
# - Trump se rend en France, respectant ainsi une tradition présidentielle post-électorale.
# - Edition Europe : Brexit, Ukraine, France : Votre briefing du lundi
# - Les émeutes françaises sont-elles une malédiction ou une bénédiction pour Macron ?
# - [...]
```

## Solution

Veuillez ne pas regarder _avant_ la session de livecode !

<details><summary markdown='span'>Voir la solution
</summary>

```python
# tests/test_news.py
import unittest

from client import News

class NewsTest(unittest.TestCase):
    def test_french_headlines(self):
        news = News()
        articles = news.headlines("fr")
        self.assertEqual(type(articles), list)
        self.assertGreater(len(articles), 0)

    def test_search(self):
        news = News()
        articles = news.search("france")
        self.assertEqual(type(articles), list)
        self.assertGreater(len(articles), 0)
```

```python
# client/__init__.py
import requests

class News:
    API_KEY = "367f28d82c3b42e2bb224b79b0ef480e"
    BASE_URL = "https://newsapi.org/v2"

    def headlines(self, country = "us"):
        payload = { 'country': country, 'apiKey': self.API_KEY }
        response = requests.get(f"{self.BASE_URL}/top-headlines", params=payload)
        return response.json()['articles']

    def search(self, keyword):
        payload = { 'q': keyword, 'apiKey': self.API_KEY }
        response = requests.get(f"{self.BASE_URL}/everything", params=payload)
        return response.json()['articles']
```

```python
# main.py
from client import News

def main():
    news = News()

    choice = input("Country headlines [default] or Search [hit s]?\n> ")
    if choice == "s":
        keyword = input("What are you looking for?\n> ")
        for article in news.search(keyword):
            print(f"- {article['title']}")
    else:
        country = input("Country?\n> ")
        for article in news.headlines(country):
            print(f"- {article['title']}")

if __name__ == '__main__':
    main()
```
</details>
