from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pandas_md_summary',
    version='0.0.1',
    url='https://github.com/prasannals/pandas_markdown_summary',
    license='MIT',
    author='Prasanna Lakkur Subramanyam',
    author_email='prasanna.lakkur@gmail.com',
    description="A library to generate markdown summaries of pandas DataFrame and Series",
    long_description=long_description,
    py_modules=['pandas_md_summary'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'matplotlib',
        'pandas>=1.0.3'
    ]
)