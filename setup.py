import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name = 'pylond',
    version = '0.0.1',
    description = 'Python 3 package that provides Icelandic translations of countries, nationalities and languages',
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
         'Programming Language :: Python :: 3',
    ],
    keywords='iceland, icelandic-language, localization',
    license = 'MIT',
    packages=['pylond'],
    install_requires=[],
    extras_require={'dev': ['pytest']}
    )