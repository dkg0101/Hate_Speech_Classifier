from setuptools import find_packages, setup

def get_requirements_list():
    req_list = []
    with open('requirements.txt','r+') as file:
        req_list = file.readlines()
        req_list = [obj.replace('\n','') for obj in req_list]

    if '-e .' in req_list:
        req_list.remove('-e .')

    return req_list

setup(
    name="hate-speech-classification",
    version="0.0.1",
    author="iNeuron",
    author_email="dkg@gmail.com",
    packages=find_packages(),
    install_requires=[]
)


# if __name__=='__main__':
#     get_requirements_list()