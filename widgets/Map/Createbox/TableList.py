from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QAbstractItemView, QListWidgetItem
from models.Table import TableType


class TableList(QListWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setIconSize(QSize(64, 64))
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setDragEnabled(True)

        self.setStyleSheet("""
        *
        {
            show-decoration-selected: 0;
            outline: 0;
        }
        
        QListWidget
        { 
            background: #092339;
            padding: 16px 0;
        }
        
        QListWidget::item
        {
            color: #fff;
        }
        
        QListWidget::item:hover
        {
            background: rgba(255, 255, 255, 0.1);
        }
        
        QListWidget::item:selected
        {
            color: #fff;
            background: rgba(255, 255, 255, 0.1);
        }
        """)

        self.add_item(TableType.SQUARE_4,'Table 4 Chars',
                      'widgets/Map/assets/4_table_icon.png', QSize(64, 64))
        self.add_item(TableType.RECTANGLE_6, 'Table 6 Chars',
                      'widgets/Map/assets/6_table_icon.png', QSize(64, 90))

    def add_item(self, type, name, icon, size):
        item = QListWidgetItem(name, self)
        pixmap = QPixmap(icon)
        item.setIcon(QIcon(pixmap))
        item.setSizeHint(size)

        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)
        item.setData(Qt.UserRole, type)




