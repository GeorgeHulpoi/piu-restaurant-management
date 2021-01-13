from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout

from widgets.Statistics.BarChartWidget import BarChartWidget
from widgets.Statistics.PieChartWidget import PieChartWidget


class ContentWidget(QWidget):

    def __init__(self, parent):
        super(ContentWidget, self).__init__(parent)

        self.setUi()

    def setUi(self):
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(32, 0, 32, 32)
        self.layout().setSpacing(0)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.layout().addWidget(PieChartWidget('Most Bought Products', ['Item 1', 'Item 2', 'Item 3', 'Item 4'], [10, 20, 30, 40], self))
        self.layout().addWidget(BarChartWidget('Time Clients', ['12:00 AM', '01:00 PM', '02:00 PM', '03:00 PM'], [3, 10, 20, 1], self))
