import requests
import os
from dotenv import load_dotenv

EONET_URL = "https://eonet.gsfc.nasa.gov/api/v3/events"

load_dotenv()
API_KEY = os.getenv("API_KEY")

def fetch_events():
    params = {
        "status": "open", # active events
        "days": 3 # last 3 days - GMT/UTC
        #"api_key": API_KEY
    }
    response = requests.get(EONET_URL, params=params)
    response.raise_for_status()
    return response.json()

def print_events(events):
    for event in events["events"]:
        print(f"Title: {event['title']}")
        print(f"Category: {event['categories'][0]['title']}")
        print(f"Date (UTC): {event['geometry'][0]['date']}")
        print(f"Description: {event['description']}")
        print(f"Coords: {event['geometry'][0]['coordinates']}")
        print(f"Link: {event['link']}")
        print(f"Sources: {event['sources']}\n")

if __name__ == "__main__":
    data = fetch_events()
    print_events(data)