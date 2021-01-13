# PyQt5
from PyQt5 import QtCore, QtWidgets

# REPOSITORIES
from repositories.TableRepository import TableRepository

# SERVICES
from services.TableOrderViewService import TableOrderViewService

# WIDGETS
from services.WindowService import WindowService
from widgets.Map.MapWidget import MapWidget
from widgets.Map.Item import Item
from widgets.Statistics.StatisticsWidget import StatisticsWidget
from widgets.TableOrderView.TableOrderView import TableOrderView
from widgets.Menu.MenuWidget import MenuWidget


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):

        # CALL SUPER
        super(MainWindow, self).__init__()
        WindowService.setInstance(self)

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
        centralwidget.setLayout(QtWidgets.QHBoxLayout())
        centralwidget.layout().setContentsMargins(QtCore.QMargins(0, 0, 0, 0))
        centralwidget.layout().setSpacing(0)

        # SETUP TABLE MAP WIDGET
        self.__mapWidget = MapWidget(self)

        models = TableRepository.find_all()

        for model in models:
            item = Item(model, self.__mapWidget)
            self.__mapWidget.addItem(item)

        # ADD TABLE MAP WIDGET TO BASE WIDGET
        centralwidget.layout().addWidget(MenuWidget(self))
        centralwidget.layout().addWidget(self.__mapWidget)
        StatisticsWidget(centralwidget)

        # SETUP MAIN WIDGET
        self.setCentralWidget(centralwidget)

        # SETUP TABLE ORDER SERVICE
        TableOrderViewService.setWidget(TableOrderView(self))
        TableOrderViewService().hideWidget()

        # CENTER WINDOW BEFORE DISPLAY
        rectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(centerPoint)
        self.move(rectangle.topLeft())

        # DISPLAY MAIN WINDOW
        self.show()

    def resizeEvent(self, event):
        WindowService.resizeSubject.on_next(event)
