from PyQt5.QtWidgets import QWidget, QHBoxLayout
from widgets.Map.Toolbox.Button import Button
from widgets.Map.MapMode import MapMode


class ToolboxWidget(QWidget):

    def __init__(self, parent):
        super(ToolboxWidget, self).__init__(parent)

        self.__parent = parent
        self.setGeometry(40, 0, 150, 50)

        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        moveBtn = Button("arrows-alt.svg",
                                MapMode.MOVE_ITEMS,
                                parent.modeObserver())
        rotateBtn = Button("sync-alt.svg",
                                  MapMode.ROTATE_ITEMS,
                                  parent.modeObserver())

        createBtn = Button("table.svg",
                                  MapMode.CREATE_ITEMS,
                                  parent.modeObserver())

        moveBtn.clicked.connect(self.moveButtonCallback)
        rotateBtn.clicked.connect(self.rotateButtonCallback)
        createBtn.clicked.connect(self.createButtonCallback)

        self.layout().addWidget(moveBtn)
        self.layout().addWidget(rotateBtn)
        self.layout().addWidget(createBtn)

    def moveButtonCallback(self, event):
        self.__parent.modeObserver().on_next(MapMode.MOVE_ITEMS)

    def rotateButtonCallback(self, event):
        self.__parent.modeObserver().on_next(MapMode.ROTATE_ITEMS)
        
    def createButtonCallback(self, event):
        self.__parent.modeObserver().on_next(MapMode.CREATE_ITEMS)
