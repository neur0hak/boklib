import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="boklib",
    version="1.1",
    License="MIT License",
    author="neur0hak",
    author_email="xxx9981@gmail.com",
    description="parsing a bank of korea api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neur0hak/boklib",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
