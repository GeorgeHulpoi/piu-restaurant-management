from PyQt5.QtWidgets import QLabel, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from widgets.Titlebar.TitlebarWidget import TitlebarWidget

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Restaurant Manegement")
        self.setMinimumSize(900, 600)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setStyleSheet("""
        QMainWindow
        {
            background-color: #202530;
        }
        """)

        layout = QVBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(TitlebarWidget(self))
        layout.addWidget(QLabel('este mare'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
