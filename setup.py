import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jupyda",
    version="0.0.7",
    author="Sourabh Maity",
    author_email="no-one@no-where.com",
    description="IPython magic extension to run CUDA C code on jupyter notebooks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sourabhXIII/jupyda",
    py_modules=['jupyda', 'src.magic_jupyda'],
    # packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
