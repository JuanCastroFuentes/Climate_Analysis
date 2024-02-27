import pandas as pd
from libs.openmeteo import MarineOpenMeteoClient
from sqlalchemy import create_engine
import pyodbc
import sqlite3

# Define Spots
spots = {
    "sur": (-38.0, -57.5),
    "norte": (-38.0, -57.0)
}

def main():
    open_meteo_client = MarineOpenMeteoClient()

    # Replace the path with the correct path to your SQLite database file
    database_path = r"C:\Users\juanm\OneDrive\Documents\CODER DATA ANALYTICS\GitHub\Climate_Analysis\DATA_BASES\WAVE_ANALYSIS.db"

    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)

    # Create a cursor
    cursor = conn.cursor()

    # Loop through each spot
    for spot_name, (latitude, longitude) in spots.items():
        api_response = open_meteo_client.latest(latitude, longitude)

        # Extract JSON content from the response
        api_json = api_response.json()

        # Extract data from the API response
        data = {}
        for key, value in api_json['daily'].items():
            data[key] = value

        # Create a DataFrame for the current spot
        df = pd.DataFrame(data)

        # Add a new column indicating the spot
        df['spot'] = spot_name

        # Export the DataFrame to a table in SQL Server
        table_name = f'WaveData_{spot_name}'
        df.to_sql(name=table_name, con=sqlite3.connect(database_path), if_exists='replace', index=False)

if __name__ == "__main__":
    main()
