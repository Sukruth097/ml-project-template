from setuptools import setup,find_packages

from typing import List

#Declaring variables for setup functions
PROJECT_NAME="laptop-price-prediction"
VERSION="0.0.1"
AUTHOR="Sukruth A V"
DESRCIPTION="This is a laptop price prediction Machine Learning Project"

REQUIREMENT_FILE_NAME="requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirenments_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """

    with open(REQUIREMENT_FILE_NAME,'r') as file:
        requirement_list = file.readlines()
        requirement_list = [requirement.replace('\n','') for requirement in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESRCIPTION,
    packages = find_packages(),
    install_requires = get_requirenments_list()
)



