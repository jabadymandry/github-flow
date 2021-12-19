# Docker 101

🎯 Le but de cet exercice est de :

* valider l'installation de Docker Desktop
* vous guider à travers les commandes courantes de Docker, en utilisant la CLI `docker`,
* tout en vous donnant quelques détails sur celles-ci et sur les concepts Docker associés

---

## 0. Validation de l'installation ✅
### 0.a. Docker Desktop est-il déjà installé ? 🐳

Vous devez déjà avoir installé Docker Desktop sur votre ordinateur - dans le cadre de la section **"Avant votre formation"** sur Learn.


👀 Si vous voyez une icône de baleine dans la barre d'état qui reste stable, **Docker Desktop** est en marche et est accessible depuis n'importe quelle fenêtre de terminal. Vous êtes prêt ✅
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/status-bar.png?raw=true" width="250"></p>

👀 Si vous ne voyez pas cette icône de baleine, mais que vous avez déjà **Docker Desktop** installé sur votre machine, il suffit de le démarrer ! Attendez que l'icône de la baleine soit stable et c'est parti ✅
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/docker-desktop.png?raw=true" width="400"></p>


👀 Si vous n'avez pas installé **Docker Desktop** :point_right: veuillez consulter la section **"Avant votre formation "** (ici, sur Learn) et suivre les étapes d'installation.

---

Assurons-nous maintenant que tout va bien, et familiarisons-nous avec les concepts introduits en cours.

### 0.b. Docker Hub 💻

##### S'inscrire
Docker Hub est un service de dépôt hébergé fourni par Docker pour trouver et partager des images de conteneurs avec votre équipe. Une fois que vous aurez créé un identifiant Docker (un utilisateur), vous serez en mesure de récupérer et de pousser des images vers le Hub.

