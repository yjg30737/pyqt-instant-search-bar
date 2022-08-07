# pyqt-instant-search-bar

![image](https://user-images.githubusercontent.com/55078043/155654257-4d31a17a-fc64-4292-aecc-cf46a9580f18.png)

PyQt instant search bar.

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-instant-search-bar`

## Included Packages
* <a href="https://github.com/spyder-ide/qtpy.git">qtpy</a> - Make this module support not only PyQt5 but also PyQt6, PySide2, PySide6 
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>
* <a href="https://github.com/yjg30737/pyqt-svg-label.git">pyqt-svg-label</a>

## Methods/Signal Overview
* #### `setLabel(visibility: bool = True, text=None)`
Set the visibility of search icon. You can set the text with this function too.
* #### `setSearchIcon(icon_filename: str)`
Set the icon. icon should be svg file.
* #### `setPlaceHolder(text: str)`
* #### `getSearchBar()`
* #### `getSearchLineEdit()`
* #### `getSearchLabel()`
* ## `searched(text: str)` signal to get the text which is written in the search bar. See the example below.

## Preview
Code Sample

```python
from PyQt5.QtWidgets import QApplication
from pyqt_instant_search_bar import InstantSearchBar

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    searchBar = InstantSearchBar()
    searchBar.searched.connect(print) # print the written text
    searchBar.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/155654257-4d31a17a-fc64-4292-aecc-cf46a9580f18.png)

## See Also

* <a href="https://github.com/yjg30737/pyqt-search-bar-menu.git">pyqt-search-bar-menu</a> - QMenu which has search bar as a first item to help you search the menu items.
* <a href="https://github.com/yjg30737/pyqt-search-bar.git">pyqt-search-bar</a> - This supports search button. (click to search, not instant search)
* <a href="https://github.com/yjg30737/pyqt-database-example.git">pyqt-database-example</a> - Search the sql database table(using QSqlTableModel) with instant search bar.
