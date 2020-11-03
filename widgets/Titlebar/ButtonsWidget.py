from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
import PyQt5.QtSvg
from PyQt5.QtCore import Qt

class ButtonsWidget(QWidget):

    def __init__(self, parent=None):
        super(ButtonsWidget, self).__init__(parent)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        btnBaseQss = """
        QPushButton
        {
            background-color: #101216;
            color: rgba(255, 255, 255, 0.6);
            font-size: 18px;
            border: 0;
        }
        """

        btnNormalQss = btnBaseQss + """
        QPushButton:hover 
        {
            background-color: #1d2028;
        }
        """

        btnCloseQss = btnBaseQss + """
        QPushButton:hover 
        {
            background: rgb(232, 17, 35);
        }
        """

        minimizeBtn = QPushButton("_")
        minimizeBtn.setStyleSheet(btnNormalQss)
        minimizeBtn.setFixedWidth(36)
        minimizeBtn.setFixedHeight(36)

        maximizeBtn = QPushButton("□")
        maximizeBtn.setStyleSheet(btnNormalQss)
        maximizeBtn.setFixedWidth(36)
        maximizeBtn.setFixedHeight(36)

        closeBtn = QPushButton("X")
        closeBtn.setStyleSheet(btnCloseQss)
        closeBtn.setFixedWidth(36)
        closeBtn.setFixedHeight(36)

        self.layout.addWidget(minimizeBtn)
        self.layout.addWidget(maximizeBtn)
        self.layout.addWidget(closeBtn)

        self.setLayout(self.layout)
        self.setFixedHeight(36)
        self.setFixedWidth(36 * 3)
