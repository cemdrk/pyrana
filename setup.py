from setuptools import setup

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'waitress',
]

setup(
    name='pyrana',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = pyrana:main',
        ],
    },
)
