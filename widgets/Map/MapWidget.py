from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import QSize, Qt, QRectF
from PyQt5.QtGui import QColor, QBrush
from widgets.Map.Item import Item
from models.Table import Table
from widgets.Map.ZoomableView import ZoomableView
import random


class MapWidget(QWidget):

    def __init__(self, parent, items=None):
        super(MapWidget, self).__init__(parent)

        if items is None:
            items = []

        self.__parent = parent
        self.__items = items

        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)

        self.__layout.setContentsMargins(0, 0, 0, 0)

        self.__scene = QGraphicsScene(0, 0, 1000, 1000)
        self.__view = ZoomableView(self.__scene, self)
        self.__view.setDragMode(QGraphicsView.ScrollHandDrag)

        self.__view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.__view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.__layout.addWidget(self.__view)
        self.__setupGrid()

        for i in range(0, 5):
            model = Table(i, random.randint(0, 1000), random.randint(0, 1000), 0.0, random.randint(0, 2))
            item = Item(model, self.__scene)
            self.__scene.addItem(item)

    def __setupGrid(self):
        brush = QBrush()
        brush.setColor(QColor('#223a50'))
        brush.setStyle(Qt.CrossPattern)
        self.__scene.setBackgroundBrush(brush)
        rect = QRectF(0.0, 0.0, 1000, 1000)  # Screen res or whatever.

        self.__scene.addRect(rect, QColor('#0b243a'), QColor('#0c273f'))
        self.__scene.addRect(rect, QColor('#0b243a'), brush)
