from PIL import Image
import os


class Resizer():

    def __init__(self, folderPath):
        self.folderPath = [file for file in os.listdir(folderPath) if file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.eps', '.j2k', '.j2p', '.jpx', '.icns', '.ico', '.pcx', '.webp', '.tiff', '.tif'))]

# def imageResizer()

# for fn in os.listdir('images_src/'):
#     if fn.endswith('.jpg'):
#         img = Image.open('images_src/' + fn)
#         if max(img.size) > 800:
#             img.thumbnail((800, 800), Image.ANTIALIAS)
#             img.save('images/' + fn, 'JPEG', quality=90)


p1 = Resizer('/Users/SK/Desktop/GitHub/PythonProjects/BulkImageResizer/images_src/')

print(p1.folderPath)
