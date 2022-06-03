## Synthèse
**Projet** : **"GestionEntreprise"** prêt à être exploité pour le cours du 07.12 (G1) et 08.12 (G2)  
**Attention :** Ne pas oublier de mettre en place un environnement virtuel (non fourni dans le repo Github). Rappel des instructions à la fin de ce document.  

### Etapes validées :  
- Mise en route de l'environnement Django (projet, app, settings, architecture, serveur web de dev)
- Premiers routings (CRUD-list)
- Premières vues
- Premier modèle
- Population de la BDD (SQLite) grâce à l'API des modèles
- Système de requêtage de l'API modèles
- Première présentation de l'admin Django
    - Utilisateur d'accès : `geoffroy/admin`

### Mise en place d'un environnement virtuel
**Objectif :** Isoler les dépendances Python (et l'interpréteur Python lui-même) de notre projet, afin d'éviter les conflits avec d'autres projets.  
**Prérequis :** Python (3.7+) installé sur la machine  
**Etapes de mise en place :**  
- Dans un le dossier projet global, déployer un nouvel env. virtuel (ici appelé `myenv` mais un nom personnalisé peut être donné)
```
python -m venv myenv
```
- Activer l'env. virtuel pour le shell courant :
    - Sur Windows
    ```
    .\myenv\Scripts\activate
    ```
    - Sur MacOS/Unix
    ```
    source myenv/bin/activate
    ```
- Vérifier que l'env. virtuel est bien activé - la mention `myenv` doit être affichée devant votre invite de commande :
    ```
    (myenv) .\projects\django_cours>
    ```
- Installer le package Django dans l'env. virtuel courant :
```
pip install django
```
- Pour vérifier l'environnement complet, le dossier projet actuel doit être :
    ```
    - Django_cours\
        - Gestion entreprise\
        - myenv\
        - todo\
        - db.sqlite3
        - manage.py
        - [...]
    ```
- Si les imports Django ne sont pas reconnus et sont signalés en erreur par votre IDE (par exemple la ligne n°1 `from django.db import models` dans le fichier `todo\models.py`) :
    - Vérifier que l'intepréteur Python configuré sur votre IDE (VSCode, PyCharm, etc.) est correctement configuré (en bas à gauche sur VSCode et en bas à droite sur PyCharm)
    - L'interprétieur sélectionné doit être celui de votre env. virtuel et non celui de votre machine (exemple sur VSCode : `Python 3.10.0 64-bit ('myenv':venv)` - en fonction de votre version de Python)