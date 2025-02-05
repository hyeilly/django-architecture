from setuptools import setup, find_packages

setup(
    name='core',
    version='0.1.0',
    packages=find_packages(include=['core', 'core.*', 'common']),  # common 패키지 포함
    install_requires=[
        "pymongo",
        "mongoengine"
    ]
)
