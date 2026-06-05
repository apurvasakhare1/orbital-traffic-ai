import requests
import os
import json
from datetime import datetime

# Create data directory if it doesn't exist
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# Correct CelesTrak JSON endpoints
CELESTRAK_URLS = {
    "active": "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json",
    "starlink": "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json"
}


def fetch_satellites(group="active"):

    if group not in CELESTRAK_URLS:
        raise ValueError(f"Unknown group: {group}")

    url = CELESTRAK_URLS[group]

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    print(f"Connecting to CelesTrak for '{group}' satellites...")
    print(f"URL: {url}")

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        print("Status Code:", response.status_code)
        print("Content-Type:", response.headers.get("Content-Type"))

        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")

        if "json" not in content_type.lower():
            print("\nUnexpected response received:")
            print(response.text[:1000])
            return None

        satellites = response.json()

        filename = f"{group}_{datetime.now().strftime('%Y%m%d')}.json"
        filepath = os.path.join(DATA_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(satellites, f, indent=2)

        print(f"\nSuccess!")
        print(f"Fetched {len(satellites)} satellites")
        print(f"Saved to: {filepath}")

        return satellites

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        return None

    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return None

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None


if __name__ == "__main__":
    fetch_satellites("active")

