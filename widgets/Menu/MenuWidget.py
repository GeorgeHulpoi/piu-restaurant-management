import pathlib

from PyQt5 import QtCore
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

from services.StatisticsWidgetService import StatisticsWidgetService
from widgets.Menu.ItemWidget import ItemWidget


class MenuWidget(QWidget):

    def __init__(self, parent=None):
        super(MenuWidget, self).__init__(parent)

        self.__parent = parent

        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.layout().setContentsMargins(0, 12, 12, 0)
        self.layout().setSpacing(0)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("""
        QWidget
        {
            background-color: #092339;
        }
        """)
        window_geometry = parent.frameGeometry()
        self.setGeometry(0, 0, 200, window_geometry.height())
        self.setFixedWidth(200)

        statisticsBtn = ItemWidget("Statistics", self)
        statisticsBtn.clicked.connect(self.OnStatisticsButtonClicked)
        self.layout().addWidget(statisticsBtn)
        orderHistoryBtn = ItemWidget("Order History", self)
        self.layout().addWidget(orderHistoryBtn)

    def OnStatisticsButtonClicked(self):
        StatisticsWidgetService.showWidget()
