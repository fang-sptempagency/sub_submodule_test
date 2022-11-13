import setuptools
from glob import glob
from os.path import basename
from os.path import splitext

with open("README.md", "r") as fh:
    long_description = fh.read()

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setuptools.setup(
    name="subsubmodule",
    version="1.0.0",
    author="fang",
    author_email="fang.sptempagency.fiction@gmail.com",
    description="show the image of saginuma",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fang-sptempagency/sub_submodule_test",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requires=_requires_from_file('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)