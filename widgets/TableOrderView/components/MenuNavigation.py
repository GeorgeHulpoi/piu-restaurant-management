from PyQt5 import QtCore, QtWidgets
from .MenuView import MenuView
from .MenuButton import MenuButton


class MenuNavigation(QtWidgets.QFrame):

    def __init__(self):

        # INIT
        super(MenuNavigation, self).__init__()

        # SETUP STYLE SHEET
        self.setStyleSheet(
            """
            QFrame
            {
                background-color: red;
            }
            """
        )

        # CONFIG BASE LAYOUT
        self.__layout = QtWidgets.QHBoxLayout()
        self.__layout.setContentsMargins(QtCore.QMargins(0,0,0,0))
        self.__layout.setSpacing(0)

        # COPY OF MENU VIEW
        menuView = MenuView.getInstance()

        foodButton = MenuButton('Food')
        foodButton.clicked.connect(lambda: menuView.setCurrentIndex(0))

        drinksButton = MenuButton('Drinks')
        drinksButton.clicked.connect(lambda: menuView.setCurrentIndex(1))
        
        dessertsButton = MenuButton('Desserts')
        dessertsButton.clicked.connect(lambda: menuView.setCurrentIndex(2))
        
        self.__layout.addWidget(foodButton)
        self.__layout.addWidget(drinksButton)
        self.__layout.addWidget(dessertsButton)

        # GENERAL CONFIG
        self.setFixedHeight(70)
        
        # SETUP LAYOUT
        self.setLayout(self.__layout)