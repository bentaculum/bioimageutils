from setuptools import setup, find_packages

setup(
    name="bioimageutils",
    version="0.1",
    description="Reoccuring utility functions and scripts for ML on bioimages",
    url="https://github.com/bentaculum/bioimageutils",
    author="Benjamin Gallusser",
    author_email="benjamin.gallusser@epfl.ch",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pre-commit",
        "pytest",
        "black",
        "numpy",
        "scikit-image",
    ],
)
