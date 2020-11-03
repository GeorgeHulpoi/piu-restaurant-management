from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from widgets.Titlebar.ButtonWidget import ButtonWidget

class ButtonsWidget(QWidget):

    def __init__(self, parent=None):
        super(ButtonsWidget, self).__init__(parent)

        self.__mainWindow = parent
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

        minimizeBtn = ButtonWidget("widgets/Titlebar/assets/minimize.svg")
        minimizeBtn.setStyleSheet(btnNormalQss)
        minimizeBtn.clicked.connect(self.MinimizeCallback)

        maximizeBtn = ButtonWidget("widgets/Titlebar/assets/maximize.svg")
        maximizeBtn.setStyleSheet(btnNormalQss)
        maximizeBtn.clicked.connect(self.MaximizeCallback)

        closeBtn = ButtonWidget("widgets/Titlebar/assets/close.svg")
        closeBtn.setStyleSheet(btnCloseQss)
        closeBtn.clicked.connect(self.CloseCallback)

        self.layout.addWidget(minimizeBtn)
        self.layout.addWidget(maximizeBtn)
        self.layout.addWidget(closeBtn)

        self.setLayout(self.layout)
        self.setFixedHeight(36)
        self.setFixedWidth(36 * 3)

    def MinimizeCallback(self):
        if self.__mainWindow is not None:
            self.__mainWindow.showMinimized()

    def MaximizeCallback(self):
        if self.__mainWindow is not None:
            if self.__mainWindow.isMaximized():
                self.__mainWindow.showNormal()
            else:
                self.__mainWindow.showMaximized()

    def CloseCallback(self):
        if self.__mainWindow is not None:
            self.__mainWindow.close()
