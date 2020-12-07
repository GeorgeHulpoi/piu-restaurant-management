from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QFrame
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QColor, QBrush
from widgets.Map.ZoomableView import ZoomableView
from widgets.Map.Toolbox.ToolboxWidget import ToolboxWidget
from widgets.Map.MapMode import MapMode
from rx.subject import BehaviorSubject

class MapWidget(QWidget):

    def __init__(self, parent):
        super(MapWidget, self).__init__(parent)

        self.__parent = parent
        self.__items = []
        self.__mode = None
        self.__mode_subject = BehaviorSubject(MapMode.MOVE_ITEMS)

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

        self.__mode_subject.subscribe(lambda m: self.on_mode_changes(m))

    def addItem(self, item):
        self.__scene.addItem(item)

    def get_mode_observer(self):
        return self.__mode_subject

    def on_mode_changes(self, mode):
        self.__mode = mode

    def get_mode(self):
        return self.__mode

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_M:
            self.__mode_subject.on_next(MapMode.MOVE_ITEMS)
        if event.key() == Qt.Key_R:
            self.__mode_subject.on_next(MapMode.ROTATE_ITEMS)

    def __setupGrid(self):
        brush = QBrush()
        brush.setColor(QColor('#223a50'))
        brush.setStyle(Qt.CrossPattern)
        self.__scene.setBackgroundBrush(brush)
        rect = QRectF(0.0, 0.0, 1000, 1000)

        self.__scene.addRect(rect, QColor('#0b243a'), QColor('#0c273f'))
        self.__scene.addRect(rect, QColor('#0b243a'), brush)