Créer un compte personnel 👉  [ici](https://hub.docker.com/signup).

##### Connexion 🔑

Ouvrez un terminal et tapez :
```bash
docker login
```

Vous serez invité à saisir votre nom d'utilisateur et votre mot de passe :
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/docker-login.png?raw=true" width="700"></p>

En cas de succès, votre terminal devrait vous indiquer "Login Succeeded" 🙌 !

---

### 0.c. Hello-World ! 👋

Validons notre installation Docker en exécutant notre premier conteneur : `hello-world`. Pour ce faire, exécutez ce qui suit dans votre terminal :

```bash
docker run hello-world
```

Puisque vous n'avez pas d'images docker sur votre hôte (puisque vous venez d'installer docker),

* il va d'abord récupérer l'image `hello-world` du Hub
* puis il lancera un conteneur à partir de cette image (celui-ci _seulement_ affiche un message)

Vous devriez vous retrouver avec quelque chose comme ça :
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/hello-world.png?raw=true" width="700"></p>


##### Pour voir les conteneurs que vous avez en cours d'exécution sur votre hôte 👀 :

```
docker ps
```

Vous ne voyez rien 🤔 ? C'est normal !
Votre conteneur `hello-world` ne tourne plus : il s'est éteint dès qu'il a eu terminé. Son travail consistait simplement à afficher un message.

En fait, la commande `docker ps` peut prendre des arguments : la documentation peut être récupérée [ici](https://docs.docker.com/engine/reference/commandline/ps/), ou vous pouvez demander l'utilisation de la commande avec `docker ps --help`.

##### Pour afficher tous les conteneurs (même ceux qui ne sont pas en cours d'exécution), exécutez :
```
docker ps -a
```

Vous devriez voir un conteneur ici. Quel est son nom ? Quelle image a été utilisée pour le faire fonctionner ? Quel est son état ?

##### Pour visualiser les images sur votre hôte :
```
docker images
```

Vous devriez voir votre image `hello-world`, fraîchement récupérée. Vous avez également accès à d'autres détails tels que

* l'id de l'image,
* la balise de l'image (utilisée pour transmettre des informations importantes sur l'image. Par défaut, la balise est "latest". Vous pouvez jeter un coup d'oeil à [cette liste de balises](https://hub.docker.com/_/python) : comprenez-vous à quoi elles servent ?),
* la taille de l'image

---

## 1. Commandes Docker courantes

### 1.a. Exécuter un conteneur

La commande [**`docker run`**](https://docs.docker.com/engine/reference/run/) est utilisée pour exécuter un conteneur à partir d'une image : vous devez lui passer le nom de l'image, comme `docker run <SOME_IMAGE>`.
<br>
👉 Par exemple, exécutez un conteneur à partir de l'image `postgres`. Vous pouvez voir [ici](https://hub.docker.com/_/postgres) que l'image postgres est disponible sur le Hub !

<details><summary markdown='span'>Voir la solution</summary>

```bash
docker run postgres
```

</details>

Il va exécuter une instance de la base de données postgres (que vous connaissez depuis hier : nous l'avons utilisée pour notre API Twitter). Comment 🤔 ?

- Docker utilisera l'image de l'hôte (votre machine) si elle existe.
- Si l'image n'est pas présente sur l'hôte, il ira sur le Docker Hub et récupèrera l'image pour vous 👌 !

Notez que pour les exécutions suivantes, la même image sera réutilisée. Votre machine n'aura pas besoin d'extraire l'image encore et encore.

Mais remarquez que lorsque vous avez lancé `docker run postgres`, cela n'a pas fonctionné ! Pourquoi ?


<details><summary markdown='span'>Voir la solution</summary>

```bash
Error: Database is uninitialized and superuser password is not specified.
   You must specify POSTGRES_PASSWORD to a non-empty value for the
   superuser. For example, "-e POSTGRES_PASSWORD=password" on "docker run".
```
Eh bien, il semble que l'image postgres attende quelque chose sur `docker run` !

</details>

👉 Essayez de réparer ça !

<details><summary markdown='span'>Voir la solution</summary>

Faisons juste ce que `docker run` demande :

```bash
docker run -e POSTGRES_PASSWORD=password postgres
```

</details>

🍾 C'est tout ! Pas besoin d'un installateur complexe, pas de conflits sur votre ordinateur portable, pas de longues heures à parcourir les forums techniques pour résoudre votre problème : vous avez une base de données en fonctionnement en une seule commande.


Le `-e` dans `docker run -e ...` correspond à une variable d'environnement. Ici, nous avons juste créé un mot de passe pour le super-utilisateur de la base de données, et l'avons passé à la commande `docker run`. Idéalement, un mot de passe devrait être plus complexe et nous ne devrions pas le fournir à partir de la ligne de commande, mais ici nous allons le faire de cette façon pour des raisons de simplicité.


Maintenant, vous devriez voir un message dans votre terminal : il semble que votre base de données soit initialisée et prête à accepter des connexions !

<details><summary markdown='span'>Voir la solution</summary>

Le message de votre terminal devrait ressembler à ceci :

```bash
...
PostgreSQL init process complete; ready for start up.

2020-11-19 19:00:28.075 UTC [1] LOG:  starting PostgreSQL 13.1 (Debian 13.1-1.pgdg100+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 8.3.0-6) 8.3.0, 64-bit
2020-11-19 19:00:28.076 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2020-11-19 19:00:28.076 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2020-11-19 19:00:28.079 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2020-11-19 19:00:28.084 UTC [56] LOG:  database system was shut down at 2020-11-19 19:00:27 UTC
2020-11-19 19:00:28.091 UTC [1] LOG:  database system is ready to accept connections
```

</details>


👉 Arrêtez le conteneur en appuyant sur CTRL-C.

---

### 1.b. Exécuter un conteneur en arrière-plan

Une autre chose que vous pouvez faire est d'exécuter un conteneur en arrière-plan (en utilisant le mode "détaché"). De cette façon, la fenêtre de votre terminal sera disponible.

👉 Essayez de lancer un nouveau conteneur postgres en mode détaché, et donnez-lui un nom : `pg`.

<details><summary markdown='span'>Indice</summary>

Si vous n'êtes pas sûr de la syntaxe et des options disponibles : demandez-les !
```bash
docker run --help
```

</details>

<details><summary markdown='span'>Voir la solution</summary>

```bash
docker run -d -e POSTGRES_PASSWORD=password --name=pg postgres
```

</details>


Que se passe-t-il si on ne lui donne pas de nom ?
👉 Exécuter un autre conteneur postgres sans lui donner de nom : quel nom lui a-t-on attribué ?

<details><summary markdown='span'>Indice</summary>

Vous souvenez-vous comment lister tous les conteneurs en cours d'exécution ?

</details>
<details><summary markdown='span'>Voir la solution</summary>

```bash
docker run -d -e POSTGRES_PASSWORD=password postgres
docker ps
```

Eh bien, Docker génère des noms pour nous si nous n'en passons aucun.

</details>

---

### 1.c. Accéder à la base de données Postgres

Maintenant que votre conteneur est en cours d'exécution, vous pourriez vouloir exécuter une requête SQL.
Commençons par lancer un terminal bash dans le conteneur :

👉 Exécutez ```docker exec -it pg /bin/bash```

Qu'avons-nous fait ici 🤔 ? Nous avons demandé à Docker d'exécuter une commande (`/bin/bash` : pour obtenir un interpréteur) dans le conteneur, en passant les indicateurs `-i` et `-t` ensemble :

* L'indicateur `-i` signifie mode "interactif" : il nous propose une saisie standard **stdin** (par défaut, un conteneur fonctionne en mode non-interactif : il ne tient pas compte des saisies de votre côté). Pour transmettre une saisie, vous devez passer cet indicateur `-i`.
* L'indicateur `-t` signifie "tty", qui est une commande de système d'exploitation de type Unix : avec cet indicateur, vous obtiendrez un invite de commande.

Ainsi, la combinaison de ces deux indicateurs nous donne accès à un "terminal", dans le conteneur 🎉 !

Nous pouvons maintenant accéder à notre base de données en utilisant la CLI `psql` :

👉 Exécutez ```psql -U postgres```

Cela vous donne accès à la ligne de commande Postgresql, où vous pouvez écrire du SQL.

<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/psql-docker.png?raw=true" width="500"></p>

👉 Quitter l'invite `psql` : `\q` + **Entrée**
👉 Quitter l'interpréteur du conteneur : `exit` + **Entrée**


C'est typiquement ce que les développeurs font localement lorsqu'ils travaillent sur un projet de webapp (comme vous l'avez fait pour l'API Twitter) : ils dockerisent l'application serveur web, et la base de données. De cette façon, leur configuration est standardisée, et ils peuvent facilement la partager !

---

### 1.d. Nettoyer

#### arrêter et effacer les conteneurs

Pour arrêter un conteneur, utilisez la commande [`docker stop`](https://docs.docker.com/engine/reference/commandline/stop/). Vous devrez passer l'ID du conteneur, ou le nom du conteneur.
👉 Arrêtez votre conteneur `pg`, et vérifiez la liste des conteneurs en cours d'exécution, et la liste des conteneurs qui ne sont pas en cours d'exécution.


<details><summary markdown='span'>Voir la solution</summary>

Arrêter le conteneur:
```bash
docker stop pg
```

Et la liste des conteneurs en cours d'exécution et des conteneurs arrêtés :
```bash
docker ps
docker ps --filter "status=exited"
```
</details>

Vous devriez voir que votre conteneur a changé d'état, passant de `running` à `exited`, mais il est toujours là ! Pour le supprimer de votre hôte, exécutez la commande `docker rm`.

👉 Supprimez votre conteneur postgres

<details><summary markdown='span'>Indice</summary>

```bash
docker rm --help
```

</details>
<details><summary markdown='span'>Voir la solution</summary>

```bash
docker rm pg
```

</details>

#### supprimer une image

Vous avez donc arrêté et supprimé votre conteneur postgres, mais qu'en est-il de l'image postgres que votre hôte a initialement récupérée du Docker Hub.

👉 Vous vous souvenez comment lister les images docker ?

<details><summary markdown='span'>Voir la solution</summary>

```bash
docker images
```

</details>

👉 Essayez de supprimer l'image `postgres` en utilisant [`docker rmi`](https://docs.docker.com/engine/reference/commandline/rmi/) et vérifiez que cela a fonctionné.

<details><summary markdown='span'>Voir la solution</summary>

```bash
docker rmi postgres
docker images
```

Si vous avez d'autres conteneurs sur votre hôte utilisant l'image `postgres`, vous ne pourrez pas supprimer l'image... Débarrassez-vous d'abord des conteneurs ! Vous savez déjà comment faire !

</details>

---

### 1.e. Dockerfile, docker build, docker push

Récapitulons ce que nous venons de faire :

* Nous avons lancé un conteneur `pg` à partir de l'image `postgres`.
* nous l'avons arrêté
* nous l'avons supprimé de l'hôte
* nous avons également supprimé son image

C'était pratique car nous voulions jouer avec l'image Postgres - déjà disponible sur le Hub.

🤔 Mais si nous voulions créer notre propre image ? Et la mettre sur le Hub pour la rendre disponible pour d'autres projets, d'autres développeurs ?

Eh bien, il faudrait :

* ➡️ écrire un `Dockerfile`,
* ➡️ construire notre conteneur Docker,
* ➡️ le pousser sur le Docker Hub !

💪 **Faisons-le !**


Nous allons jouer avec l'image `docker/whalesay`, et créer une image personnalisée à partir de celle-ci.

👉 Récupérez l'image `docker/whalesay` du Hub.

<details><summary markdown='span'>Indice</summary>

Vous savez déjà comment récupérer une image ! Si vous ne vous en souvenez pas, lancez

```bash
docker pull --help
```

</details>
<details><summary markdown='span'>Voir la solution</summary>

```bash
docker pull docker/whalesay
```

</details>

👉 Exécuter un conteneur à partir de cette image (veuillez vérifier [comment utiliser cette image](https://hub.docker.com/r/docker/whalesay/))

<details><summary markdown='span'>Voir la solution</summary>

```bash
docker run docker/whalesay cowsay "This whale is speaking ..."
```

</details>


A partir de là, nous aimerions modifier cette image, de sorte que la baleine "dise" automatiquement quelque chose (généré aléatoirement).

Nous aimerions exécuter quelque chose comme : ``docker run <Votre ID DOCKER>/custom-whale`` qui génère une citation célèbre.

Nous avons donc besoin de différentes choses ici :
* construire une nouvelle image à partir de l'image `docker/whalesay` : vous savez déjà que nous devrons écrire un [Dockerfile](https://docs.docker.com/engine/reference/builder/)
* être capable de générer des citations aléatoires : nous utiliserons [Unix Fortune](https://en.wikipedia.org/wiki/Fortune_(Unix))
* Poussez cette image construite vers votre repository Docker Hub personnel.


👉 Créez un fichier nommé Dockerfile dans ce dossier d'exercice.

```bash
cd ~/code/<user.github_nickname>/reboot-python
cd 05-Docker/01-Docker-101
touch Dockerfile
```

👉 Copiez et collez-y le texte suivant

```dockerfile
FROM docker/whalesay:latest
RUN apt-get -y update && apt-get install -y fortunes
CMD /usr/games/fortune -a | cowsay
```

Que fait-il ?

---

```dockerfile
FROM docker/whalesay:latest
```

> L'instruction **FROM** initialise une nouvelle étape de construction et définit l'image de base pour les instructions suivantes. Ici, nous utilisons l'image `docker/whalesay` (sa version la plus récente) et construisons notre image personnalisée à partir de celle-ci.

```dockerfile
RUN apt-get -y update && apt-get install -y fortunes
```

> L'instruction **RUN** exécutera toutes les commandes dans une nouvelle couche par-dessus l'image actuelle et soumettra les résultats. Chaque ligne de Dockerfile représente une "couche" de l'image complète.
Ici, la commande met à jour la liste des paquets disponibles et leurs versions, et installe le programme `fortune` pour la génération de citations aléatoires.

```dockerfile
CMD /usr/games/fortune -a | cowsay
```

> Il ne peut y avoir qu'une seule instruction **CMD** dans un Dockerfile. Le but principal d'une **CMD** est de fournir des valeurs par défaut pour un conteneur en cours d'exécution.
Ici, l'astuce consiste à utiliser le "pipe" (`|`) qui va d'abord générer une citation aléatoire (en utilisant `/usr/games/fortune -a`) et la transmettre à la commande [`cowsay`](https://en.wikipedia.org/wiki/Cowsay).

---

👉 Il est maintenant temps de construire votre image : ```docker build -t $DOCKER_ID/custom-whale .``` - qui lira les instructions du Dockerfile. N'oubliez pas de remplacer `$DOCKER_ID` par votre ID docker réel  ⚠️ !

<details><summary markdown='span'>Vous devriez voir qu'il a été construit couche par couche.</summary>

```bash
Sending build context to Docker daemon  2.048kB
Step 1/3 : FROM docker/whalesay:latest
 ---> 6b362a9f73eb
Step 2/3 : RUN apt-get -y update && apt-get install -y fortunes
 ---> Running in 4112a9cbddcd
...
...
Removing intermediate container 4112a9cbddcd
 ---> b02c2255a8e6
Step 3/3 : CMD /usr/games/fortune -a | cowsay
 ---> Running in 3e2cd7673b16
Removing intermediate container 3e2cd7673b16
 ---> 23e6cedd0cfe
Successfully built 23e6cedd0cfe
Successfully tagged $DOCKER_ID/custom-whale:latest
```

</details>


👉 Exécutez-le pour voir ce qu'il fait

<details><summary markdown='span'>Voir la solution</summary>

```bash
docker run $DOCKER_ID/custom-whale
```

</details>

👉 Exécutez-le à nouveau ! Il devrait générer des citations différentes à chaque fois - car elles sont aléatoires.

👉 Vous pouvez maintenant pousser votre image vers votre propre repository sur le Docker Hub. Assurez-vous que vous êtes connecté :
```docker login``` et exécutez ce qui suit :

```bash
docker push $DOCKER_ID/custom-whale
```

De cette façon, puisqu'il est public, n'importe qui pourrait le récupérer et l'exécuter en tant que conteneur.

👉 Même chose que ce que nous avons vu pour l'image Postgres, vous pouvez la voir listée [ici](https://hub.docker.com/).

👉 Certaines personnes sont allées encore plus loin ... Essayez celle-ci : ``docker run -it --rm danielkraic/asciiquarium`` !

---

## J'ai fini! 🎉

C'est tout pour ce défi ! Félicitations, vous avez vu comment faire pour :
- récupérer une image (`docker pull $IMAGE_NAME`)
- exécuter un conteneur à partir d'une image (`docker run $IMAGE_NAME`)
- exécuter une commande dans un conteneur en cours d'exécution (`docker exec -it $CONTAINER_NAME $SOME_COMMAND`)
- lister vos conteneurs et images (`docker ps`, `docker ps -a`, `docker images`)
- arrêter et supprimer un conteneur (`docker stop $CONTAINER_NAME`, `docker rm $CONTAINER_NAME`)
- supprimer une image (`docker rmi $IMAGE_NAME`)
- écrire un fichier Docker
- construire une image à partir d'un fichier Docker et la baliser (`docker build -t $SOME_NAME .`)
- pousser une image vers le Docker Hub (`docker push $YOUR_IMAGE`)

Vous connaissez donc déjà toutes les commandes de base pour interagir avec les images et les conteneurs !

Avant de passer à l'execice suivant (Twitter-API), sauvegardez vos progrès avec ce qui suit :

```bash
cd ~/code/<user.github_nickname>/reboot-python
cd 05-Docker/01-Docker-101
touch DONE.md
git add DONE.md && git commit -m "05-Docker/01-Docker-101"
git push origin master
```
