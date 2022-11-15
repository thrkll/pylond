import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name = 'pylond',
    version = '1.0.0',
    author = 'Þorkell Einarsson',
    author_email = 'thorkell@thorkell.lv',
    description = 'pylond provides translations of countries and nationalities into Icelandic',
    long_description = long_description
    long_description_content_type = 'text/markdown'
    license = 'MIT',
    url = 'https://github.com/thrkll/pylond',
    install_requires = [numpy>=1.19.0])