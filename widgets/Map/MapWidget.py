from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QColor, QBrush
from widgets.Map.GraphicsView import GraphicsView
from widgets.Map.Toolbox.ToolboxWidget import ToolboxWidget
from widgets.Map.Createbox.CreateboxWidget import CreateboxWidget
from widgets.Map.MapMode import MapMode
from rx.subject import BehaviorSubject

class MapWidget(QWidget):

    def __init__(self, parent):
        super(MapWidget, self).__init__(parent)

        self.__parent = parent
        self.__items = []
        self.__mode = None
        self.__mode_subject = BehaviorSubject(MapMode.MOVE_ITEMS)

        self.setLayout(QVBoxLayout())

        self.layout().setContentsMargins(0, 0, 0, 0)

        self.__scene = QGraphicsScene(0, 0, 1000, 1000)
        self.__view = GraphicsView(self.__scene, self)
        self.__view.setDragMode(QGraphicsView.ScrollHandDrag)
        self.__view.acceptDrops()

        self.__view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.__view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.__toolbox = ToolboxWidget(self)
        self.__createbox = CreateboxWidget(self)
        self.layout().addWidget(self.__view)
        self.__setupGrid()

        self.__mode_subject.subscribe(lambda m: self.onModeChanges(m))

        self.setStyleSheet("""
        QWidget
        {
            border: 0;
            outline: 0;
        }
        """)


    def addItem(self, item):
        self.__scene.addItem(item)


    def modeObserver(self):
        return self.__mode_subject


    def onModeChanges(self, mode):
        self.__mode = mode


    def mode(self):
        return self.__mode


    def view(self):
        return self.__view


    def scene(self):
        return self.__scene


    def parent(self):
        return self.__parent


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
