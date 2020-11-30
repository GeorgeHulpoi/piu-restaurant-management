from PyQt5.QtWidgets import QMainWindow, QFrame
from PyQt5.QtCore import Qt
from widgets.Map.Item import Item
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from widgets.Titlebar.TitlebarWidget import TitlebarWidget
from widgets.Map.MapWidget import MapWidget
from repositories.TableRepository import TableRepository
from services.TableOrderViewService import TableOrderViewService


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Restaurant Manegement")
        self.setMinimumSize(900, 600)
        self.setWindowFlags(Qt.Window)
        self.setStyleSheet("""
        QMainWindow
        {
            background-color: #202530;
        }
        """)

        layout = QVBoxLayout()

        self.__titlebarWidget = TitlebarWidget(self)
        self.__mapWidget = MapWidget(self)

        models = TableRepository.find_all()

        for model in models:
            item = Item(model)
            self.__mapWidget.addItem(item)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.__mapWidget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.frame = QFrame(self)
        self.frame.setGeometry(0, 0, self.width(), self.height())
        self.frame.setContentsMargins(0, 0, 0, 0)
        self.frame.setStyleSheet("background: red;")
        self.frame.setVisible(False)
        TableOrderViewService.setWidget(self.frame)

    def resizeEvent(self, event):
        #self.__titlebarWidget.OnResizeCallback(event)
        self.frame.setGeometry(0, 0, self.width(), self.height())
