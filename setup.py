from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ctipy',
    version='0.1.6',
    author='Yuriy Volkov',
    author_email='yurijvolkov1@yandex.ru',
    description='Small package for easily uploading data to Confluence.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yurijvolkov/ctipy',
    packages=find_packages(),
    install_requires=['atlassian-python-api-cti',
                      'pandas']
)
