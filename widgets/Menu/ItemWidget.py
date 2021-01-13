from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QPushButton


class ItemWidget(QPushButton):

    def __init__(self, text, parent):
        super(ItemWidget, self).__init__(text, parent)

        parent_geometry = parent.frameGeometry()
        self.setFixedWidth(parent_geometry.width())
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet("""
        QPushButton
        {
            font-size: 14px;
            color: rgba(255, 255, 255, 0.6);
            background-color: #092339;
            border: 0;
            padding: 16px;
            text-align: center;
        }
        
        QPushButton:hover
        {
            color: #fff;
            background-color: #00cc7e;
        }
        """)
