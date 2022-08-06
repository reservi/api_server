# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import sys

__version__ = "0.0.0"

def read(fname):
    """Used to read long description

    Args:
    fname (str): Filename

    Returns:
    str: File content
    """
    with open(os.path.join(os.path.dirname(__file__),
                           fname)) as description_file:
        return description_file.read()


def filter_data(data):
    """Filter requirement data

    Removes white spaces, empty lines and commented out lines

    Args:
    data (str): File content

    Returns:
    array of str: Filtered lines
    """
    lines = data.split("\n")
    filtered_lines = filter(None,
                            filter(lambda line:
                                   not line.startswith("#") and not '--' in line,
                                   map(lambda line: line.strip(),
                                       lines)))

    return list(filtered_lines)


# Check version below insted of 1.0
# 'version': '_updated_by_set_version_number_',
package_information = {
    'name': 'Reservi API',
    'version': __version__,
    'description': 'API for Reservi App',
    'maintainer': 'Dawid Brylka',
    'maintainer_email': 'eurobi.123@gmail.com',
    'url': 'TBD',
    'license': 'MIT',
    'packages': find_packages(),
    'package_data': {
        'static': ['static']
    },
    'entry_points': {
        "console_scripts": [
            "reservi=app.cli.reservi:main",
        ],
    },
    'install_requires': filter_data(read("requirements.txt")),

    # Always disable support for zip eggs
    'zip_safe': False,
}

if __name__ == '__main__':
    MINIMUM_PYTHON_VERSION = (3, 9)
    if sys.version_info < MINIMUM_PYTHON_VERSION:
        raise EnvironmentError(
            f"Python version too old. Minimum Python version: {'.'.join(map(str, MINIMUM_PYTHON_VERSION))}"
        )

    setup(**package_information)