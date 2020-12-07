from models.Table import TableType
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QTransform
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

        self.__parent_widget.get_mode_observer().subscribe(lambda m: self.on_mode_changes(m))

    def itemChange(self, change, value):
        if self.__updateChanges:
            if change == QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged:
                self.__updatePosition(value)

        return value

    def on_mode_changes(self, mode):
        if mode == MapMode.ROTATE_ITEMS:
            self.setFlags(self.flags() & ~QGraphicsItem.ItemIsMovable)
        elif mode == MapMode.MOVE_ITEMS:
            self.setFlag(QGraphicsItem.ItemIsMovable)

    def __updatePosition(self, value):
        if self.__parent_widget.get_mode() == MapMode.MOVE_ITEMS:
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
        print(event)
        duration = time.time() - self.timestampPressedEvent

        if duration < 0.3 and self.x() == self.positionPressedEvent[0] and self.y() == self.positionPressedEvent[1]:
            self.__onClick()

        TableRepository.update(self.__model)
        self.__pressed = False
        super().mouseReleaseEvent(event)

    def __onClick(self):
        TableOrderViewService.showWidget(self.__model)

    def mouseMoveEvent(self, event):
        if self.__pressed == True and self.__parent_widget.get_mode() == MapMode.ROTATE_ITEMS:
            scene_pos = event.scenePos()
            dx = self.mouse_pos_pressed.x() - scene_pos.x()
            dy = self.mouse_pos_pressed.y() - scene_pos.y()
            if dy == 0:
                angle = 90
            else:
                angle = math.degrees(math.atan(dx/dy))
                if angle < 0:
                    angle += 360

            bounding = self.boundingRect()
            x = bounding.x() + bounding.width()/2
            y = bounding.y() + bounding.height()/2
            self.setTransform(QTransform().translate(x, y).rotate(-angle).translate(-x, -y));


        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        self.__pressed = True
        self.timestampPressedEvent = time.time()
        self.positionPressedEvent = (self.x(), self.y())
        self.mouse_pos_pressed = event.scenePos()
        super().mousePressEvent(event)


