import pandas as pd
from libs.openmeteo import MarineOpenMeteoClient

# Define Spots
spots = {
    "sur": (-38.0, -57.5),
    "norte": (-38.0, -57.0)
}

def main():
    open_meteo_client = MarineOpenMeteoClient()

    print("Select a spot:")
    for index, spot_name in enumerate(spots.keys(), 1):
        print(f"{index}. {spot_name}")

    try:
        choice = int(input("Enter the spot number: "))
        if 1 <= choice <= len(spots):
            spot_name = list(spots.keys())[choice - 1]
            latitude, longitude = spots[spot_name]
            api_response = open_meteo_client.latest(latitude, longitude)
            
            # Extract JSON content from the response
            api_json = api_response.json()
            print(api_json)  # Print the JSON content

            # Extract data from the API response
            data = {}
            for key, value in api_json['daily'].items():
                data[key] = value

            # Create a DataFrame
            df = pd.DataFrame(data)

            # Print the DataFrame
            print(df.head())
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

