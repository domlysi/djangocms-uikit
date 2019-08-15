import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djangocms-uikit',
    version='0.1.3',
    packages=find_packages(exclude=('djangocms_uikit_wrapper',)),
    include_package_data=True,
    license='BSD License',  # example license
    description='A UiKit Plugin for the DjangoCMS Framework',
    long_description=README,
    url='https://github.com/domlysi/djangocms-uikit',
    author='Dominik Lysiak',
    author_email='dominik.lysiak@freenet.de',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
