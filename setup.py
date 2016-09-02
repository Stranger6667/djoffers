# coding: utf-8
from setuptools import setup

import djoffers


setup(
    name='djoffers',
    url='https://github.com/Stranger6667/djoffers',
    version=djoffers.__version__,
    packages=['djoffers'],
    license='MIT',
    author='Dmitry Dygalo',
    author_email='dadygalo@gmail.com',
    maintainer='Dmitry Dygalo',
    maintainer_email='dadygalo@gmail.com',
    keywords=['hasoffers', 'django', 'cache'],
    description='Django models for HasOffers',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    include_package_data=True,
    install_requires=['django>=1.9', 'pyoffers'],
)
