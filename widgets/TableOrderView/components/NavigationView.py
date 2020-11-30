from PyQt5 import QtCore, QtWidgets
from .MenuNavigation import MenuNavigation
from .MenuView import MenuView


class NavigationView(QtWidgets.QFrame):

    def __init__(self):

        # INIT
        super(NavigationView, self).__init__()

        # CONFIG BASE LAYOUT
        self.__layout = QtWidgets.QVBoxLayout()
        self.__layout.setContentsMargins(QtCore.QMargins(0,0,0,0))
        self.__layout.setSpacing(0)

        self.__layout.addWidget(MenuNavigation())
        self.__layout.addWidget(MenuView.getInstance())

        # SETUP LAYOUT
        self.setLayout(self.__layout)
