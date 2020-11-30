from PyQt5 import QtCore, QtGui, QtWidgets
from .Shared import *
from .CheckoutView import CheckoutView


class QtyButton(QtWidgets.QPushButton):

    def __init__(self, text):

        # CALL SUPER
        super(QtyButton, self).__init__()
        
        # SETUP STYLE SHEET
        self.setStyleSheet(
            """
            QPushButton
            {
                border: 1px solid #164850;
                border-radius: 12px;
                color: #FFFFFF;
                font: 13pt bold "Ubuntu";
                height: 26px;
                margin-left: 10px;
                margin-right: 10px;
                width: 26px;
            }

            QPushButton:hover
            {
                background-color: #164850;
                color: #000000;
            }

            QPushButton:hover:pressed
            {
                background-color: #4ECDC4;
            }
            """
        )

        # SETUP TEXT
        self.setText(text)


class OrderListItem(QtWidgets.QFrame):

    def __init__(self, name, price):

        # CALL SUPER
        super(OrderListItem, self).__init__()
        
        # PRIVATE ATTRIBUTES
        self.__name = name
        self.__price = price
        self.__checkoutPrice = price
        self.__qty = 1

        # GET INSTANCE OF CHECKOUT VIEW
        self.checkout = CheckoutView.getInstance()

        # ADJUST THE BILL
        amountValue = int(self.checkout.amountLabel.text())
        amountValue += self.__price
        self.checkout.amountLabel.setText(str(amountValue))

        # DECLARE NEW WIDGETS
        self.__addButton = QtyButton('+')
        self.__addButton.clicked.connect(lambda: self.add())
        
        self.__removeButton = QtyButton('-')
        self.__removeButton.clicked.connect(lambda: self.remove())

        self.__currentQtyWidget = QtWidgets.QLineEdit()
        self.__currentQtyWidget.setAlignment(QtCore.Qt.AlignCenter)
        self.__currentQtyWidget.setReadOnly(True)
        self.__currentQtyWidget.setText(str(self.__qty))
        self.__currentQtyWidget.setStyleSheet(
            """
            QLineEdit
            {
                background-color: #F7FFF7;
                border-radius: 22px;
                color: #000000;
                height: 44px;
                width: 44px;
            }
            """
        )

        self.__qtyLayout = QtWidgets.QHBoxLayout()
        self.__qtyLayout.setContentsMargins(QtCore.QMargins(0,0,0,0))
        self.__qtyLayout.setSpacing(0)
        self.__qtyLayout.addWidget(self.__removeButton)
        self.__qtyLayout.addWidget(self.__currentQtyWidget)
        self.__qtyLayout.addWidget(self.__addButton)

        self.__nameWidget = QtWidgets.QLabel()
        self.__nameWidget.setText(name)
        self.__nameWidget.setFixedWidth(250)
        self.__nameWidget.setStyleSheet(QLABEL_STYLE_2)

        self.__qtyWidget = QtWidgets.QFrame()
        self.__qtyWidget.setLayout(self.__qtyLayout)

        self.__priceLabel = QtWidgets.QLabel()
        self.__priceLabel.setText(str(self.__checkoutPrice))
        self.__priceLabel.setFixedWidth(70)
        self.__priceLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.__priceLabel.setStyleSheet(QLABEL_STYLE_2)

        self.__dollarLabel = QtWidgets.QLabel()
        self.__dollarLabel.setText('$')
        self.__dollarLabel.setMinimumWidth(20)
        self.__dollarLabel.setStyleSheet(QLABEL_STYLE_1)

        # CONFIG AND SETUP LAYOUT
        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().setContentsMargins(QtCore.QMargins(10,0,10,0))
        self.layout().setSpacing(0)

        # ADD WIDGETS
        self.layout().addWidget(self.__nameWidget)
        self.layout().addWidget(QtWidgets.QFrame())
        self.layout().addWidget(self.__qtyWidget)
        self.layout().addWidget(self.__priceLabel)
        self.layout().addWidget(self.__dollarLabel)
        
        # GENERAL CONFIG
        self.setFixedHeight(70)

        # SETUP STYLE SHEET
        self.setStyleSheet(
            """
            QFrame
            {
                background-color: #1A535C;
                border-radius: 7px;
            }
            """
        )

    """
    Increase qty of an item by one and update coressponding labels.
    """
    def add(self):
        self.__qty += 1
        self.__checkoutPrice = self.__qty * self.__price
        self.__currentQtyWidget.setText(str(self.__qty))
        self.__priceLabel.setText(str(self.__checkoutPrice))
        
        amountValue = int(self.checkout.amountLabel.text())
        amountValue += self.__price

        self.checkout.amountLabel.setText(str(amountValue))

    """
    Decrease qty of an item by one and update coressponding labels.

    NOTE: qty cannot be less than zero.
    """
    def remove(self):
        if self.__qty - 1 >= 0:
            self.__qty -= 1
            self.__checkoutPrice = self.__qty * self.__price
            self.__currentQtyWidget.setText(str(self.__qty))
            self.__priceLabel.setText(str(self.__checkoutPrice))

            amountValue = int(self.checkout.amountLabel.text())
            amountValue -= self.__price

            self.checkout.amountLabel.setText(str(amountValue))


class OrderList(QtWidgets.QScrollArea):

    __instance = None

    def __init__(self):
        if OrderList.__instance == None:
            # INIT
            super(OrderList, self).__init__()

            # WIDGETS
            self.inner = QtWidgets.QWidget(self)
            self.inner.setStyleSheet('background-color: transparent;')
            self.inner.setLayout(QtWidgets.QVBoxLayout())
            self.inner.layout().setContentsMargins(QtCore.QMargins(9,9,9,9))
            self.inner.layout().addWidget(QtWidgets.QFrame(self.inner))

            # GENERAL CONFIG
            self.setFixedWidth(520)
            self.setStyleSheet(
                """
                QFrame
                {
                    background-color: #FCC8C5;
                    border: none;
                }
                """
            )
            self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.setWidgetResizable(True)
            self.setWidget(self.inner)

            OrderList.__instance = self
        else:
            raise Exception('OrderList is singleton!')

    @staticmethod
    def getInstance():
        if OrderList.__instance == None:
            OrderList()
        
        return OrderList.__instance

    """
    Adds an item to the current list of items.
    """
    @staticmethod
    def addItem(name, price):
        layout = OrderList.__instance.inner.layout()
        layout.insertWidget(layout.count() - 1, OrderListItem(name, price))
