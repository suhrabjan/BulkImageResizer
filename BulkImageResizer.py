from PIL import Image
import os


class Resizer():

    def __init__(self, sourceFolderPath, outputFolderPath):
        self.sourceFolderPath = sourceFolderPath
        self.outputFolderPath = outputFolderPath
        self.imageFiles = [file for file in os.listdir(sourceFolderPath) if file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.eps', '.j2k', '.j2p', '.jpx', '.icns', '.ico', '.pcx', '.webp', '.tiff', '.tif'))]

    def imageResize(self, x_dimension, y_dimension, aspectRatio=False, subsampling=0, quality=95):
        for file in self.imageFiles:
            img = Image.open(self.sourceFolderPath + file)
            if not aspectRatio:
                img = img.resize((x_dimension, y_dimension), Image.ANTIALIAS)
                img.save(self.outputFolderPath + file, format=img.format, optimize=True, subsampling=subsampling, quality=quality)
            elif aspectRatio:
                maxSize = max(x_dimension, x_dimension)
                img.thumbnail((maxSize, maxSize), Image.ANTIALIAS)
                img.save(self.outputFolderPath + file, format=img.format, optimize=True, subsampling=subsampling, quality=quality)

    def imageCompress(self, quality=95):
        for file in self.imageFiles:
            img = Image.open(self.sourceFolderPath + file)
            img.save(self.outputFolderPath + file, format=img.format, optimize=True, quality=quality)
