from setuptools import setup, find_packages

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
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main',
        'pyqt-svg-label @ git+https://git@github.com/yjg30737/pyqt-svg-label.git@main'
    ]
)