from PyQt5 import QtCore, QtWidgets


class MenuButton(QtWidgets.QPushButton):

    def __init__(self, name):

        # INIT
        super(MenuButton, self).__init__()

        # PRIVATE ATTRIBUTES
        self.__name = name

        # SETUP STYLE SHEET
        self.setStyleSheet(
            """
            QPushButton
            {
                background-color: #729E9E;
                border-radius: none;
                color: #FFFFFF;
                font: 13pt bold "Ubuntu";
                height: 26px;
                width: 26px;
            }

            QPushButton:hover
            {
                background-color: #164850;
                color: #000000;
            }

            QPushButton:checked
            {
                background-color: #164850;
                color: #000000;
            }
            """
        )

        # GENERAL CONFIG
        self.setText(self.__name)
        self.setFixedHeight(70)
        self.setCheckable(True)
        self.setAutoExclusive(True)