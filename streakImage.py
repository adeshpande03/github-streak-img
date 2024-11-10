import requests
from datetime import datetime
import os
import shutil

def main():
    url1 = "https://github-readme-streak-stats-kappa-three.vercel.app?user=adeshpande03&theme=adeshpande03&border_radius=10&hide_longest_streak=true&hide_border=true"
    url2 = "https://github-readme-streak-stats-kappa-three.vercel.app?user=adeshpande03&theme=adeshpande03&border_radius=10&card_width=800"
    
    img_dir = "img"
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    else:
        for filename in os.listdir(img_dir):
            file_path = os.path.join(img_dir, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
    
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    
    if response1.status_code == 200:
        filename1 = os.path.join(img_dir, f"streak.svg")
        with open(filename1, 'wb') as file:
            file.write(response1.content)
    else:
        print(f"Failed to retrieve the image from url1. Status code: {response1.status_code}")
    
    if response2.status_code == 200:
        filename2 = os.path.join(img_dir, f"streak2.svg")
        with open(filename2, 'wb') as file:
            file.write(response2.content)
    else:
        print(f"Failed to retrieve the image from url2. Status code: {response2.status_code}")

if __name__ == "__main__":
    main()

