# FIXATION BUG PURCHASEPLACES

1. Ancien code

   ```shell
        @app.route('/purchasePlaces',methods=['POST'])
    def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)

   ```

   Dans ce code, on remarque plusieurs imperfections:
           **Possibilité d'acheter plus de places que de places disponibles**
           **Possibilité d'acheter plus de 12 tickets par une équipe**
           **Possibilité d'acheter zéro tickets**

   2. Fixation

      ```shell
          @app.route('/purchasePlaces', methods=['POST'])
        def purchasePlaces():
        competition_name = request.form['competition']
        club_name = request.form['club']
        places_required = int(request.form['places'])
    
        # Recherche de la compétition et du club dans les données existantes
        competition = next((c for c in competitions if c['name'] == competition_name), None)
        club = next((c for c in clubs if c['name'] == club_name), None)
    
        # Vérification si la compétition et le club existent
        if competition is None or club is None:
            flash('Error - Competition or club not found!')
            return render_template('welcome.html', club=club, competitions=competitions)
    
        # Vérification du nombre de places disponibles
        current_places = int(competition['numberOfPlaces'])
        
        if places_required <= 0 or places_required > current_places:
            flash('Error - Invalid number of places requested!')
            return render_template('welcome.html', club=club, competitions=competitions)
        
        if  places_required == 12 :
            flash('Info - You cannot buy more than 12 places!')
            return render_template('welcome.html', club=club, competitions=competitions)
    
    
        # Mise à jour du nombre de places après l'achat
        competition['numberOfPlaces'] = current_places - places_required
    
        flash('Great - Booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions)
      ```

      # EXPLOITATION DU CODE 

1. **Définition du Point d'Accès (Endpoint) :**
   ```python
   @app.route('/purchasePlaces', methods=['POST'])
   def purchasePlaces():
   ```
   Ce code définit un point d'accès pour traiter les requêtes HTTP POST au chemin `/purchasePlaces`.

2. **Récupération des Données :**
   ```python
   competition_name = request.form['competition']
   club_name = request.form['club']
   places_required = int(request.form['places'])
   ```
   Il récupère les données de la requête POST entrante. Plus précisément, il obtient le nom de la compétition, le nom du club et le nombre de places nécessaires à partir des données du formulaire.

3. **Validation des Données :**
   ```python
   competition = next((c for c in competitions if c['name'] == competition_name), None)
   club = next((c for c in clubs if c['name'] == club_name), None)
   ```
   Il vérifie si la compétition et le club spécifiés existent dans les données fournies.

4. **Gestion d'Erreur - Compétition ou Club Non Trouvé :**
   ```python
   if competition is None or club is None:
       flash('Erreur - Compétition ou club introuvable !')
       return render_template('welcome.html', club=club, competitions=competitions)
   ```
   Si la compétition ou le club n'est pas trouvé, il affiche un message d'erreur et rend un modèle (probablement avec un message de bienvenue).

5. **Validation - Nombre de Places Demandées :**
   ```python
   current_places = int(competition['numberOfPlaces'])
   
   if places_required <= 0 or places_required > current_places or places_required == 12:
       flash('Erreur - Nombre de places demandées invalide !')
       return render_template('welcome.html', club=club, competitions=competitions)
   ```
   Il vérifie si le nombre de places demandées est invalide (inférieur ou égal à 0, supérieur aux places disponibles ou égal à 12). S'il y a des conditions remplies, il affiche un message d'erreur et rend le modèle.

6. **Mise à Jour du Nombre de Places :**
   ```python
   competition['numberOfPlaces'] = current_places - places_required
   ```
   Si la requête passe toutes les validations, il met à jour le nombre de places disponibles pour la compétition après l'achat.

7. **Message de Réussite :**
   ```python
   flash('Super - Réservation terminée !')
   return render_template('welcome.html', club=club, competitions=competitions)
   ```
   Si l'achat est réussi, il affiche un message de réussite et rend le modèle.

**Corrections de Bugs :**
- **Possibilité d'acheter plus que de places disponibles :** Le code vérifie si le nombre de places demandées est supérieur aux places disponibles actuelles.
- **Possibilité d'acheter plus de 12 billets :** Il vérifie spécifiquement si le nombre de places demandées est égal à 12 et affiche un message d'information.
- **Possibilité d'acheter zéro billet :** Il vérifie si le nombre de places demandées est inférieur ou égal à 0.

