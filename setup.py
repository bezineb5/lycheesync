
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    reqs = f.read().strip().split('\n')

setup(
    name="lycheesync",
    version="3.0.10",
    author="Gustave Pate",
    author_email="gustave.pate@fake.com",
    description="Photo synchronization utility for Lychee",
    license="MIT",
    url="http://github.com/GustavePate/lycheesync",
    packages=find_packages(),
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        'console_scripts': [
            'lycheesync=lycheesync.sync:main',
        ]
    },
    install_requires=reqs,
)
