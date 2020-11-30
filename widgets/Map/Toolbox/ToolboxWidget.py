from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from widgets.Map.Toolbox.Button import Button
from PyQt5.QtCore import QPoint

class ToolboxWidget(QWidget):

    def __init__(self, parent):
        super(ToolboxWidget, self).__init__(parent)

        self.__layout = QHBoxLayout()
        self.setGeometry(40, 0, 100, 50)

        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.__layout)

        self.__moveBtn = Button("arrows-alt.svg")
        self.__rotateBtn = Button("sync-alt.svg")

        self.__layout.addWidget(self.__moveBtn)
        self.__layout.addWidget(self.__rotateBtn)
