from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Load README
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Load requirements
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    lines = f.readlines()
    requirements = [l.strip().strip('\n') for l in lines
                    if l.strip() and not l.strip().startswith('#')]

setup(
    name='upscrot',
    version='1.0.0b2',

    description='Directly upload screenshots to a SSH server.',
    long_description=long_description,

    url='https://github.com/dbrgn/upscrot/',

    author='Danilo Bargen',
    author_email='mail@dbrgn.ch',

    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Home Automation',
        'Topic :: Utilities',
    ],
    keywords='screenshot upload scrot ssh',

    packages=['upscrot'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'upscrot=upscrot.main:entrypoint',
        ],
    },
    package_data={
        '': ['README.md', 'requirements.txt'],
    },
)
