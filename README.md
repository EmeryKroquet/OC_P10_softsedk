<h3 align="center">
    <img alt="Logo" title="#logo" src="softdesk_P10-02.png">
    <br>
</h3>

# Projet Académique OpenClassrooms Projet P10

- [Objectif](#obj)
- [Compétences](#competences)
- [Technologies](#techs)
- [Requirements](#reqs)
- [Architecture](#architecture)
- [Configuration locale](#localconfig)
- [Documentation](#docs)

<a id="obj"></a>

## Objectif

SoftDesk, une société d'édition de logiciels de collaboration, a décidé de publier une application permettant de
remonter et suivre des problèmes techniques.
Cette solution, SoftDesk Support, s’adresse à des entreprises en B2B (Business to Business).

SoftDesk a mis en place une nouvelle équipe chargée de ce projet et vous avez été embauché comme ingénieur logiciel pour
créer un back-end performant et sécurisé, devant servir des applications front-end sur différentes plateformes. Il faut
alors trouver un moyen standard de traiter les données, ce qui peut se faire en développant une API RESTful.
<a id="competences"></a>

## Compétences acquises

- Documenter une application
- Créer une API RESTful avec Django REST
- Sécuriser une API afin qu'elle respecte les normes OWASP et RGPD

<a id="techs"></a>

## Technologies Utilisées

- [Python3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [DjangoRestFramework](https://www.django-rest-framework.org/)
- [JWT](https://jwt.io/)
- [Sqlite](https://www.sqlite.org/)

<a id="reqs"></a>

## Requirements

- django
- djangorestframework
- djangorestframework-simplejwt
- python-dotenv

<a id="architecture"></a>

## Architecture et répertoires

```
Project
├── softdesk
│   
│   ├── softdesk_app : répertoire contenant notre application principale
│   ├── softdesk : répertoire du projet django
│   │    ├── settings.py : fichier de réglages django
│   │    ├── urls.py : fichier principal des endpoints
│   │    ├── ..
│   ├── db.sqlite3 : base de données intègré
│   ├── manage.py : fichier principal de gestion django
│
|── README.md 
|── requirements.txt
```

<a id="localconfig"></a>

## Configuration locale

## Installation

### 1. Récupération du projet sur votre machine locale

Clonez le repository sur la machine local en entrant la commande:

```bash
git clone https://github.com/EmeryKroquet/OC_P10-Django-Rest-API-Framework.git
```

Accédez au répertoire du cloné en entrant la commande:

```bash
cd OC_P10-Django-Rest-API-Framework
```

### 2. Création d'un environnement virtuel

Créez l'environnement virtuel venv en entrant la commande:

```bash
python3 -m venv venv
```

### 3. Activation et installation de l'environnement virtuel

Activez l'environnement virtuel venv nouvellement créé en entrant la commande:

```bash
source env/bin/activate
```

Installez la dépendance du projet dans en entrant la commande:

```bash
pip install -r requirements.txt
```

### 4. Initialisation de la base de données

Accédez au dossier du projet en entrant la commande:

```bash
cd softdesk
```

Procédez à une recherche de migrations en entrant lsa commande:

```bash
python manage.py makemigrations
```

Lancer les migrations nécessaires avec la commande:

```bash
python manage.py migrate
```

## Utilisation

### 1. Démarrage du serveur local

Accédez au dossier du projet avec la commande:

```bash
cd softdesk
```

Démarrez le serveur local avec la commande:

```python

python
manage.py
runserver

```

<a id="docs"></a>

## Documentation

Retrouvez la source de documentation de l'api sur postman : https://documenter.getpostman.com/view/11247386/VUqyoZZ5