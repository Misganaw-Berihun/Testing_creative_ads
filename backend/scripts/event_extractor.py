import re
import requests

def extract_events(url):
    response = requests.get(url)

    if response.status_code == 200:
        js_content = response.text

        send_event_pattern = r'sendEvent\("([^"]+)"'

        send_events = re.findall(send_event_pattern, js_content)

        print("First parameters from texts that start with 'SendEvent':")
        events = set()
        for event in send_events:
            events.add(event)
        
        return events

    else:
        print(f"Failed to fetch JavaScript file from {url}. Status code: {response.status_code}")