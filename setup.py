import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylhdc",
    version="0.0.1",
    author="Guillaume BITON",
    author_email="guillaume@gbweb.fr",
    description="A personal finance management package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gbwebdev/pylhdc",
    project_urls={
        "Bug Tracker": "https://github.com/gbwebdev/pylhdc/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)