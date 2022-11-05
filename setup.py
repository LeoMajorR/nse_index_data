import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='nse_data',
    author='Ravi Singh',
    author_email='ssingh.raviprakash@gmail.com',
    description='A package to get data from NSE India',
    keywords='NSE, NSE India, NSE Data, NSE Data API, NSE Data Package, NSE Data Python, NSE Data Python Package, NSE Data Python API, NSE Data Python Module, NSE Data Python Library, NSE Data Python Wrapper, NSE Data Python Wrapper Package, NSE Data Python Wrapper API, NSE Data Python Wrapper Module, NSE Data Python Wrapper Library, NSE Data Python Wrapper Wrapper, NSE Data Python Wrapper Wrapper Package, NSE Data Python Wrapper Wrapper API, NSE Data Python Wrapper Wrapper Module, NSE Data Python Wrapper Wrapper Library, NSE Data Python Wrapper Wrapper Wrapper, NSE Data Python Wrapper Wrapper Wrapper Package, NSE Data Python Wrapper Wrapper Wrapper API, NSE Data Python Wrapper Wrapper Wrapper Module, NSE Data Python Wrapper Wrapper Wrapper Library, NSE Data Python Wrapper Wrapper Wrapper Wrapper, NSE Data Python Wrapper Wrapper Wrapper Wrapper Package, NSE Data Python Wrapper Wrapper Wrapper Wrapper API, NSE Data Python Wrapper Wrapper Wrapper Wrapper Module, NSE Data Python Wrapper Wrapper Wrapper Wrapper Library, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Package, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper API, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Module, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Library, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Package, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper API, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Module, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Library, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Package, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper API, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Module, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Library, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Package, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper API, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Module, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Library, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Wrapper Package, NSE Data Python Wrapper Wrapper Wrapper Wrapper Wrapper',
    url='https://github.com/leomajorr/nse_index_data',
    project_urls={
        'Documentation': 'https://github.com/leomajorr/nse_index_data',
        'Bug Reports':
        'https://github.com/leomajorr/nse_index_data/issues',
        'Source Code': 'https://github.com/leomajorr/nse_index_data',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers, Financial and Insurance Industry, Education, Science/Research, Information Technology',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=examplepy:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
    #     ],
    # },
)
