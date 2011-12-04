try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
        'description': 'My Project',
        'author': 'Michael Morisy',
        'url': 'URL to get it at'
        'download_url': 'URL to download it',
        'author_email': 'morisy@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname'
}

setup(**config)


