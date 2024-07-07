from setuptools import setup, find_packages

setup(
    name='data_gen',  
    version='0.1.0',  
    description='A utility package for ML Projects', 

    packages=find_packages(), 
  
    entry_points={  
        'console_scripts': [
            'data-gen=data_gen.cli:main',  
        ],
    },
)

