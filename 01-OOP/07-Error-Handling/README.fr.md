# Gestion des erreurs

Les erreurs et les exceptions font partie de tout langage de programmation. Au moment de l'exécution, notre code peut ne pas se comporter comme nous l'attendons. Supposons que vous avez un dictionnaire et que vous essayez d'accéder à une clé qui _n'existe pas_. C'est une erreur, et Python fournit des indications pour cela (ici ce serait un `KeyError`). Heureusement, il existe un moyen de gérer ces erreurs dans le code.


Commencez par lire le chapitre 8 du Tutoriel Python sur [les Erreurs et les Exceptions](https://docs.python.org/3.8/tutorial/errors.html).

## Syntaxe

Chaque langage propose des **mots-clés** spécifiques pour traiter les erreurs.

Voici les plus importantes que vous devez connaître en Python :

- `try / except` pour que le flux de contrôle gère les erreurs du code appelé
- `raise` lorsque votre code soulève une erreur
- `finally` pour **toujours** exécuter du code après un `essai`
- `with` est spécifique à Python et aide à fermer correctement les flux IO ([cf 8.7](https://docs.python.org/3.8/tutorial/errors.html#predefined-clean-up-actions))

## Exercice

Expérimentons dans le [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) Python avec la fonction intégrée [`int()`](https://docs.python.org/3/library/functions.html#int). Cette fonction est vraiment pratique car elle prend une String et la convertit en un nombre entier. Elle est utile pour lire des informations à partir d'un fichier ou d'un flux réseau où tout est constitué de caractères.


```bash
python

>>> int("1")
1

>>> int("not_a_number")
# => Qu'est-ce qui se passe?
```

Vous venez de déclencher une `ValueError`. Codons un bloc `try / except`.

Ouvrez le fichier `square.py` et lisez le code :

```python
import sys

if __name__ == "__main__":
    print(type(sys.argv[1]))
```

Avant d'exécuter le code, essayez de trouver quel est le comportement de ce petit programme. Vous êtes prêt?

```bash
pipenv run python square.py
```

Que se passe-t-il ? Comment pouvons-nous atténuer ce comportement ? Il y a deux réponses valables à cette question, pouvez-vous coder les deux versions ?

Maintenant que nous avons traité le cas où l'utilisateur ne fournit pas d'argument, fournissons-en un :

```bash
pipenv run python square.py 42
pipenv run python square.py wagon
```

Il est maintenant temps d'utiliser `int()` pour convertir ces arguments de type String et les utiliser. Lors de l'exécution, votre programme devrait afficher le carré du nombre. Si l'argument n'est pas un nombre, il devrait afficher "Not a number". Pour tester votre code, exécutez simplement les commandes ci-dessus 👆, il n'y a pas de test associé à cet exercice. Appelez un professeur si vous avez besoin d'aide.

## (Optionnel) Gestion des erreurs dans PowerShell

PowerShell fournit une structure `try / catch` directement dans le langage :

```powershell
try {
  NonsenseString
}
catch {
  "An error occurred."
}
```

Il est possible de traiter une exception spécifique en fournissant un type entre crochets juste après le mot-clé `catch`, permettant ainsi plusieurs comportements en fonction du type d'erreur :

```powershell
try {
   $wc = new-object System.Net.WebClient
   $wc.DownloadFile("http://www.contoso.com/MyDoc.doc","c:\temp\MyDoc.doc")
}
catch [System.Net.WebException],[System.IO.IOException] {
    "Unable to download MyDoc.doc from http://www.contoso.com."
}
catch {
    "An error occurred that could not be resolved."
}
```

Ces exemples sont tirés du [Microsoft Docs](https://docs.microsoft.com/powershell/module/microsoft.powershell.core/about/about_try_catch_finally), nous vous encourageons à lire l'article en entier pour plus de détails.