from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from services.StatisticsWidgetService import StatisticsWidgetService
from services.WindowService import WindowService
from widgets.Statistics.ContentWidget import ContentWidget
from widgets.Statistics.HeaderWidget import HeaderWidget


class StatisticsWidget(QWidget):

    def __init__(self, parent):
        super(StatisticsWidget, self).__init__(parent)
        StatisticsWidgetService.setWidget(self)
        self.setUi()

        WindowService.resizeSubject.subscribe(self.onWindowResize)


    def setUi(self):
        self.setVisible(False)

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        self.onWindowResize(None)
        self.setStyleSheet("""
        QWidget
        {
            background-color: #092339;
        }
        """)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.raise_()

        self.layout().addWidget(HeaderWidget(self))
        self.layout().addWidget(ContentWidget(self))
        self.layout().setStretch(0, 0)
        self.layout().setStretch(1, 1)


    def onWindowResize(self, event):
        geometry = WindowService.instance.frameGeometry()
        self.setGeometry(0, 0, geometry.width(), geometry.height())