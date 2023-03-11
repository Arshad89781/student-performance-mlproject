from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str):
    """Get all libraries from requirements.txt and make it as list and remove '-e .'

    Args:
        file_path (str): requirements.txt file path

    Returns:
        liat(str): list of libraries
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='studedent-performance-project',
    version='0.0.1',
    author='arshad',
    author_email='arshadalishasd@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
