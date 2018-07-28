from PIL import Image
import os


class Resizer():

    def __init__(self, sourceFolderPath, outputFolderPath):
        self.sourceFolderPath = sourceFolderPath
        self.outputFolderPath = outputFolderPath
        self.imageFiles = [file for file in os.listdir(sourceFolderPath) if file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.eps', '.j2k', '.j2p', '.jpx', '.icns', '.ico', '.pcx', '.webp', '.tiff', '.tif'))]

    def imageResize(self, x_dimension, y_dimension, aspectRatio=False, quality=95):
        for file in self.imageFiles:
            img = Image.open(self.sourceFolderPath + file)
            if not aspectRatio:
                img = img.resize((x_dimension, y_dimension), Image.ANTIALIAS)
                img.save(self.outputFolderPath + file, format=img.format, quality=quality)
            elif aspectRatio:
                maxSize = max(x_dimension, x_dimension)
                img.thumbnail((maxSize, maxSize), Image.ANTIALIAS)
                img.save(self.outputFolderPath + file, format=img.format, quality=quality)


# def imageResizer()

# for fn in os.listdir('images_src/'):
#     if fn.endswith('.jpg'):
#         img = Image.open('images_src/' + fn)
#         if max(img.size) > 800:
#             img.thumbnail((800, 800), Image.ANTIALIAS)
#             img.save('images/' + fn, 'JPEG', quality=90)


p1 = Resizer('/Users/SK/Desktop/GitHub/PythonProjects/BulkImageResizer/images_src/', '/Users/SK/Desktop/GitHub/PythonProjects/BulkImageResizer/dinara/')

p1.imageResize(500, 600, quality=50)
