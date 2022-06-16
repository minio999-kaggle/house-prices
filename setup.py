from setuptools import setup, find_packages

with open("LICENSE") as file:
    license = file.read() 

with open("requirements.txt") as file:
    requirements = file.read().splitlines()

setup(
    name="app",
    version='0.1.0',
    description='Predicting house prices',
    author='Dominik Mińkowski',
    author_email='minkowskidominik03@gmail.com',
    url='',
    license=license,
    include_package_data=True,
    package_dir={"":"src"},
    packages=find_packages(where='src'),
    install_requires=requirements,
)