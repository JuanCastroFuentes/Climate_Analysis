from flask import Flask, render_template, request, g
import pandas as pd
import sqlite3

app = Flask(__name__)

# Define Spots
spots = {
    "sur": (-38.0, -57.5),
    "norte": (-38.0, -57.0)
}

# Path to SQLite database file
database_path = r"C:\Users\juanm\OneDrive\Documents\CODER DATA ANALYTICS\DATABASES\DATA_BASES\WAVE_ANALYSIS.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database_path)
    return db

def close_db(e=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    instructions = (
        "Welcome to the Wave Analysis App!\n\n"
        "To query wave data, go to the '/query' route.\n"
        "Select a spot, enter the desired parameters, and submit the form."
    )
    return instructions

@app.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        spot_name = request.form['spot']
        result_df = fetch_wave_data(spot_name)
        return render_template('result.html', tables=[result_df.to_html(classes='data')])

    return render_template('query.html', spots=spots.keys())

def fetch_wave_data(spot_name):
    # Fetch data from the SQLite database
    cursor = get_db().cursor()
    table_name = f'WaveData_{spot_name}'
    query = f'SELECT * FROM {table_name};'
    df = pd.read_sql_query(query, get_db())
    return df

# Register close_db to be called when the application context is popped
app.teardown_appcontext(close_db)

if __name__ == '__main__':
    app.run(debug=True)
