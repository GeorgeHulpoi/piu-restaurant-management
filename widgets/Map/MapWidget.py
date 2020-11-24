from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import QSize, Qt
from widgets.Map.items.TableItem import TableItem
from widgets.Map.CustomQGraphicsView import CustomQGraphicsView

class MapWidget(QWidget):

    def __init__(self, parent):
        super(MapWidget, self).__init__(parent)

        self.__parent = parent
        # self.setStyleSheet("background: red")

        self.setMinimumSize(parent.width(), parent.height() - 36)

        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)

        self.__layout.setContentsMargins(0, 0, 0, 0)

        self.__scene = QGraphicsScene(0, 0, 1000, 1000)
        self.__view = CustomQGraphicsView(self.__scene, self)
        self.__view.setDragMode(QGraphicsView.ScrollHandDrag)

        self.__view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.__view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.__layout.addWidget(self.__view)

        item = TableItem("widgets/Map/assets/table.svg")
        item.setX(500)
        item.setY(500)

        self.__scene.addItem(item)

        self.OnResizeCallback()


    def sizeHint(self):
        return QSize(self.__parent.width(), self.__parent.height() - 36)

    def OnResizeCallback(self):
        self.setGeometry(0, 0, self.__parent.width(), self.__parent.height())


