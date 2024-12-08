
from setuptools import setup, find_packages

setup(
    name="ml_sdk",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "tensorflow",
        "torch",
        "boto3",
        "numpy",
    ],
    description="SDK for on-device ML model optimization and deployment",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your-repo/ml-sdk",
)
