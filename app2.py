import numpy as np
import flask
import pickle
# Use pickle to load in the pre-trained model.
with open(f'Notebooks/nbamodel.pkl', 'rb') as f:
    classifier = pickle.load(f)
app = flask.Flask(__name__, template_folder='templates')
@app.route('/')
def main():
    return(flask.render_template('Untitled-1.html'))
if __name__ == '__main__':
    app.run()

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('Untitled-1.html'))
    if flask.request.method == 'POST':
        Team1 = flask.request.form['Team']
        Team2 = flask.request.form['Opponent']
        input_variables = nba_stats([[Team1, Team2]],
                                       columns=['Team', 'Opponent'],
                                       dtype=int64)
        prediction = model.predict(input_variables)[0]
        return flask.render_template('main.html',
                                     original_input={'Team':Team1,
                                                     'Opponent':Team2},
                                     result=prediction,
                                     )
