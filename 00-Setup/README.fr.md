
:bulb: **Astuce**: si vous pouvez voir ce conseil, votre compte Github est correctement lié, vous pouvez continuer avec l'installation !

## GitHub

Nous utiliserons votre compte public personnel `github.com`. Si vous lisez ceci, cela signifie que vous en avez un et que vous vous êtes connecté avec !

Tout d'abord, assurez-vous que ce repo soit correctement copié (fork) sur votre compte personnel GitHub.

Nous devons créer une clé SSH sur votre ordinateur et la lier à votre compte GitHub. À la fin de la semaine, n'oubliez pas de supprimer cette clé de votre compte GitHub, comme ce n'est pas votre ordinateur. Protégez votre clé avec un **mot de passe** compliqué garantira une bonne sécurité pendant la semaine.

GitHub propose des tutoriels pratiques. Suivez-les:

1. [Générer une nouvelle clé SSH](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-windows)
1. [Ajouter cette clé à votre compte GitHub](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/#platform-windows)

Pour vérifier si cette étape est effectuée, exécutez:

```bash
ssh -T git@github.com
```

S'il est indiqué "Permission denied", appelez un professeur pour vous aider. S'il est indiqué "Hi <github_nickname>", tout va bien!

Enfin, nous devons configurer la commande locale `git` pour préciser qui vous êtes lorsque vous faites un commit:

```bash
git config --global user.email "your_github_email@domain.com"
git config --global user.name "Your Full Name"
```

Il est important d'utiliser la même adresse électronique que celle que vous utilisez sur [GitHub](https://github.com/settings/emails) afin que [les commits soient liés à votre profil](https://help.github.com/articles/why-are-my-commits-linked-to-the-wrong-user/#commits-are-not-linked-to-any-user).


## Exercices

Le repository que vous venez de forker contient tous les exercices de la semaine. Pour travailler dessus, clonez-les sur votre ordinateur. Puis, toujours dans Git Bash, exécutez:

```bash
mkdir -p ~/code/<user.github_nickname> && cd $_
git clone git@github.com:<user.github_nickname>/reboot-python.git
cd reboot-python
git remote add upstream git@github.com:lewagon/reboot-python.git

pwd # C'est votre repository d'exercices!
```

Ce repository a un `Pipfile`. Vous pouvez maintenant installer facilement les dépendances avec la commande suivante:

```bash
pipenv install --dev # pour installer les `packages' **et** `dev-packages`
```

Cela créera le Virtualenv pour ce dossier, en utilisant Python 3.8 comme [spécifié](https://github.com/lewagon/reboot-python/blob/master/Pipfile#L15-L16)

## Valider le défi

Pour chaque défi, nous vous encourageons à **versionner** et **pousser** votre progression. Commençons maintenant avec :

```bash
cd 00-Setup
touch READY
git add READY
git commit -m "I am ready"
git push origin master
```

Vous devriez obtenir un point vert à gauche pour suivre votre progression. Cheers !
