from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel

from services.StatisticsWidgetService import StatisticsWidgetService
from widgets.Statistics.CloseButtonWidget import CloseButtonWidget


class HeaderWidget(QWidget):

    def __init__(self, parent):
        super(HeaderWidget, self).__init__(parent)

        self.setUi()

    def setUi(self):
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(32, 32, 32, 32)
        self.layout().setSpacing(0)

        self.setStyleSheet("""
        QLabel 
        {
            font-size: 32px;
            color: #fff;
        }
        """)

        self.layout().setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        closeBtn = CloseButtonWidget(self)
        closeBtn.clicked.connect(self.onCloseButtonClicked)
        self.layout().addWidget(closeBtn)
        self.layout().addWidget(QLabel("Statistics"))

    def onCloseButtonClicked(self):
        StatisticsWidgetService.hideWidget()
