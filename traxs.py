import requests
import time
import json

def track_location_by_phone_number(phone_number):
    # Replace with your Google Maps Geocoding API key
    api_key = "YOUR_API_KEY"

    # Base URL for the Geocoding API
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    while True:
        try:
            params = {
                "address": phone_number,
                "key": api_key
            }
            response = requests.get(base_url, params=params)
            response.raise_for_status()

            data = response.json()
            location = data["results"][0]["geometry"]["location"]
            latitude, longitude = location["lat"], location["lng"]

            # Generate Google Maps link
            maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

            # Process location data and update visualization
            # ...

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)  # Retry after 60 seconds

        time.sleep(30)  # Poll every 30 seconds

# Get the phone number from the user
phone_number = input("Enter the phone number: ")

# Call the tracking function
track_location_by_phone_number(phone_number)
