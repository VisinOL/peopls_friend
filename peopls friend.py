import requests
import os
import shutil

def download_picture(folder, filename, picture_link):
    file_path = requests.get(picture_link).content
    with open(filename, 'wb') as file:
        file.write(file_path)


def main():
    folder = 'dogs'
    if not os.path.isdir(folder):
        os.mkdir(folder)
    else:
        shutil.rmtree(folder)
        os.mkdir(folder)
    url = 'https://random.dog/woof.json'
    for i in range(50):
        params = {"filter" : "mp4,webm"}
        picture_link = requests.get(url, params=params).json()["url"]
        link, picture_extension = os.path.splitext(picture_link)
        filename = f'{folder}/dog{i+1}{picture_extension}'
        download_picture(folder, filename, picture_link)

if __name__ == '__main__':
      main()
