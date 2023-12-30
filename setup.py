from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)->list[str]:
    """Func returns list of reqs"""
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements
            

setup(
    name="mlproject",
    version="0.0.1",
    author="Beechhceeb",
    author_email="beechhceeb@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)