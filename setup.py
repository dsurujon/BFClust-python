from setuptools import setup

setup(
    name = 'BFClust',
    version = '0.1',
    description = 'Boundary Forest Clustering',
    url = 'https://github.com/dsurujon/BFClust-python',
    author = 'Defne Surujon',
    email = 'defnesurujon@gmail.com',
    
    scripts = ['BFC', 'BFC-augment'],
    install_requires = ['numpy', 'pandas', 'joblib', 'sklearn', 'biopython']
)