from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

from services.WindowService import WindowService
from widgets.Map.MapMode import MapMode
from widgets.Map.Createbox.TableList import TableList

class CreateboxWidget(QWidget):

    def __init__(self, parent=None):
        super(CreateboxWidget, self).__init__(parent)

        self.parent = parent
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.raise_()
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.layout().addWidget(TableList(self))

        parent.modeObserver().subscribe(self.onModeChanges)
        WindowService.resizeSubject.subscribe(self.onWindowResize)

    def onModeChanges(self, mode):
        if mode == MapMode.CREATE_ITEMS:
            self.show()
            window_geometry = self.parent.parent().frameGeometry()
            self.move(window_geometry.width() - 400, 0)
        else:
            self.hide()

    def onWindowResize(self, event):
        geometry = WindowService.instance.frameGeometry()
        self.setGeometry(geometry.width() - 400, 0, 200, geometry.height())
