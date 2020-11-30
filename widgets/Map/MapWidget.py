from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QFrame
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QColor, QBrush
from widgets.Map.ZoomableView import ZoomableView
from widgets.Map.Toolbox.ToolboxWidget import ToolboxWidget


class MapWidget(QWidget):

    def __init__(self, parent):
        super(MapWidget, self).__init__(parent)

        self.__parent = parent
        self.__items = []

        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)

        self.__layout.setContentsMargins(0, 0, 0, 0)

        self.__scene = QGraphicsScene(0, 0, 1000, 1000)
        self.__view = ZoomableView(self.__scene, self)
        self.__view.setDragMode(QGraphicsView.ScrollHandDrag)

        self.__view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.__view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.__toolbox = ToolboxWidget(self)
        self.__layout.addWidget(self.__view)
        self.__setupGrid()

    def addItem(self, item):
        self.__scene.addItem(item)


    def __setupGrid(self):
        brush = QBrush()
        brush.setColor(QColor('#223a50'))
        brush.setStyle(Qt.CrossPattern)
        self.__scene.setBackgroundBrush(brush)
        rect = QRectF(0.0, 0.0, 1000, 1000)  # Screen res or whatever.

        self.__scene.addRect(rect, QColor('#0b243a'), QColor('#0c273f'))
        self.__scene.addRect(rect, QColor('#0b243a'), brush)
