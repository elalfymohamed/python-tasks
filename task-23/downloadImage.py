import requests
import os
import shutil


def downloadImage():
    image_url = input("Please enter an image URL (string): ")
    file_name = input('Save image as (string):')

    try:
        name_image = image_url.split("/")[-1]
        response = requests.get(image_url)
        if response.status_code != 200:
            print('Image Couldn\'t be retrieved')
        else:
            if not os.path.exists(file_name):
                os.mkdir(file_name)
            with open(name_image, "wb") as f:
                f.write(response.content)
                shutil.move(name_image, file_name)
            print('Image sucessfully Downloaded: ', file_name)

    except:
        print("please enter the URL image")


downloadImage()

# test url image

# https://toppng.com/uploads/preview/cigar-hand-transparent-png-11519552420rdpzltbxkv.png
