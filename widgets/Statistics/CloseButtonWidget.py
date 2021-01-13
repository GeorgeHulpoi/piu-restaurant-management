import pathlib

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QSizePolicy


class CloseButtonWidget(QPushButton):

    def __init__(self, parent):
        super(CloseButtonWidget, self).__init__(parent)

        self.setUi()

    def setUi(self):
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setLayout(QHBoxLayout())
        self.setCursor(QCursor(Qt.PointingHandCursor))
        iconPath = str(pathlib.Path(__file__).parent.absolute()) + "/assets/back.svg"
        icon = QSvgWidget(iconPath, self)
        icon.setFixedHeight(36)
        icon.setFixedWidth(36)

        self.setFixedWidth(44)
        self.setFixedHeight(44)
        self.layout().setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 8, 0, 8)
        self.layout().addWidget(icon)
        self.setStyleSheet("""
        QPushButton 
        {
            border: 0;
            padding: 0;
        }
        """)
