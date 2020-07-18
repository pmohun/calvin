import os

from setuptools import find_packages, setup

version_contents = {}
with open(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "calvin/version.py")
) as f:
    exec(f.read(), version_contents)

setup(
    name="calvin",
    description="Python library for interacting with the OpenAI api",
    version=version_contents["VERSION"],
    install_requires=[
        'requests >= 2.20; python_version >= "3.0"',
        'requests[security] >= 2.20; python_version < "3.0"',
    ],
    extras_require={},
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    scripts=[],
    # packages=find_packages(exclude=["tests", "tests.*"]),
    # package_data={"openai": ["data/ca-certificates.crt"]},
    author="Philip Mohun",
    author_email="calvin@philmohun.com",
    url="https://github.com/pmohun/calvin",
)

DESCRIPTION = "Simple premade prompts for interacting with GPT-3"
LONG_DESCRIPTION = """
**calvin** is a Python package that provides premade prompts for interacting with language models like GPT-3. It simplifies the learning curve by providing ease to use examples and sample text to get started. Additionally, it has the broader goal
of becoming **the most comprehensive repository of prompts for interacting with language models.**
"""

DISTNAME = "calvin"
LICENSE = "MIT"
AUTHOR = "philmohun"
EMAIL = "calvin@philmohun.com"
URL = ""
DOWNLOAD_URL = ""
PROJECT_URLS = {
    "Bug Tracker": "https://github.com/pmohun/calvin/issues",
    "Documentation": "https://github.com/pmohun/calvin
    "Source Code": "https://github.com/pmohun/calvin",
}
CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Environment :: Console",
    "Operating System :: OS Independent",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Topic :: Scientific/Engineering",
    "Topic :: Communications :: Chat",
]