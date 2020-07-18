import os

from setuptools import find_packages, setup

version_contents = {}
with open(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "openai/version.py")
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
