#TEST D'INTEGRATION
---

Ce projet utilise des tests d'intégration pour garantir le bon fonctionnement des fonctionnalités du serveur GUDLFT Registration. Ces tests sont implémentés à l'aide de l'outil de test unittest de Python et intègrent la bibliothèque BeautifulSoup pour faciliter l'analyse du contenu HTML renvoyé par le serveur.

### Configuration de l'environnement de test

Pour exécuter les tests d'intégration, assurez-vous que l'environnement de test est configuré correctement. Utilisez la commande suivante :

```bash
    python -m unittest .\tests_integrations\TestIntegration.py
```

### Structure des tests

1. **Test de la route '/showSummary' :**
   - Vérifie que la page de résumé est accessible en utilisant un utilisateur existant.
   - Analyse le contenu HTML pour s'assurer que le message de bienvenue et les informations utilisateur sont présents.

2. **Test de la route '/book' :**
   - Vérifie que la réservation pour un événement spécifique est accessible.
   - Analyse le contenu HTML de la page de réservation pour s'assurer que les informations de réservation sont présentes, y compris le nouveau champ 'Available Places'.

3. **Test de la route '/purchasePlaces' :**
   - Vérifie que l'achat de places pour un événement est fonctionnel.
   - Analyse le contenu HTML de la page après l'achat pour s'assurer que le message de confirmation est présent.

### Modifications apportées à la route '/book'

La route '/book' a été modifiée pour gérer la récupération des informations du club et de la compétition avec la nouvelle structure de données (burg). La recherche des éléments a été ajustée en conséquence.

```python
@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)
```
** modification**

```python
    @app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = next((c for c in clubs if c['name'] == club), None)
    foundCompetition = next((c for c in competitions if c['name'] == competition), None)
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong - please try again")
        return render_template('welcome.html', club=club, competitions=competitions)
```

