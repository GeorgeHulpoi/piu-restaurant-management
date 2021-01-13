import json

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QScrollArea

from ..shared.Colors import Colors
from ..shared.Constants import Constants
from .MenuItem import MenuItem


class MenuItems(QFrame):

    def __init__(self, title, file_path, hook):

        # call super
        super(MenuItems, self).__init__()

        # get arguments
        self.title = title
        self.file_path = file_path
        self.hook = hook

        # define style-sheet
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {Colors.ORANGE_WEB};
                padding: 10px;
            }}

            QLabel#title {{
                background-color: {Colors.ORANGE_WEB};
                color: {Colors.BLACK};
                font-size: 24px;
                font-weight: bold;
                letter-spacing: 3px;
                min-height: 20px;
                max-height: 20px;
                padding: 10px;
                text-transform: uppercase;
            }}

            QScrollArea {{
                padding: 7px;
                border: none;
            }}
        """)

        # setup layout
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(Constants.QLAYOUT_NO_MARGINS)
        self.layout().setSpacing(0)

        # define a title label
        title_label = QLabel()
        title_label.setText(self.title)
        title_label.setObjectName("title")

        # define a scroll area
        scroll_area = QScrollArea()

        # setup a central widget for scroll area
        central_widget = QFrame()
        central_widget.setLayout(QVBoxLayout())
        central_widget.layout().setContentsMargins(Constants.QLAYOUT_NO_MARGINS)
        central_widget.layout().setSpacing(10)

        # setup and config scroll area
        scroll_area.setWidget(central_widget)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)

        # read from file path and add items to scroll area
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                for item in data:
                    menu_item = MenuItem(
                        item['name'], item['price'], item['description'])
                    menu_item.connectHook(self.hook)
                    central_widget.layout().insertWidget(0, menu_item)

        except Exception:
            print("File was corrupt or could not been opened.")

        # add widgets
        self.layout().addWidget(title_label)
        self.layout().addWidget(scroll_area)
