import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Utilities-Lib",
    version="0.0.1",
    author="HipyCas",
    author_email="hipycas+python@gmail.com",
    description="A set of useful classes and functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HipyCas/Utilities-Lib-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

