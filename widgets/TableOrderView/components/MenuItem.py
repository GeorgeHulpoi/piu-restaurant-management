from PyQt5 import QtCore, QtWidgets
from .OrderList import OrderList


class MenuItem(QtWidgets.QFrame):

    def __init__(self, name, description, price):

        # INIT
        super(MenuItem, self).__init__()

        nameWidget = QtWidgets.QLabel(name)
        nameWidget.setStyleSheet(
            """
            QLabel
            {
                border-bottom: 1px solid black;
                border-radius: none;
                font: 18pt "Ubuntu";
            }
            """
        )

        descriptionWidget = QtWidgets.QLabel(description)
        descriptionWidget.setStyleSheet(
            """
            QLabel
            {
                font: 13pt "Ubuntu";
                padding-left: 1px;
            }
            """
        )

        priceWidget = QtWidgets.QLabel('price: ' + str(price) + '$')
        priceWidget.setStyleSheet(
            """
            QLabel
            {
                border-radius: none;
                font: 14pt "Ubuntu"; 
            }
            """
        )

        addWidget = QtWidgets.QFrame()

        addButton = QtWidgets.QPushButton('ADD')
        addButton.setStyleSheet(
            """
            QPushButton
            {
                background-color: #1C7349;
                border-radius: 10px;
                color: white;
                height: 30px;
                max-width: 100px;
                max-height: 70px;
                width: 100px;
            }

            QPushButton:hover
            {
                background-color: #3ACF87;
                color: #000000;
            }
            """
        )
        addButton.clicked.connect(lambda: OrderList.getInstance().addItem(name, price))

        addWidget.setLayout(QtWidgets.QHBoxLayout())
        addWidget.layout().addWidget(priceWidget)
        addWidget.layout().addWidget(addButton)

        self.setStyleSheet(
            """
            QFrame
            {
                background-color: #729E9E;
                border-radius: 18px;
            }
            """
        )
        self.setFixedHeight(200)

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(nameWidget)
        self.layout().addWidget(descriptionWidget)
        self.layout().addWidget(addWidget)
