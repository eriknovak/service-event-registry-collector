from setuptools import setup, find_packages

setup(
    name="collector",
    version="1.0.0",
    description="Setting up the Event Registry Collector CLI",
    author="Erik Novak",
    author_email="erik.novak@ijs.si",
    packages=find_packages(include=["collector", "collector.*"]),
    install_requires=["eventregistry==8.6.1", "requests", "urllib3", "python-dotenv"],
    entry_points={"console_scripts": ["collect=collector.__main__:main"]},
    setup_requires=["flake8"],
)
