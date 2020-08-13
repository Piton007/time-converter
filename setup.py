
import  setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name="time-converter-Piton007",
    version="0.1",
    author="Piton007",
    author_email="josemowa45321@gmail.com",
    description="Time converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Piton007/time-converter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)