import requests
from datetime import datetime
import os
import shutil

def main():
    url = "https://github-readme-streak-stats-kappa-three.vercel.app?user=adeshpande03&theme=adeshpande03&border_radius=10&hide_longest_streak=true&hide_border=true"
    
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
    
    response = requests.get(url)
    
    if response.status_code == 200:
        today_date = datetime.today().strftime('%Y-%m-%d')
        filename = os.path.join(img_dir, f"streak.svg")
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to retrieve the image. Status code: {response.status_code}")

if __name__ == "__main__":
    main()

