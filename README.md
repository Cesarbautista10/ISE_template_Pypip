
# ISE_template_Pypip

This repository is focused on building MicroPython projects using Thonny, a free code editor, and implementing new mechanics to cater to a wider audience.

> [!NOTE]
> This repository is tailored for Windows operating systems.

Firstly, you need an account on [PyPI](https://pypi.org/account/login/), an index where you can find multiple libraries and package projects for various Python applications.

> [!WARNING]
> You need to configure a token in your local file named `.pypirc` located at `"C:/Users/YourUserName/.pypirc"`.
> ```python
> [pypi]
> username = __token__
> password = <PyPI token>
> ```

You can register and upload your projects, focusing on applications utilizing microcontroller technologies and free code, as they are essential for progress. For more information, read [here](https://packaging.python.org/en/latest/specifications/pypirc/).

## Environment

You need to install two libraries:

```bash
pip install --upgrade twine
```

and

```bash
pip install wheel
```

## Files

The following files are necessary for building the project.


Create your file using a simple class as an example:

```python
# calculator.py
class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        return sum(self.numbers)

    def subtract(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result -= num
        return result

    def multiply(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result *= num
        return result

    def divide(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result /= num
        return result
```

Save your file in an independent directory `./package/calculator.py`. In a file `__init__.py`, import the library before:

```python
# __init__.py

from package.calculator import Calculator
```

> [!CAUTION]
> The filename is `calculator.py`, and the class used is `Calculator`.


The directory structure is as follows:

```bash
./package/ 
    __init__.py
    calculator.py
```

> [!NOTE] "package" is a placeholder name for the package. You can rename this directory and its files as needed.## MANIFEST.in

The ***MANIFEST.in*** file is a resource for saving the structure of the package. It's recommended to use this structure:

```
include README.md
include LICENSE
recursive-include resource *.py
```

Finally, the ***setup.py*** file saves the configuration metadata necessary for building the project. The recommendation for use is to add the following features:

```python
import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.x.x'
PACKAGE_NAME = 'package'
AUTHOR = 'Author name'
AUTHOR_EMAIL = 'name@email.com'
LICENSE = 'License'
DESCRIPTION = 'Description about the project.'
# Read the contents of your README file for the long description
with open('README.md', 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# Add your required packages to INSTALL_REQUIRES list
INSTALL_REQUIRES = []

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',  # Specify the type of content
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)
```

## Build

To build, simply run the following command:

```
python setup.py sdist bdist_wheel
```

The result will be new directories:

```
build
dist
package.egg-info
```

Check the configuration before uploading:

```
twine check dist/*
```

The result in the console should be:

```
    Checking dist/package-0.1-py3-none-any.whl: PASSED
    Checking dist/package-0.1.tar.gz: PASSED
```

Finally, upload the project:

```
twine upload dist/*
```

If everything is good, you can see the project deployed on Windows PyPI.

Mode of use:

Install the version package in Thonny, for example:

![Thonny install](https://raw.githubusercontent.com/Cesarbautista10/ISE_SSD1306/main/Images/ins.png)
