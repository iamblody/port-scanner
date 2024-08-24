from setuptools import setup

setup(
    name='port_scanner',
    version='0.1',
    scripts=['bps.py'],
    install_requires=[
        'colorama',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
