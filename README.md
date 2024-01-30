# FIXATION BUG SHOWSUMMARY

1. Ancien code
    ```shell
    @app.route('/showSummary',methods=['POST'])
    def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    return render_template('welcome.html',club=club,competitions=competitions)
    ```

2. Correction du code
   ```shell
   @app.route('/showSummary', methods=['POST'])
    def showSummary():
        email = request.form['email']
        club = next((club for club in clubs if club['email'] == email), None)
        if club:
            return render_template('welcome.html', club=club, competitions=competitions)
        else:
            error_message = 'Error - Email not found.'
            return render_template('index.html', error_message=error_message)
   ```

En effet dans l'ancien code, lorsqu'un email incorrect est saisi une erreur se produit, parce qu'il y avait pas vérification avant la rédirection. Pour ce faire dans a correection du code, j'ai essayé de faire la vérification de l'email dans la base de donnéées, si l'email ne correspond pas ou est erroné, on un message pour dire que l'email est incorrect.




