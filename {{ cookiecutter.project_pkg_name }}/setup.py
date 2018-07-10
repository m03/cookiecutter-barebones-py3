"""
A setuptools based setup module.
"""

import setuptools
import os


def read_long_description():
    """Read the long description text from the README.rst file"""
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.rst')
    with open(path, encoding='utf-8') as input_file:
        text = input_file.read()
    return text

setuptools.setup(
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development ',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
    data_files=[],
    description='{{ cookiecutter.project_description }}',
    entry_points={},
    extras_require={},
    include_package_data=True,
    install_requires=[
        "boltons >= 17.1.0, < 18.0.0",
    ],
    keywords='',
    license='BSD',
    long_description=read_long_description(),
    name='{{ cookiecutter.project_pkg_name }}',
    packages=[
        '{{ cookiecutter.project_module_name }}',
    ],
    package_data={},
    setup_requires=[
        "pytest-runner >= 4.2",
    ],
    tests_require=[
        "mock >= 2.0.0",
        "pytest >= 3.6.3",
        "pytest-cov >= 2.5.1",
    ],
    test_suite = 'tests',
    url='',
    version='{{ cookiecutter.version }}',
)



