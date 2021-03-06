from setuptools import setup, find_packages

setup(
    name='XRD/FTIR Data Processing Tool Suite',
    version='1.0',
    packages=find_packages(include=['Code', 'Code.*']),
    install_requires=[
        'pytest',
        'numpy',
        'pandas',
        'scipy',
        'lmfit',
        'sklearn',
        'pdfTex'
    ]
)