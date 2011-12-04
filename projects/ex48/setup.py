try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
        'description': 'Lexicon',
        'author': 'Michael Morisy',
        'url': 'URL to get it at'
        'download_url': 'URL to download it',
        'author_email': 'morisy@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['lexicon'],
        'scripts': [],
        'name': 'lexicon'
}

setup(**config)


