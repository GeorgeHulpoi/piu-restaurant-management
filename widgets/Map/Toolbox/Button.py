from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QHBoxLayout
import pathlib


class Button(QPushButton):

    def __init__(self, icon, mode, observer):
        super(Button, self).__init__()

        self.mode = mode

        iconPath = str(pathlib.Path(__file__).parent.absolute()) + "/assets/" + icon
        icon = QSvgWidget(iconPath, self)
        icon.setFixedWidth(22)
        icon.setFixedHeight(22)
        icon.setStyleSheet("background: transparent")

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(icon)

        self.setFixedHeight(50)
        self.setFixedWidth(50)
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        observer.subscribe(self.onModeChanges)

    def onModeChanges(self, mode):
        if mode == self.mode:
            self.setActive()
        else:
            self.setInactive()

    def setActive(self):
        self.setStyleSheet("""
        Button 
        {
            border: 0; 
            background-color: rgba(255, 255, 255, 0.3);
        }
        """)

    def setInactive(self):
        self.setStyleSheet("""
        Button 
        {
          border: 0; 
          background-color: rgba(255, 255, 255, 0.15);
        }
        
        Button:hover
        {
          background-color: rgba(255, 255, 255, 0.3);
        }
        """)
