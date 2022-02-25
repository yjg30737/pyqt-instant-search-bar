# pyqt-auto-search-bar
PyQt Auto Search Bar

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-auto-search-bar.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>
* <a href="https://github.com/yjg30737/pyqt-svg-label.git">pyqt-svg-label</a>

## Preview
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_auto_search_bar import AutoSearchBar


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    searchBar = AutoSearchBar()
    searchBar.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/155654257-4d31a17a-fc64-4292-aecc-cf46a9580f18.png)
