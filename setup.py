from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-auto-search-bar',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_auto_search_bar.style': ['lineedit.css', 'search_bar.css', 'widget.css'],
                  'pyqt_auto_search_bar.ico': ['search.svg']},
    description='PyQt auto search bar',
    url='https://github.com/yjg30737/pyqt-auto-search-bar.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper>=0.0.1',
        'pyqt-svg-label>=0.0.1'
    ]
)