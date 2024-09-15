from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pandas-notion',
    version='0.1.0',
    author='jarias',
    author_email='jacinto.arias@taidy.cloud',
    description='A package to convert Notion databases to Pandas DataFrames',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/demosense/pandas-notion',
    project_urls={
        'Bug Tracker': 'https://github.com/demosense/pandas-notion/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'pandas>=1.0',
        'requests>=2.0',
    ],
)