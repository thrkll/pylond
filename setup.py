import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name = 'pylond',
    version = '0.1.0',
    description = 'Icelandic translations of countries, nationalities and languages',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/thrkll/pylond',
    author = 'Þorkell Einarsson',
    author_email = 'thorkell@thorkell.lv',
    classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Natural Language :: Icelandic',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Internationalization',
            'Topic :: Software Development :: Localization',
            'Topic :: Utilities'
    ],
    keywords='iso639, iso3166, localization, iceland, icelandic-language',
    license = 'MIT',
    packages=['pylond'],
    install_requires=['numpy'],
    extras_require={'dev': ['pytest']}
    )