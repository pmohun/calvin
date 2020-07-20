import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="calvin",
    version="0.0.1",
    author="Phil Mohun, Malcolm Navarro, DNE LLC",
    author_email="calvin@philmohun.com",
    description="calvin is a Python library for developers using GPT-3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pmohun/calvin",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD-3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)