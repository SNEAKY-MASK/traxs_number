import requests
import time
import folium

def track_location(phone_number):
    """Tracks the real-time location of a phone number using the Google Maps Geocoding API.

    Args:
        phone_number (str): The phone number to track.
    """

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

            # Create a map centered on the location
            m = folium.Map(location=[latitude, longitude])

            # Add a marker to the map
            folium.Marker([latitude, longitude], popup="Target Location").add_to(m)

            # Save the map as an HTML file
            m.save("location.html")

            print("Location updated.")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)  # Retry after 60 seconds

        time.sleep(30)  # Poll every 30 seconds

# Get the phone number from the user
phone_number = input("Enter the phone number: ")

# Call the tracking function
track_location(phone_number)
