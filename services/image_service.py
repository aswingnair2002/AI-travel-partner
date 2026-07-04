import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PEXELS_API_KEY")


def get_destination_images(destination, count=4):

    headers = {
        "Authorization": API_KEY
    }

    url = (
        f"https://api.pexels.com/v1/search"
        f"?query={destination}+travel"
        f"&per_page={count}"
    )

    try:

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(response.text)
            return []

        data = response.json()

        images = []

        for photo in data.get("photos", []):

            images.append({
                "photographer": photo["photographer"],
                "url": photo["src"]["large"]
            })

        return images

    except Exception as e:

        print(e)
        return []