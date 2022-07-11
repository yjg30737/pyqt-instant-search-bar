# pyqt-instant-search-bar
PyQt instant search bar - instant search friendly GUI.

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-instant-search-bar`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>
* <a href="https://github.com/yjg30737/pyqt-svg-label.git">pyqt-svg-label</a>

## Methods Overview
* #### `setLabel(visibility: bool = True, text=None)`
Set the visibility of search icon. You can set the text with this function too.
* #### `setSearchIcon(icon_filename: str)`
Set the icon. icon should be svg file.
* #### `setPlaceHolder(text: str)`
* #### `getSearchBar()`
* #### `getSearchLineEdit()`
* #### `getSearchLabel()`

## Preview
Code Sample

```python
from PyQt5.QtWidgets import QApplication
from pyqt_instant_search_bar import InstantSearchBar

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    searchBar = InstantSearchBar()
    searchBar.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/155654257-4d31a17a-fc64-4292-aecc-cf46a9580f18.png)

## See Also

* <a href="https://github.com/yjg30737/pyqt-search-bar-menu.git">pyqt-search-bar-menu</a> - QMenu which has search bar as a first item to help you search the menu items.
* <a href="https://github.com/yjg30737/pyqt-search-bar.git">pyqt-search-bar</a> - This supports search button.
