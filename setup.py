import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colada",
    version="0.0.1",
    author="Sourabh Maity",
    author_email="maity.sourabh13@gmail.com",
    description="IPython magic extension to run CUDA C code on Google colab.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sourabhXIII/colada",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
