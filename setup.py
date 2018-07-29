from setuptools import setup

setup(
    name='BulkImageResizer',
    version='0.1',
    description='Resizes any number of images, written to use in responsive front end web development',
    long_description=open('README.md', 'r').read(),
    install_requires=['PIL'],
    url='https://github.com/suhrabjan/BulkImageResizer',
    author='Suhrab Kurbanov',
    author_email='sir.suhrab@gmail.com',
    packages=setuptools.find_packages(),
    scripts=['BulkImageResizer'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)
