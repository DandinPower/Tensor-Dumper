from setuptools import setup, find_packages

setup(
    name="dumper",
    version="0.1",
    packages=find_packages(),
    description='A simple tensor dumper',
    author='Joseph Liaw',
    author_email='tomhot246@gmail.com',
    url='https://github.com/DandinPower/Tensor-Dumper',
    install_requires=[
        'numpy',
        'torch',
    ],
)