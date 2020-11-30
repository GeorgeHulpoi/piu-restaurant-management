from PyQt5 import QtCore, QtWidgets
from .MenuPage import MenuPage


class MenuView(QtWidgets.QStackedWidget):

    __instance = None

    def __init__(self):
        if MenuView.__instance == None:
            # INIT
            super(MenuView, self).__init__()

            # SETUP STYLE SHEET
            self.setStyleSheet(
                """
                QStackedWidget
                {
                    background-color: #164850;
                }
                """
            )

            # SETUP MENU PAGES
            foodPage = MenuPage('widgets/TableOrderView/components/resources/food.json')
            drinksPage = MenuPage('widgets/TableOrderView/components/resources/drinks.json')
            dessertsPage = MenuPage('widgets/TableOrderView/components/resources/dessert.json')

            # ADD PAGES
            self.addWidget(foodPage)
            self.addWidget(drinksPage)
            self.addWidget(dessertsPage)

            self.setCurrentIndex(0)

            MenuView.__instance = self
        else:
            raise Exception('ceva')
    
    @staticmethod
    def getInstance():
        if MenuView.__instance == None:
            MenuView()
        
        return MenuView.__instance