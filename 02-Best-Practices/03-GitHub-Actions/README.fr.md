
# Github Actions

Les actions Github sont un moyen d'exécuter une commande en réaction à un événement sur votre repo Github. Quelques détails à prendre en compte :
- Un événement est toute action git (push, nouvelle branche) mais aussi des événements spécifiques à Github (par exemple, une nouvelle Pull Request est créée).
- Seuls les événements sur votre dépôt Github distant seront pris en compte ; si vous commitez sur votre machine locale mais ne poussez pas, rien ne sera déclenché.
- Une action peut être, vraiment, n'importe quoi : n'importe quelle commande shell, une autre action Github, etc.

Quelques exemples de cas d'usages :
- Envoyer un message Slack lorsqu'une nouvelle PR est créée.
- Exécuter les tests de votre projet et télécharger les résultats des tests vers Amazon S3
- Créer un package de votre projet automatiquement après chaque push, afin que votre application soit prête à être déployée
- Déployer votre projet en production si nous fusionnons une PR dans la branche principale et si tout ce qui précède a réussi !

:bulb: Toutes ces actions seront exécutées sur un serveur appelé runner. Le runner peut être auto-hébergé, ou peut être fourni par Github.

:warning: Chaque tâche d'un workflow sera exécutée sur un runner distinct. Vous ne pouvez pas avoir une tâche qui configure l'environnement et une seconde qui exécute vos tests, car la seconde tâche ne sera pas exécutée sur l'environnement précédemment préparé mais sur un nouvel environnement. Cependant, cela peut être réalisé en plusieurs étapes dans un seul job.

# Notre premier workflow

Écrivons notre premier workdlow. Un workflow est défini dans un fichier YAML par un ou plusieurs événements sur lesquels il doit être déclenché, et un ou plusieurs jobs qui seront exécutés lorsque le workflow est déclenché. Une tâche est définie par une série d'étapes, et chaque étape peut être soit une commande shell, soit une autre action Github, importée soit du même repo, soit d'un autre. Si une étape se termine anormalement (c'est-à-dire que le code d'état est différent de 0), l'ensemble du worklow est arrêté et les étapes / jobs suivants ne sont pas exécutés.

:bulb: Github fournit une plateforme d'Actions qui peuvent être réutilisées. Elles sont fournies soit par Github (voir https://github.com/actions), soit par la communauté.

Tout d'abord, créez un nouveau repo vide sur votre compte Github et clonez-le. Ne créez pas de nouvelle branche pour l'instant, nous allons pousser directement vers la branche `master`.

Ensuite, nous devons créer un dossier spécial à la racine de votre projet, qui sera reconnu par Github :

```bash
mkdir -p .github/workflows
```

Créons maintenant le fichier de notre workflow. Il doit être situé dans le répertoire `.github/workflows`, qui sera détecté par Github.

```bash
touch .github/workflows/first-workflow.yml
```

Ajoutez ceci à `first-workflow.yml`

```yaml
name: first-workflow
on: [push]
jobs:
  check-python-version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: |
          python --version
```

Voyons ligne par ligne ce que nous faisons :

```yaml
name: first-workflow
```

C'est le nom qui sera affiché sur l'interface Github Action que nous utiliserons un peu plus tard.

```yaml
on: [push]
```

Une liste d'événements sur lesquels ce workflow sera déclenché. Ici, nous écoutons uniquement les push git, ce qui signifie que ce workflow sera automatiquement exécuté lorsque nous `git push` ce repo vers Github.

```yaml
jobs:
```

Une liste de jobs, définie par l'indentation. Ici, nous n'avons qu'un seul travail, check-python-version.

```yaml
runs-on: ubuntu-latest
```

Notre runner. Ici, nous définissons que Github doit nous fournir un serveur exécutant la dernière version d'Ubuntu.

```yaml
steps:
```

Une liste d'étapes pour le job en cours. Toutes ces étapes seront exécutées une par une dans le même environnement.

```yaml
- uses: actions/checkout@v2
```

La première étape. Ce sera presque toujours exactement celle-ci. "uses" indique que nous utilisons une autre action Github. "actions" signifie ici en fait l'espace de travail Github "actions" et "actions/checkout" le repo Github https://github.com/actions/checkout sur lequel l'action est hébergée. Cette action extrait votre repo sur le commit qui a déclenché le workflow.

```yaml
- uses: actions/setup-python@v2
```

