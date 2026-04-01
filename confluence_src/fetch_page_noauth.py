import requests
import os
from requests.auth import HTTPBasicAuth

URL = "https://mendozra1972.atlassian.net/wiki/rest/api/content/163934"

USERNAME = "pythonserviceaccount-ny5hyhp2p5@serviceaccount.atlassian.com"
API_TOKEN = os.environ.get("CONFLUENCE_API_TOKEN")

response = requests.get(
    URL,
    params={},
    auth=HTTPBasicAuth(USERNAME, API_TOKEN),
)
response.raise_for_status()

page = response.json()
title = page.get("title", "No title")
space = page.get("space", {}).get("key", "unknown")
body = page.get("body", {}).get("storage", {}).get("value", "No content")

print(f"Title: {title}")
print(f"Space: {space}")
print(f"\nContent:\n{body}")
