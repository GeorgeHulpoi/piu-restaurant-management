from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsView, QListWidgetItem
from models.Table import TableType
from repositories.TableRepository import TableRepository
from widgets.Map.Createbox.TableList import TableList
from widgets.Map.Item import Item


class GraphicsView(QGraphicsView):

    def __init__ (self, scene, parent=None):
        super(GraphicsView, self).__init__(scene, parent)

        self.__parent = parent
        self.__scene = scene
        self.setStyleSheet("background-color: #061727")


    def wheelEvent(self, event):
        # Zoom Factor
        zoomInFactor = 1.25
        zoomOutFactor = 1 / zoomInFactor

        # Set Anchors
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)

        # Save the scene pos
        oldPos = self.mapToScene(event.pos())

        # Zoom
        if event.angleDelta().y() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor
        self.scale(zoomFactor, zoomFactor)

        # Get the new position
        newPos = self.mapToScene(event.pos())

        # Move scene to old position
        delta = newPos - oldPos
        self.translate(delta.x(), delta.y())


    def dragMoveEvent(self, event):
        pass


    def dragEnterEvent(self, event):
        if not isinstance(event.source(), TableList):
            return

        item = event.source().currentItem()
        if not isinstance(item, QListWidgetItem):
            return
        self.drop_item = item

        data = item.data(Qt.UserRole)

        if data.name in TableType.__members__:
            event.acceptProposedAction()


    def dropEvent(self, event):
        pos = self.mapToScene(event.pos())
        type = self.drop_item.data(Qt.UserRole)
        model = TableRepository.create(pos.x(), pos.y(), 0, type)
        item = Item(model, self.__parent)
        self.__scene.addItem(item)
        item.setCenter(pos)
        TableRepository.update(item.model())
