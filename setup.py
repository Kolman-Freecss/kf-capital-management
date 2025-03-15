from setuptools import setup, find_packages

setup(
    name='kf-capital-management',
    version='0.1.0',
    description='A desktop/mobile application for capital management',
    author='Kolman-Freecss',
    url='https://github.com/Kolman-Freecss/kf-capital-management',
    packages=find_packages(),
    install_requires=[
        'kivy',
        'pandas',
        'matplotlib',
        'python-cron',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'kf-capital-management=src.main:main',
        ],
    },
)
