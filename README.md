# BulkImageResizer

 BulkImageResizer automates image resizing and compression of any number of images in a folder. I developed this script to automatically resize and compress the images for responsive web development.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

No prerequisites. BulkImageResizer is compatible with both Python2 and Python3.

### Installation

* Basic installation on your default Python version. Type in following code on your terminal:
```
$ pip install BulkImageResizer
```
If you want to install on a different Python version than default then:
* if default is Python2, then to install on Python3:
```
$ python3 -m pip install BulkImageResizer
```
* if default is Python3, then to install on Python2:
```
$ python2 -m pip install BulkImageResizer
```

## Usage

1. First import the module using the following command on your python project.
```
from BulkImageResizer.BulkImageResizer import BulkImageResizer
```
2. Instantiate BulkImageResizer object with the following arguments:
 * path to source folder (containing images)
 * path to new folder (to save resized images).
 here is an example:
```
sourceFolder = '/Users/SK/Desktop/sourceFolder/'
exportFolder = '/Users/SK/Desktop/exportFolder/'

test1 = BulkImageResizer(sourceFolder, exportFolder)
```
3.1 To resize the image use imageResize() method. It takes minimum two integer numbers as arguments, which indicates the size you want in pixels. 
 here is an example:
```
test1.imageResize(800, 600)
```
 this will resize all the images in the sourceFolder according to given pixels and save them in exportFolder. The original photos in the sourceFolder will not change. 
 If you want to keeps aspect ratio unchanged then use the following:
```
test1.imageResize(800, 600, aspectRatio=False)
```
 this will resize all the images in the sourceFolder so that no matter what the length of the longer side of the image will equal 800px and the length of the shorter side of the image will be calculated based on the aspect ration of the original image. The resized images will be saved in exportFolder.
 You can also change the subsampling value and quality of the image. By default subsampling is set to 0 and can be changed up to 2. Quality is set to 95, which is the maximum quality and can be lowered if you would like to compress the image and decrease file size.
```
test1.imageResize(800, 600, subsampling=2, quality=85)
```
3.2 If you want to just comress the photo without changing the pixel size then you can use imageCompress() method. By default quality is set to 95. If you would like to decrease the file size then you can lower the quality.
```
test1.imageComress(quality=75)
```

## Version

## Authors

## License

## Acknowledgements
