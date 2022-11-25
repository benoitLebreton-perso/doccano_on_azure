from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='doccano-on-azure',
      version='1.0',
      description='Python doccano client',
      author='Quantmetry',
      author_email='',
      install_requires=required,
      packages=find_packages()
     )