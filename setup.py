import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
setuptools.setup(
    name="cbim_utils",
    version="0.0.1",
    author_email="m.martinelli@cbim.it",
    description="Various utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=requirements
    
)