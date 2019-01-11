import pathlib
from setuptools import setup, find_packages


VERSION = "1.0.0"

DEPENDENCIES = []

# The text of the README file
with open('README.md', encoding='utf-8') as f:
    README = f.read()

# This call to setup() does all the work
setup(
    name="random-username",
    version="1.0.7",
    description="Randomly generate compelling usernames.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/williexu/random_username",
    author="williexu",
    author_email="wx44@cornell.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=DEPENDENCIES,
    entry_points={
        "console_scripts": [
            "random_username=random_username.__main__:main"
        ]
    }
)