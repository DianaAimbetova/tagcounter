import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-DianaAimbetova",
    version="0.0.1",
    author="Diana Aimbetova",
    author_email="diana_aimbetova@epam.com",
    description="A small package for tag counter application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DianaAimbetova/tagcounter/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)