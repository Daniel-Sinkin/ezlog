from setuptools import find_packages, setup

setup(
    name="ezlog",
    version="0.1.0",
    packages=find_packages(),
    description="A simple logging utility.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Daniel-Sinkin/ezlog",
    author="Daniel Sinkin",
    author_email="danielsinkin97@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Only tested with python 3.12
)
