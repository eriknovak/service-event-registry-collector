from setuptools import setup, find_packages

with open("README.md", mode="r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()

setup(
    name="collector",
    version="1.0.0",
    author="Erik Novak",
    author_email="erik.novak@ijs.si",
    description="Setting up the Event Registry Collector CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["collector", "collector.*"]),
    install_requires=[req for req in requirements if req[:2] != "# "],
    entry_points={"console_scripts": ["collect=collector.__main__:main"]},
    setup_requires=["flake8"],
)
