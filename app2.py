import flask
import pickle
import pandas as pd

with open(f'Notebooks/nbamodel2.pkl', 'rb') as f:
    classifier = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('Untitled-1.html'))

    if flask.request.method == 'POST':

        Home_or_Away = flask.request.form['Home']
        Field_Goals_Made = flask.request.form['FieldGoals']
        Three_Point_Shots_Made = flask.request.form['X3PointShots']
        Free_Throws_Made = flask.request.form['FreeThrows']
        Free_Throws_Attempted = flask.request.form['FreeThrowsAttempted']
        Steals = flask.request.form['Steals']
        Opponent_3_Point_Shots = flask.request.form['Opp.3PointShots']
        Opponent_Rebounds = flask.request.form['Opp.TotalRebounds']
        Opponent_Steals = flask.request.form['Opp.Steals']
        Opponent_Turnovers = flask.request.form['Opp.Turnovers']

        input_variables = pd.DataFrame([[Home_or_Away, Field_Goals_Made,
                                         Three_Point_Shots_Made, Free_Throws_Made,
                                         Free_Throws_Attempted, Steals, Opponent_3_Point_Shots,
                                         Opponent_Rebounds,
                                         Opponent_Steals, Opponent_Turnovers]],
                                       columns=['Home', 'FieldGoals', 'X3PointShots', 'FreeThrows', 'FreeThrowsAttempted', 'Steals',
                                                'Opp.3PointShots', 'Opp.TotalRebounds', 'Opp.Steals', 'Opp.Turnovers'],
                                       dtype=float)

        prediction = classifier.predict(input_variables)[0]

        return flask.render_template('Untitled-1.html',
                                     original_input=
                                     {'Home_or_Away': Home_or_Away,
                                      'Field Goals Made': Field_Goals_Made,
                                      'Three Point Shots Made': Three_Point_Shots_Made,
                                      'Free Throws Made': Free_Throws_Made,
                                      'Free Throws Attempted': Free_Throws_Attempted,
                                      'Steals': Steals,
                                      'Opponent 3 Point Shots': Opponent_3_Point_Shots,
                                      'Opponent Rebounds': Opponent_Rebounds,
                                      'Opponent Steals': Opponent_Steals,
                                      'Opponent Turnovers': Opponent_Turnovers},
                                     result=prediction)

if __name__ == '__main__':
    app.run()