Deuxième étape. Idem ici, nous utilisons l'action externe [setup-python](https://github.com/actions/setup-python). Elle téléchargera et installera Python pour le job en cours.

```yaml
with:
        python-version: '3.9'
```

"with" indique que nous fournissons des paramètres à l'action externe utilisée (ici actions/setup-python). Nous indiquons que nous voulons une version Python 3.9.

```yaml
- run: |
      python --version
```

Ici, nous n'utilisons pas `uses` mais `run` qui indique que nous allons exécuter des commandes shell. Le tube `|` indique que le script peut être multiligne. Ce n'est pas le cas ici mais nous aurions pu ajouter une autre commande ci-dessous, ou nous aurions pu simplement écrire `- run: python --version`.

Essayons! Ajoutez, validez et transférez le fichier vers votre référentiel distant.

Une fois que vous l'avez poussé, allez dans l'interface Github, sur la page de votre projet, et cliquez sur l'onglet "Actions". Après quelques secondes, vous devriez voir votre workflow apparaître sur le côté gauche, sous "Tous les workflows", et vous devriez voir une instance de votre workflow en cours d'exécution.

<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/gh_action_workflow_home.jpg?raw=true" width="900"></p>

Cliquez sur l'exécution du workflow pour accéder à la page de cette exécution :

<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/gh_action_workflow_progress.jpg?raw=true" width="900"></p>

Ici, nous n'avons qu'un seul job, python-check-version. Cliquez dessus pour avoir plus de détails :

<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/gh_action_workflow_details.jpg?raw=true" width="750"></p>

Vous pouvez afficher n'importe quelle étape pour obtenir sa sortie :

<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/gh_action_python_version.jpg?raw=true" width="300"></p>


:bulb: Vous pouvez voir que deux autres étapes ont été exécutées après `python --version`. `Post Run actions/checkout@v2` a été automatiquement ajoutée à la fin de votre workflow par notre première étape `actions/checkout@v2`. Cliquez dessus pour voir ce qu'elle fait ! Principalement, elle désactive les paramètres de git pour s'assurer qu'ils ne seront plus jamais accessibles. Surtout utile lorsque nous configurons des informations d'authentification. `Complete job` est ajoutée par Github pour les opérations internes.

# Exercices

