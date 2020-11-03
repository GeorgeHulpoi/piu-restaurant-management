from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from widgets.Titlebar.ButtonsWidget import ButtonsWidget

class TitlebarWidget(QWidget):

    def __init__(self, parent):
        super(TitlebarWidget, self).__init__()

        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("background-color: #101216;")

        titleLabel = QLabel('Restaurant Management')
        titleLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        titleLabel.setContentsMargins(16, 0, 16, 0)
        titleLabel.setStyleSheet("""
            color: rgba(255, 255, 255, 0.7);
            font-weight: 600;
        """)

        self.layout.addWidget(titleLabel)
        self.layout.addWidget(ButtonsWidget())
        self.layout.setSpacing(0)

        self.setLayout(self.layout)
        self.setFixedHeight(36)
        self.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.buttons() == Qt.LeftButton:
            self.__pressed = True
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.__pressed == True:
            currPos = self.parent.mapToGlobal(self.parent.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.parent.mapFromGlobal(currPos + diff)
            self.parent.move(newPos)

            self.__mouseMovePos = globalPos

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.__pressed = False
