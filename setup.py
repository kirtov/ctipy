from setuptools import setup, find_packages

setup(
    name='ctipy',
    version='0.1.2',
    author='Yuriy Volkov',
    author_email='yurijvolkov1@yandex.ru',
    description='Small package for easily uploading data to Confluence.',
    url='https://github.com/yurijvolkov/ctipy',
    packages=find_packages(),
    install_requires=['atlassian-python-api-cti']
)
