from PyQt5.QtWidgets import QWidget, QHBoxLayout
from widgets.Map.Toolbox.Button import Button
from widgets.Map.MapMode import MapMode

class ToolboxWidget(QWidget):

    def __init__(self, parent):
        super(ToolboxWidget, self).__init__(parent)

        self.__parent = parent
        self.__layout = QHBoxLayout()
        self.setGeometry(40, 0, 100, 50)

        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.__layout)

        self.__moveBtn = Button("arrows-alt.svg",
                                MapMode.MOVE_ITEMS,
                                self.__parent.get_mode_observer())
        self.__rotateBtn = Button("sync-alt.svg",
                                  MapMode.ROTATE_ITEMS,
                                  self.__parent.get_mode_observer())

        self.__moveBtn.clicked.connect(self.MoveButtonCallback)
        self.__rotateBtn.clicked.connect(self.RotateButtonCallback)

        self.__layout.addWidget(self.__moveBtn)
        self.__layout.addWidget(self.__rotateBtn)

    def MoveButtonCallback(self, event):
        self.__parent.get_mode_observer().on_next(MapMode.MOVE_ITEMS)

    def RotateButtonCallback(self, event):
        self.__parent.get_mode_observer().on_next(MapMode.ROTATE_ITEMS)
