from setuptools import setup

from os import path
import sys

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='ctf-announcement',
    packages=['ctf_announcement'],
    version='0.2',
    author='numirias',
    author_email='numirias@users.noreply.github.com',
    url='https://github.com/secse-ctf/announcement',
    license='MIT',
    python_requires='>=3.5',
    install_requires=['python-dateutil', 'feedparser'],
    entry_points={
        'console_scripts': [
            'ctf-announcement = ctf_announcement.__main__:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description='Fill a CTF announcement template with data from CTFtime',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
