import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name = 'pylond',
    version = '0.0.1',
    author = 'Þorkell Einarsson',
    author_email = 'thorkell@thorkell.lv',
    description = 'pylond provides translations of countries and nationalities into Icelandic',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    license = 'MIT',
    url = 'https://github.com/thrkll/pylond',
    packages = ['pylond']
    )