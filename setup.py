from setuptools import setup, find_packages

setup(
    name='python-pong',
    version='1.0.0',
    author="Dyrektrypt",
    description="A Python library containing components and implementations of the game Pong for Pygame",
    packages=find_packages(include=["pong, pong.*"]),
    install_requires=["pygame"]
)
