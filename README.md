#Modifications apportées à la route '/book'
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

En utilisant la fonction **nex**t avec une valeur par défaut, vous pouvez obtenir le premier élément correspondant de la liste clubs ou competitions, ou *None* si aucun élément correspondant n'est trouvé. Cela permet d'éviter l'erreur **"IndexError: list index out of range"** en cas de liste vide, lors du test d'integration.

#HTML 
Amélioration de l'interface UI