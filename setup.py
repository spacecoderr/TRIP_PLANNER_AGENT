from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    '''
    This function will return list of requirements'''
    requirement_list:List[str]=[]
    try:
        with open('requiremnts.txt','r') as f:
            lines=f.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_list
print(get_requirements())
setup(
    name="AI-TRAVEL-PLANNER",
    version="0.0.1",
    author="prabhudatta priyadarshi",
    author_email="homospacian22@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)