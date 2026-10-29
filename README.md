# Mini-projet Docker — Application Flask

## 1. Présentation

Ce projet consiste à conteneuriser une application web Python Flask avec Docker. Il permet de pratiquer la création d’images, l’exécution de conteneurs, la configuration par variables d’environnement, la gestion des ressources, le cache Docker et la publication sur Docker Hub.

## 2. Prérequis

- Docker Engine
- Git
- Un terminal Linux
- Une connexion Internet pour télécharger les dépendances et publier l’image

## 3. Structure du projet

```text
tp-flask/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## 4. Construire l’image

Depuis le répertoire du projet :

```bash
docker build -t monapp:1.0.0 .
```

## 5. Lancer le conteneur

```bash
docker run -d --name monapp-test \
  -p 8081:5000 \
  -e APP_MESSAGE="Bonjour depuis Docker !" \
  --memory=128m \
  --cpus=0.5 \
  monapp:1.0.0
```

## 6. Tester l’application

```bash
curl http://localhost:8081
```

Pour consulter les journaux :

```bash
docker logs monapp-test
```

Pour vérifier les limites de ressources :

```bash
docker inspect monapp-test
```

## 7. Publication sur Docker Hub

Image publiée : `elghoulmariem/monapp`

Tags utilisés :

- `1.0.0` : version initiale
- `1.0.1` : version mise à jour
- `1.0` : alias mis à jour vers la version `1.0.1`

Pour récupérer et lancer la version mise à jour :

```bash
docker pull elghoulmariem/monapp:1.0.1
docker run -d --name monapp-public \
  -p 8084:5000 \
  -e APP_MESSAGE="Application téléchargée depuis Docker Hub !" \
  elghoulmariem/monapp:1.0.1
```

## 8. Bonnes pratiques appliquées

- Utilisation d’une image Python légère (`python:3.12-slim`).
- Installation des dépendances avant la copie du code pour optimiser le cache.
- Exclusion des fichiers inutiles et secrets via `.dockerignore`.
- Exécution de l’application avec un utilisateur non privilégié.
- Configuration par variable d’environnement.
- Limitation de la mémoire et du CPU.
- Versionnement des images avec des tags.

## 9. Auteur

Projet réalisé dans le cadre des Docker Training Labs.
