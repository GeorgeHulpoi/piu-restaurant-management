from PyQt5.QtWidgets import QLabel, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from widgets.Titlebar.TitlebarWidget import TitlebarWidget
from widgets.Map.MapWidget import MapWidget


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

        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.__mapWidget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def resizeEvent(self, event):
        #self.__titlebarWidget.OnResizeCallback(event)
        pass
