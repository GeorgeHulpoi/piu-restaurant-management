from models.Table import TableType
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtWidgets import QGraphicsItem
from repositories.TableRepository import TableRepository
from services.TableOrderViewService import TableOrderViewService
import time


class Item(QGraphicsSvgItem):
    def __init__(self, model):

        self.__model = model
        self.__updateChanges = False

        svgPath = None
        if self.__model.getType() == TableType.ROUND_4:
            svgPath = 'widgets/Map/assets/round_table.svg'
        elif self.__model.getType() == TableType.SQUARE_4:
            svgPath = 'widgets/Map/assets/square_table.svg'
        elif self.__model.getType() == TableType.RECTANGLE_6:
            svgPath = 'widgets/Map/assets/rectangle_table.svg'

        super(Item, self).__init__('widgets/Map/assets/table.svg')

        self.setScale(1)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)

        self.setX(self.__model.getX())
        self.setY(self.__model.getY())
        self.__updateChanges = True

    def itemChange(self, change, value):
        if self.__updateChanges:
            if change == QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged:
                self.__updatePosition(value)

        return value

    def __updatePosition(self, value):
        bounding = self.scene().sceneRect()
        internal_bounding = self.boundingRect()

        if value.x() < 0:
            self.setX(0)
        if value.x() + internal_bounding.width() > bounding.width():
            self.setX(bounding.width() - internal_bounding.width())

        if value.y() < 0:
            self.setY(0)
        if value.y() + internal_bounding.height() > bounding.height():
            self.setY(bounding.height() - internal_bounding.height())

        self.__model.setX(self.x())
        self.__model.setY(self.y())

    def mouseReleaseEvent(self, event):
        duration = time.time() - self.timestampPressedEvent

        if duration < 0.3 and self.x() == self.positionPressedEvent[0] and self.y() == self.positionPressedEvent[1]:
            self.__onClick()

        TableRepository.update(self.__model)
        super().mouseReleaseEvent(event)

    def __onClick(self):
        TableOrderViewService.showWidget(self.__model)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.timestampPressedEvent = time.time()
        self.positionPressedEvent = (self.x(), self.y())


