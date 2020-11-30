from PyQt5 import QtCore, QtWidgets
from .Shared import *


class CheckoutView(QtWidgets.QFrame):

    __instance = None

    def __init__(self):

        if CheckoutView.__instance == None:
            # INIT
            super(CheckoutView, self).__init__()

            # WIDGETS
            totalView = QtWidgets.QFrame()
            totalView.setStyleSheet(
                """
                QFrame
                {
                    border: none;
                }
                """
            )

            totalLabel = QtWidgets.QLabel()
            totalLabel.setText('TOTAL:')
            totalLabel.setStyleSheet(QLABEL_STYLE_3)

            self.amountLabel = QtWidgets.QLabel()
            self.amountLabel.setText('0')
            self.amountLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.amountLabel.setStyleSheet(QLABEL_STYLE_3)

            dollarLabel = QtWidgets.QLabel()
            dollarLabel.setText('$')
            dollarLabel.setFixedWidth(20)
            dollarLabel.setStyleSheet(QLABEL_STYLE_1)

            totalLayout = QtWidgets.QHBoxLayout()
            totalLayout.addWidget(totalLabel)
            totalLayout.addWidget(self.amountLabel)
            totalLayout.addWidget(dollarLabel)

            totalView.setLayout(totalLayout)

            checkoutButton = QtWidgets.QPushButton()
            checkoutButton.setFixedHeight(70)
            checkoutButton.setText('CHECKOUT')
            checkoutButton.setStyleSheet(
                """
                QPushButton
                {
                    color: #FFFFFF;
                    background-color: #FF6B6B;
                    border: none;
                    border-radius: 6px;
                    font: 14pt "Ubuntu";
                    letter-spacing: 0.3em;
                }

                QPushButton:hover
                {
                    color: #000000;
                    background-color: #FBB5B1;
                    border: 3px solid #FF6B6B;
                }
                """
            )

            # CONFIG LAYOUT
            self.__layout = QtWidgets.QVBoxLayout()
            self.__layout.setContentsMargins(QtCore.QMargins(9,9,9,9))
            self.__layout.setSpacing(6)
            self.__layout.addWidget(totalView)
            self.__layout.addWidget(checkoutButton)

            # GENERAL CONFIG
            self.setFixedHeight(150)

            # SETUP STYLE SHEET
            self.setStyleSheet(
                """
                QFrame
                {
                    background-color: #FCC8C5;
                    border: none;
                    border-top: 1px solid #FBB5B1;
                }
                """
            )

            # SETUP LAYOUT
            self.setLayout(self.__layout)

            CheckoutView.__instance = self
        else:
            raise Exception('CheckoutView is singleton!')
    
    @staticmethod
    def getInstance():
        if CheckoutView.__instance == None:
            CheckoutView()
        
        return CheckoutView.__instance