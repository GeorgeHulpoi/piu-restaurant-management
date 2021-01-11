from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget
from PyQt5.QtCore import Qt
from widgets.Map.MapMode import MapMode
from widgets.Map.Createbox.TableList import TableList

class CreateboxWidget(QWidget):

    def __init__(self, parent):
        super(CreateboxWidget, self).__init__(parent)

        self.__parent = parent
        self.__layout = QVBoxLayout()
        self.__layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        window_geometry = parent.get_parent().frameGeometry()
        self.setGeometry(window_geometry.width() - 200, 0, 200, window_geometry.height())
        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.__layout.setSpacing(0)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: red")

        self.setLayout(self.__layout)

        list = TableList(self)
        self.__layout.addWidget(list)

        parent.get_mode_observer().subscribe(lambda m: self.on_mode_changes(m))

    def on_mode_changes(self, mode):
        if mode == MapMode.CREATE_ITEMS:
            self.show()
        else:
            self.hide()

    def update_view(self):
        window_geometry = self.__parent.get_parent().frameGeometry()
        self.setGeometry(window_geometry.width() - 200, 0, 200, window_geometry.height())
