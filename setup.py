from distutils.core import setup
from setuptools import find_packages
import os


# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(name= "Project",
    packages=find_packages('.'), 
    version='1.0.0',
    license='3-BSD',
    description='Singer artists analysis',
    long_description = long_description,
    long_description_context_type = 'text/markdown',
    author='Maria Victoria Diaz Lopez',
    author_email='mariav1445@gmail.com',     
    url='',
    keywords=["artists", "songs", "popularity", "audio features"],
    install_requires=["pandas==1.0.4", "matplotlib==3.2.1", "numpy==1.18.4", "scipy==1.4.1", "scikit.learn==0.23.1", "seaborn==0.10.1", "statistics==1.0.3.5"],
    test_suite = 'Project.test',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Topic :: System :: Installation/Setup',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
