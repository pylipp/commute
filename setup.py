from setuptools import setup, find_packages

setup(
    name='commute',
    use_scm_version=True,
    description='Tool to list public transport schedules for commuting',
    url='https://github.com/pylipp/commute',
    author='Philipp Metzner',
    author_email='beth.aleph@yahoo.de',
    license='GPLv3',
    py_modules=["main"],
    entry_points = {
        'console_scripts': ['commute = main:main']
        },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
    setup_requires=["setuptools_scm"],
    install_requires=[
        "mvg-api@git+https://github.com/leftshift/python_mvg_api.git@e943888293a0706a212360fad4d99c7bac6acf5d#egg=mvg-api",
    ],
    extras_require={
        "dev": [
            "twine",
            "wheel",
            "setuptools",
            "flake8",
        ],
    },
)
