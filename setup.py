import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jax-loss",
    version="0.0.1",
    author="Devin de Hueck",
    author_email="d.dehueck@gmail.com",
    description="A jax library of common machine learning loss functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ddehueck/jax-loss",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)