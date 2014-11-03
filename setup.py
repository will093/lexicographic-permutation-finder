try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'Lexographic Permutation Finder',
        'author': 'Will ST',
        'url': '',
        'download_url': '',
        'author_email': 'willst.willst@gmail.com',
        'version': '0.1',
        'install_requires': [],
        'packages': ['src'],
        'scripts': [],
        'name': 'Lexographic Permutation Finder'
        }

setup(**config)

