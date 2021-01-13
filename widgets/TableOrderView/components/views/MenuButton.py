from PyQt5.QtWidgets import QPushButton
from ..shared.Colors import Colors


class MenuButton(QPushButton):

    def __init__(self, title):

        # call super
        super(MenuButton, self).__init__()

        # get arguments
        self.title = title

        # setup and config
        self.setText(self.title)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {Colors.BLACK}; 
                border: 0; 
                color: {Colors.WHITE};
                font-weight: bold;
                letter-spacing: 3px;
                padding: 10px;
                text-transform: uppercase;
            }}

            QPushButton:hover:!pressed {{
                background-color: {Colors.ORANGE_WEB};
                color: {Colors.BLACK};
                letter-spacing: 1px;
            }}

            QPushButton:hover:pressed {{
                background-color: {Colors.BRIGHT_YELLOW_CRAYOLA};
            }}
        """)
