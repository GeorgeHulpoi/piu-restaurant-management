# PyQt5
from PyQt5 import QtCore, QtWidgets

# REPOSITORIES
from repositories.TableRepository import TableRepository

# SERVICES
from services.TableOrderViewService import TableOrderViewService

# WIDGETS
from widgets.Map.MapWidget import MapWidget
from widgets.Map.Item import Item
from widgets.TableOrderView.TableOrderView import TableOrderView


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):

        # CALL SUPER
        super(MainWindow, self).__init__()

        # CONFIGURE MAIN WINDOW
        self.width = kwargs.get('width', 1280)
        self.height = kwargs.get('height', 720)
        self.title = kwargs.get('title', 'App')
        self.setMinimumSize(self.width, self.height)
        self.setWindowTitle(self.title)

        # SETUP STYLE SHEET
        self.setStyleSheet('background-color: #202530;')

        # CONFIG MAIN WIDGET
        centralwidget = QtWidgets.QWidget()
        centralwidget.setLayout(QtWidgets.QVBoxLayout())
        centralwidget.layout().setContentsMargins(QtCore.QMargins(0,0,0,0))
        centralwidget.layout().setSpacing(0)
        
        # SETUP TABLE MAP WIDGET
        self.__mapWidget = MapWidget(self)

        models = TableRepository.find_all()

        for model in models:
            item = Item(model, self.__mapWidget)
            self.__mapWidget.addItem(item)
        
        # ADD TABLE MAP WIDGET TO BASE WIDGET
        centralwidget.layout().addWidget(self.__mapWidget)

        # SETUP MAIN WIDGET
        self.setCentralWidget(centralwidget)

        # SETUP TABLE ORDER SERVICE
        TableOrderViewService.setWidget(TableOrderView(self, self.width, self.height))

        # CENTER WINDOW BEFORE DISPLAY
        rectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(centerPoint)
        self.move(rectangle.topLeft())

        # DISPLAY MAIN WINDOW
        self.show()
