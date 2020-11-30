from PyQt5 import QtCore, QtWidgets
from .components.OrderView import OrderView
from .components.NavigationView import NavigationView


class TableOrderView(QtWidgets.QFrame):

    def __init__(self, parent, width, height):

        # CALL SUPER
        super(TableOrderView, self).__init__(parent)

        # CONFIG FRAME
        self.width = width
        self.height = height
        self.setGeometry(0, 0, self.width, self.height)
        self.setVisible(False)

        # SETUP AND CONFIG LAYOUT
        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().setContentsMargins(QtCore.QMargins(0,0,0,0))
        self.layout().setSpacing(0)

        # ADD WIDGETS
        self.layout().addWidget(OrderView())
        self.layout().addWidget(NavigationView())
