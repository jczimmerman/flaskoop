import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="flask-oop"
    version="0.0.1",
    author="Joe Zimmerman",
    author_email="joeyzimmerman17@gmail.com",
    description="Flask version of my adventure game.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
