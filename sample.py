from PyQt5.QtWidgets import QApplication
from pyqt_instant_search_bar import InstantSearchBar

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    searchBar = InstantSearchBar()
    searchBar.searched.connect(print) # print the written text
    searchBar.show()
    app.exec_()