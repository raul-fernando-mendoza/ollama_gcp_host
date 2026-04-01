import os
import requests
from requests.auth import HTTPBasicAuth


CONFLUENCE_BASE_URL = "https://24hf.atlassian.net/wiki"
PAGE_URL = f"{CONFLUENCE_BASE_URL}/spaces/~620591431fec260068c2e8d6/overview"

# Space key extracted from the URL
SPACE_KEY = "~620591431fec260068c2e8d6"


def get_confluence_client():
    email = os.environ.get("CONFLUENCE_EMAIL")
    api_token = os.environ.get("CONFLUENCE_API_TOKEN")
    if not email or not api_token:
        raise EnvironmentError(
            "Set CONFLUENCE_EMAIL and CONFLUENCE_API_TOKEN environment variables."
        )
    return HTTPBasicAuth(email, api_token)


def get_space_overview(space_key: str) -> dict:
    """Retrieve the overview page content for a Confluence space."""
    auth = get_confluence_client()

    # The overview page is the space homepage; fetch it via the space API
    url = f"{CONFLUENCE_BASE_URL}/rest/api/space/{space_key}"
    params = {"expand": "homepage.body.storage,homepage.title"}

    response = requests.get(url, auth=auth, params=params)
    response.raise_for_status()
    return response.json()


def extract_page_content(space_data: dict) -> dict:
    homepage = space_data.get("homepage", {})
    title = homepage.get("title", "No title")
    body = homepage.get("body", {}).get("storage", {}).get("value", "No content")
    return {"title": title, "body": body, "space_key": space_data.get("key")}


if __name__ == "__main__":
    print(f"Fetching Confluence space overview for: {SPACE_KEY}\n")

    space_data = get_space_overview(SPACE_KEY)
    page = extract_page_content(space_data)

    print(f"Title: {page['title']}")
    print(f"Space Key: {page['space_key']}")
    print(f"\nContent (HTML/Storage format):\n{page['body']}")