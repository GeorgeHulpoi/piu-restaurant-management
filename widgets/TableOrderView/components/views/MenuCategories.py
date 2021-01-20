from PyQt5.QtWidgets import QFrame, QVBoxLayout
from ..shared.Colors import Colors
from ..shared.Constants import Constants
from .MenuButton import MenuButton


class MenuCategories(QFrame):

    is_open = True

    def __init__(self, parent=None):

        # call super
        super(MenuCategories, self).__init__(parent)

        # setup and config
        self.setFixedWidth(200)
        self.setStyleSheet(
            f"QFrame {{background-color: {Colors.OXFORD_BLUE}; padding: 10px;}}")

        # setup layout
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(Constants.QLAYOUT_NO_MARGINS)
        self.layout().setSpacing(10)

        # define fill component
        fill_space = QFrame()

        # define buttons
        self.btn_food = MenuButton("food")
        self.btn_drinks = MenuButton("drinks")
        self.btn_dessert = MenuButton("dessert")

        # add widgets
        self.layout().addWidget(self.btn_food)
        self.layout().addWidget(self.btn_drinks)
        self.layout().addWidget(self.btn_dessert)
        self.layout().addWidget(fill_space)

        # hide layout on startup
        self.showHide()

    def showHide(self):
        self.is_open = not self.is_open

        if self.is_open:
            self.show()
        else:
            self.hide()

    def connectHook(self, hook, f_idx, dr_idx, ds_idx):

        # define button actions based on hook: QStackedWidget and index
        self.btn_food.clicked.connect(lambda x: hook.setCurrentIndex(f_idx))
        self.btn_drinks.clicked.connect(lambda x: hook.setCurrentIndex(dr_idx))
        self.btn_dessert.clicked.connect(
            lambda x: hook.setCurrentIndex(ds_idx))
