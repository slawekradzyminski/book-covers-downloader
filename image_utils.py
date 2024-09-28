import os
import requests


def download_image(image_url, file_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(response.content)
        return file_path
    else:
        return "Failed to download image"


def sanitize_filename(title):
    return (
        title.replace(" ", "_")
        .replace("'", "")
        .replace("-", "_")
        .replace("!", "")
        .replace("?", "")
    )
