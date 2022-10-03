from PIL import Image

def imageResize():
    try:
        path_image = input("enter path image: ")
        size_width = int(input("enter width: "))
        size_height = int(input("enter height: "))

        save_name = path_image.split("/")[-1]
        image = Image.open(f"{path_image}")
        sunset_resized = image.resize((size_height, size_width))
        sunset_resized.save(f"{save_name}")
    except:
        print("please try again")

imageResize()
