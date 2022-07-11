import os, inspect, sys

from PyQt5.QtWidgets import QWidget, QLineEdit, QGridLayout, QLabel, \
    QHBoxLayout, qApp
from PyQt5.QtCore import Qt
from pyqt_resource_helper import PyQtResourceHelper
from pyqt_svg_label import SvgLabel


class InstantSearchBar(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # search bar label
        self.__label = QLabel()

        self._initUi()

    def _initUi(self):
        self.__searchLineEdit = QLineEdit()
        self.__searchIconLbl = SvgLabel()
        ps = qApp.font().pointSize()
        self.__searchIconLbl.setFixedSize(ps * 1.5, ps * 1.5)

        self.__searchBar = QWidget()
        self.__searchBar.setObjectName('searchBar')

        lay = QHBoxLayout()
        lay.addWidget(self.__searchIconLbl)
        lay.addWidget(self.__searchLineEdit)
        self.__searchBar.setLayout(lay)
        lay.setContentsMargins(ps // 2, 0, 0, 0)
        lay.setSpacing(0)

        self.__searchLineEdit.setFocus()

        self.setAutoFillBackground(True)

        lay = QHBoxLayout()
        lay.addWidget(self.__searchBar)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(2)

        self._topWidget = QWidget()
        self._topWidget.setLayout(lay)

        lay = QGridLayout()
        lay.addWidget(self._topWidget)

        searchWidget = QWidget()
        searchWidget.setLayout(lay)
        lay.setContentsMargins(0, 0, 0, 0)

        lay = QGridLayout()
        lay.addWidget(searchWidget)
        lay.setContentsMargins(0, 0, 0, 0)

        self.__setStyle()

        self.setLayout(lay)

    # ex) searchBar.setLabel(True, 'Search Text')
    def setLabel(self, visibility: bool = True, text=None):
        if text:
            self.__label.setText(text)
        self.__label.setVisible(visibility)

    def __setStyle(self):
        self.__searchIconLbl.setSvgFile('ico/search.svg')
        PyQtResourceHelper.setStyleSheet([self.__searchLineEdit, self.__searchBar, self],
                                         ['style/lineedit.css', 'style/search_bar.css', 'style/widget.css'])

    def setSearchIcon(self, icon_filename: str):
        self.__searchIconLbl.setIcon(icon_filename)

    def setPlaceHolder(self, text: str):
        self.__searchLineEdit.setPlaceholderText(text)

    def getSearchBar(self):
        return self.__searchLineEdit

    def getSearchLineEdit(self):
        return self.__searchLineEdit

    def getSearchLabel(self):
        return self.__searchIconLbl

    def showEvent(self, e):
        self.__searchLineEdit.setFocus()
