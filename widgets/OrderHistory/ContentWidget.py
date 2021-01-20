import os
import json

from sys import platform
from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListWidget, QPlainTextEdit


class ContentWidget(QWidget):

    def __init__(self, parent):
        super(ContentWidget, self).__init__(parent)

        self.read_area = QPlainTextEdit(self)
        self.widgets_path = os.path.dirname(os.path.dirname(__file__))
        self.dirname = os.path.join(self.widgets_path, "TableOrderView", "orders")
        self.list_bills_widget = QListWidget()
        self.list_bills_data = []
        self.setUi()

    def setUi(self):
        if platform == "win32":
            self.setStyleSheet("""
                QListWidget, QPlainTextEdit {
                    font-family: 'Courier New';
                    font-size: 15px;
                    color: white;
                    border: 1px solid white;
                    border-radius: 10px;
                    padding: 15px;
                }
            """)
        else:
            self.setStyleSheet("""
                QListWidget, QPlainTextEdit {
                    font-family: 'monospace';
                    color: white;
                    border: 1px solid white;
                    border-radius: 10px;
                    padding: 15px;
                }
            """)

        self.setLayout(QHBoxLayout())
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.layout().setContentsMargins(32, 0, 32, 32)

        self.readBills()
        self.list_bills_widget.itemClicked.connect(
            lambda x: self.onItemClickedOpen(x))

        self.layout().addWidget(self.list_bills_widget)
        self.layout().addWidget(self.read_area)

    def readBills(self):
        try:
            # access from root folder, subdirectories and files
            for root, subdir, files in os.walk(self.dirname):

                # for every file in files
                for filename in files:

                    # ignore if the file indicates the dummy.txt
                    if not filename.__eq__("dummy.txt"):
                        self.list_bills_data.append(filename)

            for bill in self.list_bills_data:
                date = datetime.fromtimestamp(int(os.path.splitext(bill)[0]))
                self.list_bills_widget.addItem(str(date))

        except Exception as e:
            print(e)

    def onItemClickedOpen(self, x):
        try:
            date = x.text()
            timestamp = int(datetime.timestamp(datetime.strptime(date, "%Y-%m-%d %H:%M:%S")))
            filename = f"{timestamp}.json"
            file_path = os.path.join(self.dirname, filename)
            with open(file_path) as json_file:
                data = json.load(json_file)

                self.read_area.clear()
                self.read_area.insertPlainText(
                    '{name:<{name_width}}{between}{qty:>{qty_width}}{between}{price:>{price_width}}\n'.format(
                        name="Name",
                        name_width=30,
                        between=' '*4,
                        qty="Qty",
                        qty_width=5,
                        price="Price",
                        price_width=10
                    ))

                self.read_area.insertPlainText(
                    ''.join([char * 53 for char in '-']))
                self.read_area.insertPlainText('\n')

                for item in data["order-list"]:
                    self.read_area.insertPlainText(
                        '{name:<{name_width}}{between}{qty:>{qty_width}}{between}{price:>{price_width}}\n'.format(
                            name=item["name"],
                            name_width=30,
                            between=' '*4,
                            qty=item["qty"],
                            qty_width=5,
                            price=item["price"],
                            price_width=10
                        ))

                self.read_area.insertPlainText(
                    ''.join([char * 53 for char in '-']))
                self.read_area.insertPlainText("\n{string:>{string_width}}".format(
                    string=f"Total: {data['total']}", string_width=53))
        except Exception as e:
            print(e)
