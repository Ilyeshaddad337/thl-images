import os 

from bs4 import BeautifulSoup
p = "/home/ilyeshaddad/.local/share/Anki2/User 1/collection.media"
cpy_dir= "/home/ilyeshaddad/Desktop/images_thl/"

filee = "notion.html"
start_result = "<ul>"

with open(filee, "r") as f:
    data = f.read()
    
if data :
    soup = BeautifulSoup(data, "html.parser")
    
    images = soup.find_all("img")
    images = [image["src"] for image in images]
    for image in images :
        if os.path.exists(os.path.join(p, image)) :
            os.system("cp \"{}\" {}".format(os.path.join(p, image), cpy_dir))
            print("copied {}".format(image))
            data = data.replace(image, os.path.join("images_thl", image.split("/")[-1]))
        else:
            print("file doesn't exist")
            print(os.path.join(p, image))

    # with open(filee.split('.')[0]+"-test.html", "w") as f:
    #     f.write(data)