:bulb: Dans les exercices suivants, gardez à l'esprit qu'il existe une [plateforme](https://github.com/marketplace?type=actions) avec de nombreuses Actions prêtes à l'emploi !

Pour les besoins de l'exercice, nous allons installer les dépendances suivantes :

```bash
pipenv --python 3.9
pipenv install nose pylint --dev
```

Nous pouvons commit ceci :

```bash
git add Pipfile* && git commit -m "add python dependencies"
```

Ajoutons également un fichier de test. Créez un répertoire `app/tests` :

```bash
mkdir -p app/tests && touch app/__init__.py && touch app/tests/test_example.py
```

Et ajoutez ce fichier `test_example.py` :

```python
# tests/test_example.py
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

from unittest import TestCase
import pylint

class TestExample(TestCase):

    def test_example(self):
        self.assertIsNotNone(pylint)
```

Commit !
```bash
git add app && git commit -m "add first app files"
```

## Exercice 1

Créez un nouveau workflow qui :
- Réagira aux requêtes push et pull (consultez la [documentation](https://docs.github.com/en/actions/learn-github-actions/events-that-trigger-workflows) !)
- A un job avec les étapes suivantes :
     - Checkout la branche
     - Installe les dépendances (indice : jetez un œil au workflow [setup-python](https://github.com/actions/setup-python))
     - Exécute le linter sur le répertoire `app`
     - Lance les tests

:bulb: N'oubliez pas que pour tester votre workflow, vous devez le valider et le pousser vers Github.

<details><summary markdown="span">Voir la solution
</summary>


```yaml
name: Python Linter & Tests

on:
  push:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.9
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pipenv
        pipenv install --dev
    - name: Lint with pylint
      run: |
        pipenv run pylint app
    - name: Test with nose
      run: |
        pipenv run nosetests
```
</details>


:tada: Toutes nos félicitations ! Vous avez mis en place un premier pipeline CI sur votre projet :tada:

## Aller plus loin avant l'exercice 2
### Contexte

Github fournit des variables de contexte qui peuvent être utilisées pour récupérer de nombreuses informations internes (numéro d'exécution actuel, nom du workflow, nom de la branche git, etc.). Contrairement aux variables d'environnement, les variables de contexte sont réévaluées entre chaque étape et deviennent des valeurs codées en dur au moment de l'exécution.

Par exemple, `github.event_name` contient le nom de l'événement qui a déclenché l'exécution du workflow. Pour accéder à la valeur, utilisez la syntaxe d'expression : `${{ github.event_name }}`

:bulb: Voir [contextes](https://docs.github.com/en/actions/learn-github-actions/contexts) pour toutes les variables de contexte disponibles et [expressions](https://docs.github.com/en/actions/learn-github-actions/expressions) pour la syntaxe de l'expression.

### Secrets

L'une des variables de contexte disponibles est `secrets`, qui vous permet d'accéder à des variables spéciales utilisées à des fins d'authentification. Vous pouvez les définir vous-même (par exemple en en créant un depuis l'interface Github dans votre compte en allant dans Paramètres => Secrets) mais un est mis à disposition par Github lors de l'exécution du workflow : `${{ secrets.GITHUB_TOKEN }}`.

Au début de chaque exécution de workflow, Github crée automatiquement un secret `GITHUB_TOKEN` unique et le rend accessible au workflow. Ce jeton peut être utilisé pour authentifier et apporter des modifications au référentiel pour lequel il est en cours d'exécution ; par exemple ajouter un commentaire, créer une Pull Request, ajouter un reviewer, etc.

### Conditions

Vous pouvez exécuter conditionnellement une étape ou une tâche avec la syntaxe "if". Par exemple, si vous souhaitez exécuter une étape ou un job uniquement si l'événement en cours est déclenché sur la branche "master", nous pouvons ajouter les éléments suivants au niveau de l'étape (ou du job) :

```yaml
if: ${{ github.ref == 'refs/heads/master' }}
```

Vous pouvez définir une condition au niveau du job ou au niveau de l'étape.

## Exercice 2

:warning: **Ne pas commit directement vos changements dans `master`** Créez d'abord une branche, avec par exemple :


```bash
git checkout -b test_workflow
```

Allons-y !

Ajoutez un autre job au workdlow de l'exercice 1 (**travaillez sur le même fichier, n'en créez pas un autre!**) qui créera une pull request (PR) avec les exigences suivantes :
- Le nouveau job sera nommé `review`
- Le PR ne doit être créée que si nous ne sommes **pas** sur la branche `master`
- Le titre de la PR doit avoir le format suivant : `Awesome PR by <actor>` où `<actor>` est le nom d'utilisateur Github de la personne qui a déclenché le workflow
- Ce nouveau job ne doit être exécuté que si le précédent job `build` que nous avons créé ci-dessus a réussi


<details><summary markdown="span">Indices (ne les lire qu'après votre premier essai !)
</summary>

- Vous pouvez utiliser le workflow [pull-request](https://github.com/marketplace/actions/github-pull-request-action). Regardez sa documentation pour savoir comment l'utiliser.
- Vous pouvez utiliser le mot-clé `needs` au niveau du job afin de définir les dépendances entre les travaux. Par exemple, un travail avec `needs: job1` ne s'exécutera que lorsque `job1` s'est exécuté et a réussi.

</details>


<details><summary markdown="span">Solution (à ne regarder que si vous avez vraiment vraiment essayé !)
</summary>

```yaml
name: Python Linter & Tests

on: push

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.9
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pipenv
        pipenv install --dev
    - name: Lint with pylint
      run: |
        pipenv run pylint app
    - name: Test with nose
      run: |
        pipenv run nosetests

  review:
    runs-on: ubuntu-latest
    needs: build
    if: ${{ github.ref != 'refs/heads/master' }}
    steps:
      - uses: actions/checkout@v2
      - name: Create Pull Request
        uses: repo-sync/pull-request@v2
        with:
          source_branch: ""
          destination_branch: "master"
          github_token: ${{ secrets.GITHUB_TOKEN }}
          pr_title: "Awesome PR by ${{ github.actor }}"
```

</details>


## J'ai fini

Avant de passer à l'exercice suivant, marquer vos progrès avec les éléments suivants :

```bash
cd ~/code/<user.github_nickname>/reboot-python
cd 02-Best-Practices/03-GitHub-Actions
touch DONE.md
git add DONE.md && git commit -m "02-Best-Practices/03-GitHub-Actions done"
git push origin master
```
