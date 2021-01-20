import json
import os
import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QScrollArea, QWidget, QLabel

from ..shared.Colors import Colors
from ..shared.Constants import Constants
from .ListItem import ListItem
from .MenuButton import MenuButton


class Checkout(QFrame):

    def __init__(self):

        super(Checkout, self).__init__()

        self.setObjectName("self")
        self.setStyleSheet(f"""
            QFrame#self {{
                background-color: {Colors.DARK_CORNFLOWER_BLUE};
                min-width: 400px;
                max-width: 400px;
            }}

            QScrollArea {{
                border: none;
                background-color: {Colors.DARK_CORNFLOWER_BLUE};
                border-bottom: 1px solid {Colors.PLATINUM};
                padding-top: 17px;
            }}

            QLabel {{
                padding: 10px;
                background-color: {Colors.DARK_CORNFLOWER_BLUE};
            }}
        """)

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(Constants.QLAYOUT_NO_MARGINS)
        self.layout().setSpacing(0)

        self.total_price = 0

        self.label_total = QLabel(self)
        self.label_total.setText(f"{self.total_price} $")
        self.label_total.setAlignment(Qt.AlignCenter | Qt.AlignRight)

        self.btn_checkout = MenuButton("checkout")
        self.btn_checkout.clicked.connect(lambda x: self.checkoutAndPay())

        self.checkout_area = QFrame(self)
        self.checkout_area.setLayout(QVBoxLayout())
        self.checkout_area.layout().setContentsMargins(Constants.QLAYOUT_NO_MARGINS)
        self.checkout_area.layout().setSpacing(0)
        self.checkout_area.layout().addWidget(self.label_total)
        self.checkout_area.layout().addWidget(self.btn_checkout)

        self.inner = QWidget(self)
        self.inner.setStyleSheet('background-color: transparent;')
        self.inner.setLayout(QVBoxLayout())
        self.inner.layout().setContentsMargins(Constants.QLAYOUT_NO_MARGINS)
        self.inner.layout().addWidget(QFrame(self.inner))

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.inner)

        self.layout().addWidget(self.scroll_area)
        self.layout().addWidget(self.checkout_area)

    def addListItem(self, item):
        layout = self.inner.layout()
        layout.insertWidget(layout.count() - 1, ListItem(item, self))
        self.raiseTotalPrice(item)

    def raiseTotalPrice(self, item):
        self.total_price += item.getPrice()
        self.label_total.setText(f"{self.total_price} $")

    def lowerTotalPrice(self, item):
        if self.total_price != 0:
            self.total_price -= item.getPrice()
            self.label_total.setText(f"{self.total_price} $")

    def checkoutAndPay(self):
        try:
            if self.total_price != 0:
                # get layout
                layout = self.inner.layout()

                result = {
                    "total": 0,
                    "order-list": []
                }

                # remove all widgets from layout
                for i in reversed(range(layout.count())):
                    item = layout.itemAt(i).widget()

                    # layout.count() is index of fill_space which is of type QFrame
                    if i != layout.count() - 1:

                        # read data and store it as a json
                        order_item = {"name": "", "price": 0}
                        order_item["name"] = item.getTitle()
                        order_item["price"] = item.getPrice()
                        order_item["qty"] = item.getQty()
                        result["order-list"].append(order_item)

                    item.deleteLater()

                result["total"] = self.total_price

                # read date and time and use as output name
                #now = datetime.now(tz=None)
                #dt_string = now.strftime("%d.%m.%Y_%H:%M:%S")
                now = int(time.time())

                # export json
                tableOrderViewPath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
                with open(os.path.join(tableOrderViewPath, "orders", f"{now}.json"), "w") as json_output:
                    json.dump(result, json_output)

                # add fill space
                layout.addWidget(QFrame(self.inner))

                # reset total price
                self.total_price = 0
                self.label_total.setText(f"{self.total_price} $")
        except Exception as e:
            print(e)
