import requests
import os
import shutil

def download_picture(folder):
    url = "https://random.dog/woof.json"
    params = {"filter": "mp4,webm"}
    link = requests.get(url, params=params).json()["url"]
    basename, extension = os.path.splitext(link)
    response = requests.get(link)
    response.raise_for_status()
    filename = f"dog_{item}{extension}"
    with open(f"{folder}/{filename}", 'wb') as file:
        file.write(response.content)
    return response.content

if __name__ == '__main__':
    folder = "dogs"
    if os.path.isdir(folder):
        shutil.rmtree(folder)
    elif not os.path.isdir(folder):
        os.makedirs(folder)

    count = 50
    for item in range(count):
        download_picture(folder)
