from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
  '''
  this functions returns list of requirements
  '''  
  requirements=[]
  Hypen_e_dot="-e ."
  with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.replace("\n","") for req in requirements]

    if Hypen_e_dot in requirements:
      requirements.remove(Hypen_e_dot)
  return requirements


setup(
name='mlproject',
version='0.0.1',
author='Darren',
author_email='darrendsouza66@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)