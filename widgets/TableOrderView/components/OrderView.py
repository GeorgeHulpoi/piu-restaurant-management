from PyQt5 import QtCore, QtGui, QtWidgets
from .OrderList import OrderList
from .CheckoutView import CheckoutView


class OrderView(QtWidgets.QWidget):

    __instance = None

    def __init__(self):
        if OrderView.__instance is None:

            # CALL SUPER
            super(OrderView, self).__init__()
            
            # DECLARE NEW WIDGETS
            self.orderList = OrderList.getInstance()
            self.checkout = CheckoutView()
            
            # SETUP AND CONFIG LAYOUT
            self.setLayout(QtWidgets.QVBoxLayout())
            self.layout().setContentsMargins(QtCore.QMargins(0,0,0,0))
            self.layout().setSpacing(0)

            # ADD WIDGETS
            self.layout().addWidget(self.orderList)
            self.layout().addWidget(self.checkout)

            # CONFIG SELF
            self.setFixedWidth(self.orderList.width())

            # SET INSTANCE TO SELF
            OrderView.__instance = self

        else:
            raise Exception('OrderView is singleton!')

    @staticmethod
    def getInstance():
        if OrderView.__instance is None:
            OrderView()
        
        return OrderView.__instance
