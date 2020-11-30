from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtSvg import QSvgWidget


class ButtonWidget(QPushButton):

    def __init__(self, svgPath, parent=None):
        super(ButtonWidget, self).__init__(parent)

        icon = QSvgWidget(svgPath, self)
        icon.setFixedWidth(12)
        icon.setFixedHeight(12)
        icon.setStyleSheet("background-color: transparent;")

        self.layout = QHBoxLayout()
        self.layout.addWidget(icon)
        self.setLayout(self.layout)

        self.setFixedHeight(36)
        self.setFixedWidth(36)
