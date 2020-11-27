from models.Table import TableType
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtWidgets import QGraphicsItem

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

        if value.x() >= 0:
            self.__model.setX(value.x())
        else:
            self.setX(0)

        if value.x() + internal_bounding.width() <= bounding.width():
            self.__model.setX(value.x())
        else:
            self.setX(bounding.width() - internal_bounding.width())

        if value.y() >= 0:
            self.__model.setY(value.y())
        else:
            self.setY(0)

        if value.y() + internal_bounding.height() <= bounding.height():
            self.__model.setY(value.y())
        else:
            self.setY(bounding.height() - internal_bounding.height())


