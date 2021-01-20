import os

from sys import platform

from PyQt5.QtWidgets import QWidget, QFrame, QHBoxLayout, QStackedWidget
from .components.shared.Colors import Colors
from .components.shared.Constants import Constants

from .components.views.Checkout import Checkout
from .components.views.Menu import Menu
from .components.views.MenuCategories import MenuCategories
from .components.views.MenuItems import MenuItems
from services.WindowService import WindowService


class TableOrderView(QWidget):

    def __init__(self, parent):

        # call super
        super(TableOrderView, self).__init__(parent)

        # get parent resolution
        resolution = parent.frameGeometry()

        # setup and config
        self.setMinimumSize(resolution.size())
        self.setStyleSheet(
            f"QFrame {{ background-color: {Colors.OXFORD_BLUE} }}")

        # setup layout
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(Constants.QLAYOUT_NO_MARGINS)
        self.layout().setSpacing(0)

        # define menus
        menu_categories = MenuCategories(self)
        menu = Menu(self, menu_categories)

        # define a stacked widget for categories
        stacked_menu = QStackedWidget(self)

        # define checkout widget
        checkout = Checkout(self)

        # define a page/widget for each category
        category_food = MenuItems(
            "foods", f"{os.path.dirname(__file__)}/components/resources/food.json", checkout)
        category_drinks = MenuItems(
            "drinks", f"{os.path.dirname(__file__)}/components/resources/drinks.json", checkout)
        category_dessert = MenuItems(
            "dessert", f"{os.path.dirname(__file__)}/components/resources/dessert.json", checkout)

        # add each page to the stacked widget
        stacked_menu.addWidget(category_food)
        stacked_menu.addWidget(category_drinks)
        stacked_menu.addWidget(category_dessert)

        # add a fourth page for startup reasons only
        stacked_menu.addWidget(QFrame())

        # set starting index for stacked widget
        stacked_menu.setCurrentIndex(3)

        # connect buttons with stacked widget
        menu_categories.connectHook(stacked_menu, 0, 1, 2)

        # add widgets
        self.layout().addWidget(menu)
        self.layout().addWidget(menu_categories)
        self.layout().addWidget(stacked_menu)
        self.layout().addWidget(checkout)

        # setup resize event handler
        WindowService.resizeSubject.subscribe(self.onWindowResize())

    def onWindowResize(self):
        geometry = WindowService.instance.frameGeometry()

        if platform == "win32":
            self.setGeometry(0, 0, geometry.width() - 2, geometry.height() - 39)
        else:
            self.setGeometry(0, 0, geometry.width(), geometry.height())
