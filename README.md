# pyqt-auto-search-bar
PyQt auto search bar which is search icon on the left only exists as a label, not clickable button. See the preview below.

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

## See Also

* <a href="https://github.com/yjg30737/pyqt-search-bar-menu.git">pyqt-search-bar-menu</a> - In this package this module's ```AutoSearchBar``` used as a ```QWidgetAction``` type top item of the menu. In ```pyqt-search-bar-menu```'s preview, you will see ```AutoSearchBar```'s feature in detail. 
* <a href="https://github.com/yjg30737/pyqt-search-bar.git">pyqt-search-bar</a> - This supports search button.
