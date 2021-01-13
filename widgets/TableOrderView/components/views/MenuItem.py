from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QScrollArea

from ..shared.Colors import Colors
from ..shared.Constants import Constants
from .MenuButton import MenuButton


class MenuItem(QFrame):

    def __init__(self, title, price, description):

        # call super
        super(MenuItem, self).__init__()

        # get arguments
        self.title = title
        self.price = int(price)
        self.description = description

        # setup and config
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {Colors.OXFORD_BLUE};
                min-height: 200px;
                max-height: 200px;
                color: {Colors.WHITE}
            }}

            QLabel {{
                min-height: 20px;
                max-height: 20px;
                padding: 10px;
                letter-spacing: 1px;
            }}

            QLabel#item-title {{
                font-size: 20px;
                border-bottom: 2px solid {Colors.ORANGE_WEB}
            }}
        """)

        # setup layout
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(Constants.QLAYOUT_NO_MARGINS)
        self.layout().setSpacing(0)

        # define widgets
        label_title = QLabel()
        label_title.setText(self.title)
        label_title.setObjectName("item-title")

        label_price = QLabel()
        label_price.setText(f"{self.price} $ | price")
        label_price.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        label_description = QLabel()
        label_description.setText(self.description)
        label_description.setWordWrap(True)

        self.btn_add = MenuButton("add")

        # add widgets
        self.layout().addWidget(label_title)
        self.layout().addWidget(label_description)
        self.layout().addWidget(label_price)
        self.layout().addWidget(self.btn_add)

    def getTitle(self):
        return self.title

    def getPrice(self):
        return self.price

    def connectHook(self, hook):
        self.btn_add.clicked.connect(lambda x: hook.addListItem(self))
