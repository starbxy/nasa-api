import requests
import os

EONET_URL = "https://eonet.gsfc.nasa.gov/api/v3/events"

num_events = 5

def fetch_events(limit=num_events):
    params = {
        "limit": limit,  # number of events to fetch
        "status": "open" # active events
    }
    response = requests.get(EONET_URL, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    data = fetch_events(limit=num_events)
    for event in data["events"]:
        print(f"Title: {event['title']}")
        print(f"Category: {event['categories'][0]['title']}")
        print(f"Date: {event['geometry'][0]['date']}")
        print(f"Coords: {event['geometry'][0]['coordinates']}")
        print(f"Link: {event['link']}\n")