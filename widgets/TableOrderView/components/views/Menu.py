from PyQt5.QtWidgets import QFrame, QVBoxLayout
from ..shared.Colors import Colors
from ..shared.Constants import Constants
from .MenuButton import MenuButton


class Menu(QFrame):

    def __init__(self, parent, target):

        # call super
        super(Menu, self).__init__(parent)

        # get arguments
        self.target = target
        self.parent = parent

        # setup and config
        self.setFixedWidth(200)
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {Colors.OXFORD_BLUE};
                padding: 10px;
            }}
            """)

        # setup layout
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(Constants.QLAYOUT_NO_MARGINS)
        self.layout().setSpacing(0)

        # define fill component
        fill_space = QFrame()

        # define buttons
        btn_main_menu = MenuButton("menu")
        btn_go_back = MenuButton("go back")

        # define button actions
        btn_main_menu.clicked.connect(lambda x: self.target.showHide())
        btn_go_back.clicked.connect(lambda x: self.parent.close())

        # add widgets
        self.layout().addWidget(btn_main_menu)
        self.layout().addWidget(fill_space)
        self.layout().addWidget(btn_go_back)
