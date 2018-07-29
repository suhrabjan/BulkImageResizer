from setuptools import setup, find_packages

setup(
    name='BulkImageResizer',
    version='1.0.2',
    description='Resizes any number of images, written to use in responsive front end web development',
    long_description=open('README.md', 'r').read(),
    install_requires=['Pillow'],
    url='https://github.com/suhrabjan/BulkImageResizer',
    author='Suhrab Kurbanov',
    author_email='sir.suhrab@gmail.com',
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)
