from PyQt5.QtWidgets import QWidget, QHBoxLayout
from widgets.Map.Toolbox.Button import Button
from widgets.Map.MapMode import MapMode

class ToolboxWidget(QWidget):

    def __init__(self, parent):
        super(ToolboxWidget, self).__init__(parent)

        self.__parent = parent
        self.__layout = QHBoxLayout()
        self.setGeometry(40, 0, 150, 50)

        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.__layout.setSpacing(0)
        self.setLayout(self.__layout)

        self.__moveBtn = Button("arrows-alt.svg",
                                MapMode.MOVE_ITEMS,
                                self.__parent.get_mode_observer())
        self.__rotateBtn = Button("sync-alt.svg",
                                  MapMode.ROTATE_ITEMS,
                                  self.__parent.get_mode_observer())

        self.__createBtn = Button("table.svg",
                                  MapMode.CREATE_ITEMS,
                                  self.__parent.get_mode_observer())

        self.__moveBtn.clicked.connect(self.move_button_callback)
        self.__rotateBtn.clicked.connect(self.rotate_button_callback)
        self.__createBtn.clicked.connect(self.create_button_callback)

        self.__layout.addWidget(self.__moveBtn)
        self.__layout.addWidget(self.__rotateBtn)
        self.__layout.addWidget(self.__createBtn)

    def move_button_callback(self, event):
        self.__parent.get_mode_observer().on_next(MapMode.MOVE_ITEMS)

    def rotate_button_callback(self, event):
        self.__parent.get_mode_observer().on_next(MapMode.ROTATE_ITEMS)
        
    def create_button_callback(self, event):
        self.__parent.get_mode_observer().on_next(MapMode.CREATE_ITEMS)
