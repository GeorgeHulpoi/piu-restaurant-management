import json

from PyQt5 import QtCore, QtWidgets
from .MenuItem import MenuItem


class MenuPage(QtWidgets.QScrollArea):

    def __init__(self, filePath):

        # INIT
        super(MenuPage, self).__init__()

        # SETUP STYLE SHEET
        self.setStyleSheet(
            """
            QFrame
            {
                background-color: #164850;
            }
            """
        )

        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        
        self.inner = QtWidgets.QFrame(self)
        self.inner.setLayout(QtWidgets.QVBoxLayout())
        self.inner.layout().addWidget(QtWidgets.QFrame(self.inner))

        self.setWidget(self.inner)

        with open(filePath) as json_file:
            data = json.load(json_file)
                
            for x in data:
                self.addItem(x['name'], x['description'], x['price'])

    """
    Adds an item to the current list of items.
    """
    def addItem(self, name, description, price):
        layout = self.inner.layout()
        layout.insertWidget(layout.count() - 1, MenuItem(name, description, price))