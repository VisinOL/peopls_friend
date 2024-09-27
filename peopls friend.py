import requests
import os
import shutil

def download_picture(folder,link):
        basename, extension = os.path.splitext(link)
        if extension not in [".webm", ".mp4"]:
            response = requests.get(link)
            response.raise_for_status()
            filename = f"dog_{item}{extension}"
            with open(f"{folder}/{filename}", 'wb') as file:
                file.write(response.content)

def get_url():
    url = "https://random.dog/woof.json"
    response = requests.get(url)
    response.raise_for_status()
    link = response.json()["url"]
    return link

if __name__ == '__main__':
    folder = "dogs"
    if not os.path.exists(folder):
        os.makedirs(folder)
    elif os.path.exists(folder):
        shutil.rmtree(folder)
    count = 50
    for item in range(count):
        download_picture(folder,get_url())
