from flask import Flask, render_template, request, g
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Define Spots
spots = {
    "sur": (-38.0, -57.5),
    "norte": (-38.0, -57.0)
}

# Replace the path with the correct path to your SQLite database file
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

def fetch_wave_data(spot_name):
    # Fetch data from the SQLite database
    cursor = get_db().cursor()
    table_name = f'WaveData_{spot_name}'
    query = f'SELECT * FROM {table_name};'
    df = pd.read_sql_query(query, get_db())
    return df

def generate_chart(df):
    print("Columns in DataFrame:", df.columns)

    plt.figure(figsize=(10, 6))
    
    plt.plot(df['time'], df['wave_height_max'], label='Wave Height')
    
    plt.title('Wave Height Over Time')
    plt.xlabel('Time')  # Change to the actual x-axis label
    plt.ylabel('Wave Height (meters)')
    plt.legend()

    # Save the plot to a BytesIO object
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    # Encode the image as base64 for embedding in HTML
    encoded_image = base64.b64encode(image_stream.read()).decode('utf-8')

    return f"data:image/png;base64,{encoded_image}"


@app.before_request
def before_request():
    g.db = get_db()

@app.teardown_request
def teardown_request(exception=None):
    close_db()

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
        chart_image = generate_chart(result_df)
        return render_template('result.html', tables=[result_df.to_html(classes='data')], chart_image=chart_image)

    return render_template('query.html', spots=spots.keys())

if __name__ == '__main__':
    app.run(debug=True)
