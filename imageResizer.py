from PIL import Image
import os


for fn in os.listdir('images_src/'):
    if fn.endswith('.jpg'):
        img = Image.open('images_src/' + fn)
        if max(img.size) > 800:
            img.thumbnail((800, 800), Image.ANTIALIAS)
            img.save('images/' + fn, 'JPEG', quality=90)
