**Readme - GUDLFT Registration Server Setup**

---

### Prérequis

Avant de démarrer le serveur GUDLFT Registration, assurez-vous d'avoir les éléments suivants installés sur votre machine :

1. **Python :** [Télécharger Python](https://www.python.org/downloads/)

2. **Flask :** Installez Flask en utilisant la commande suivante dans votre terminal :

    ```bash
    pip install Flask
    ```

### Configuration de l'environnement virtuel

Créez un environnement virtuel pour isoler les dépendances du projet. Utilisez les commandes suivantes dans le terminal :

```bash
# Créez un environnement virtuel
python -m venv venv

# Activez l'environnement virtuel (sous Windows)
venv\Scripts\activate

# Activez l'environnement virtuel (sous macOS/Linux)
source venv/bin/activate
```

### Installation des dépendances

Installez les dépendances nécessaires pour le projet en utilisant la commande suivante :

```bash
pip install -r requirements.txt
```

### Configuration des fichiers

Assurez-vous d'avoir configuré correctement les fichiers de données tels que `clubs.json` et `competitions.json` dans le répertoire du projet.

### Lancement du serveur Flask

Une fois que tout est configuré, lancez le serveur Flask avec la commande suivante :

```bash
flask run
```

Le serveur sera accessible à l'adresse [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

`

### Configuration 

Si vous avez besoin de spécifier un fichier de configuration lors de l'exécution de l'application, utilisez l'option `-c` ou `--config` suivie du chemin vers le fichier de configuration :

```bash
set FLASK_APP = server.py
flask run 

flask --app server.py run
```

Assurez-vous que votre fichier de configuration est correctement formaté et correspond aux besoins spécifiques de votre application.

N'oubliez pas de désactiver l'environnement virtuel lorsque vous avez terminé en utilisant la commande :

```bash
deactivate
```

Ces étapes garantiront que votre environnement est configuré correctement et que le serveur GUDLFT Registration est prêt à être utilisé.