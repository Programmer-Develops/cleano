from setuptools import setup, find_packages

setup(
    name='cleano',
    version='0.1.0',
    author='Shantanu Pandya',
    author_email='programmerdevelops@gmail.com',
    description='A Python package for data cleaning and preprocessing.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scikit-learn>=0.24.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scipy>=1.7.0"
    ],
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)