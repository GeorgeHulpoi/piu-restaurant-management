from PyQt5.QtSvg import QSvgRenderer, QGraphicsSvgItem
from PyQt5.QtWidgets import QGraphicsItem

class TableItem(QGraphicsSvgItem):
    def __init__(self, fileName):
        super(TableItem, self).__init__(fileName)
        self.setScale(0.5)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)

    def itemChange(self, change, value):
        if (change == QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged):
            # value is PyQt5.QtCore.QPointF
            pass

        return value
