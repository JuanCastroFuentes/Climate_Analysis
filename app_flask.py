from flask import Flask, render_template, request
import pandas as pd
import sqlite3

app = Flask(__name__)

# Define Spots
spots = {
    "sur": (-38.0, -57.5),
    "norte": (-38.0, -57.0)
}

# Replace the path with the correct path to your SQLite database file
database_path = r"C:\Users\juanm\OneDrive\Documents\CODER DATA ANALYTICS\DATABASES\DATA_BASES\WAVE_ANALYSIS.db"

# Reuse the existing SQLite connection from api_local.py
conn = sqlite3.connect(database_path)

def fetch_wave_data(spot_name):
    # Fetch data from the SQLite database
    cursor = conn.cursor()
    table_name = f'WaveData_{spot_name}'
    query = f'SELECT * FROM {table_name};'
    df = pd.read_sql_query(query, conn)
    return df

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

if __name__ == '__main__':
    app.run(debug=True)