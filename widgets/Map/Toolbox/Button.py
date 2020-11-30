from PyQt5.QtWidgets import QPushButton
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
import pathlib

class Button(QPushButton):

    def __init__(self, icon):
        super(Button, self).__init__()

        iconPath = str(pathlib.Path(__file__).parent.absolute()) + "\\assets\\" + icon
        icon = QSvgWidget(iconPath, self)
        icon.setFixedWidth(22)
        icon.setFixedHeight(22)
        icon.setStyleSheet("background: transparent")

        self.__layout = QHBoxLayout()
        self.__layout.addWidget(icon)
        self.setLayout(self.__layout)

        self.setFixedHeight(50)
        self.setFixedWidth(50)
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
