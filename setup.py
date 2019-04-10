# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

setup(
    name='homomorphic-filter',
    version='v1.0.0-alpha.0',
    description="Homomorphic filtering",
    long_description="Image enhancement using homomorphic filtering",
    keywords='Image processing',
    url='https://github.com/nikAizuddin/homomorphic-filter',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.16.2',
        'pillow>=5.4.1',
    ],
    entry_points={
        'console_scripts': [
            'homomorphic=homomorphic.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
