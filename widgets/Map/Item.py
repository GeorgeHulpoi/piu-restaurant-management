from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from models.Table import TableType
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtWidgets import QGraphicsItem, QMenu
from PyQt5.QtGui import QTransform, QCursor
from repositories.TableRepository import TableRepository
from services.TableOrderViewService import TableOrderViewService
import math
import time
from widgets.Map.MapMode import MapMode


class Item(QGraphicsSvgItem):

    def __init__(self, model, parent_widget):

        self.__model = model
        self.__updateChanges = False
        self.__pressed = False
        self.__parent_widget = parent_widget

        svgPath = 'widgets/Map/assets/4_table.svg'

        if self.__model.getType() == TableType.RECTANGLE_6:
            svgPath = 'widgets/Map/assets/6_table.svg'

        super(Item, self).__init__(svgPath)

        self.setScale(1)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.setX(self.__model.getX())
        self.setY(self.__model.getY())
        self.__updateChanges = True

        self.__parent_widget.modeObserver().subscribe(lambda m: self.onModeChanges(m))


    def itemChange(self, change, value):
        if self.__updateChanges:
            if change == QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged:
                self.updatePosition(value)
            elif change == QGraphicsItem.GraphicsItemChange.ItemTransformHasChanged:
                self.__model.setRotation(self.rotation())

        return value


    def onModeChanges(self, mode):
        if mode == MapMode.ROTATE_ITEMS:
            self.setFlag(QGraphicsItem.ItemIsSelectable)
            self.setFlags(self.flags() & ~QGraphicsItem.ItemIsMovable)
        elif mode == MapMode.MOVE_ITEMS:
            self.setFlags(QGraphicsItem.ItemIsSelectable)
            self.setFlag(QGraphicsItem.ItemIsMovable)
        else:
            self.setFlags(self.flags() & ~QGraphicsItem.ItemIsSelectable)
            self.setFlags(self.flags() & ~QGraphicsItem.ItemIsMovable)


    def model(self):
        return self.__model


    def updatePosition(self, value):
        if self.__parent_widget.mode() == MapMode.MOVE_ITEMS or \
                self.__parent_widget.mode() == MapMode.CREATE_ITEMS:
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


    def setCenter(self, point):
        internal_bounding = self.boundingRect()
        self.setX(point.x() - internal_bounding.width() / 2.0)
        self.setY(point.y() - internal_bounding.height() / 2.0)


    def mouseReleaseEvent(self, event):
        if self.__pressed:
            duration = time.time() - self.timestampPressedEvent

            if duration < 0.3 and self.x() == self.positionPressedEvent[0] and \
                    self.y() == self.positionPressedEvent[1]:
                self.__onClick()

            TableRepository.update(self.__model)
            self.__pressed = False
        super().mouseReleaseEvent(event)


    def __onClick(self):
        TableOrderViewService.showWidget(self.__model)


    def mouseMoveEvent(self, event):
        if self.__pressed == True and self.__parent_widget.mode() == MapMode.ROTATE_ITEMS:
            scene_pos = event.scenePos()
            dx = self.mouse_pos_pressed.x() - scene_pos.x()
            dy = self.mouse_pos_pressed.y() - scene_pos.y()
            if dy == 0:
                angle = 90
            else:
                angle = math.degrees(math.atan(dx / dy))
                if angle < 0:
                    angle += 360

            bounding = self.boundingRect()
            x = bounding.x() + bounding.width() / 2
            y = bounding.y() + bounding.height() / 2
            self.setTransform(QTransform().translate(x, y).rotate(-angle).translate(-x, -y))

        super().mouseMoveEvent(event)


    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.__pressed = True
            self.timestampPressedEvent = time.time()
            self.positionPressedEvent = (self.x(), self.y())
            self.mouse_pos_pressed = event.scenePos()
        super().mousePressEvent(event)


    def contextMenuEvent(self, event):
        menu = QMenu()
        action = menu.addAction("Open")
        action.triggered.connect(self.onOpenCallback)
        action = menu.addAction("Delete")
        action.triggered.connect(self.onDeleteCallback)
        menu.exec(event.screenPos())


    def onOpenCallback(self, checked=False):
        self.__onClick()


    def onDeleteCallback(self, checked=False):
        TableRepository.deleteById(int(self.getModel().getId()))
        self.__parent_widget.scene().removeItem(self)
