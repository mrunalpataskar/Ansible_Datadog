import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable only the InsecureRequestWarning from urllib3
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def get_latest_releases(api_url):
    try:
        response = requests.get(api_url, verify=False)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        data = response.json()
        return data
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return None

if __name__ == "__main__":
    api_url = "https://api.github.com/repos/DataDog/datadog-agent/releases"

    latest_releases = get_latest_releases(api_url)
    tags = []  # Initialize an empty list to store tags
    if latest_releases:
        for release in latest_releases:
            tags.append(release['tag_name'])  # Append tag to the list
        print(tags[1])  # Print all collected tags at once
    else:
        print("Failed to fetch latest releases.")

