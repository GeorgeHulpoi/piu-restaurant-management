from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton

from ..shared.Colors import Colors
from ..shared.Constants import Constants


class ListItem(QFrame):

    def __init__(self, item, hook):

        # call super
        super(ListItem, self).__init__()

        # get arguments
        self.hook = hook
        self.title = item.getTitle()
        self.price = item.getPrice()
        self.qty = 0

        # setup and config
        self.setObjectName("parent")
        self.setStyleSheet(f"""
            QFrame {{
                min-height: 50px;
                max-height: 50px;
                min-width: 340px;
                max-width: 340px;
                padding: 0px 10px 0px 10px;
            }}

            QFrame#parent {{
                border: 1px solid {Colors.BLACK};
                border-radius: 6px;
                margin-left: 19px;
            }}

            QPushButton {{
                background-color: {Colors.BLACK};
                border: none;
                color: {Colors.WHITE};
                min-width: 30px;
                max-width: 30px;
                min-height: 30px;
                max-height: 30px;
                border-radius: 15px;
                font-size: 20px;
            }}

            QLabel {{
                font-size: 20px;
            }}

            QLabel#qty {{
                max-width: 50px;
                min-width: 50px;
            }}
        """)

        # define widgets
        self.label_qty = QLabel()
        self.label_qty.setText(f"{self.qty}")
        self.label_qty.setObjectName("qty")
        self.label_qty.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)

        label_title = QLabel()
        label_title.setText(self.title)
        label_title.setObjectName("title")

        btn_add = QPushButton()
        btn_add.setText("+")

        btn_rmv = QPushButton()
        btn_rmv.setText("-")

        # define button actions
        btn_add.clicked.connect(lambda x: self.raiseQty())
        btn_rmv.clicked.connect(lambda x: self.lowerQty())

        # setup layout
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(Constants.QLAYOUT_NO_MARGINS)
        self.layout().setSpacing(0)

        # add widgets
        self.layout().addWidget(label_title)
        self.layout().addWidget(btn_rmv)
        self.layout().addWidget(self.label_qty)
        self.layout().addWidget(btn_add)

    def raiseQty(self):
        if not self.qty.__eq__(999):
            self.qty += 1
            self.updateQty()
            self.hook.raiseTotalPrice(self)

    def lowerQty(self):
        if not self.qty.__eq__(0):
            self.qty -= 1
            self.updateQty()
            self.hook.lowerTotalPrice(self)

    def updateQty(self):
        self.label_qty.setText(f"{self.qty}")

    def getTitle(self):
        return self.title

    def getPrice(self):
        return self.price

    def getQty(self):
        return self.qty
