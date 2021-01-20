import os
import json
import collections

from datetime import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from widgets.Statistics.BarChartWidget import BarChartWidget
from widgets.Statistics.PieChartWidget import PieChartWidget


class ContentWidget(QWidget):

    def __init__(self, parent):
        super(ContentWidget, self).__init__(parent)

        self.items = {}
        self.clients = {}

        self.setUi()

    def setUi(self):
        self.setLayout(QHBoxLayout())
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.layout().setContentsMargins(32, 0, 32, 32)
        self.layout().setSpacing(0)
        self.createWidgets()

    def refresh(self):
        for i in reversed(range(self.layout().count())):
            self.layout().itemAt(i).widget().deleteLater()

        self.createWidgets()

    def createWidgets(self):
        self.readOrders()
        self.layout().addWidget(PieChartWidget('Most Bought Products',
                                               list(self.items.keys()), list(self.items.values()), self))
        self.layout().addWidget(BarChartWidget('Time Clients',
                                               list(self.clients.keys()), list(self.clients.values()), self))

    def readOrders(self):
        widgetsPath = os.path.dirname(os.path.dirname(__file__))
        d = {}
        t = {
            10: 0, 11: 0, 12: 0, 13: 0,
            14: 0, 15: 0, 16: 0, 17: 0,
            18: 0, 19: 0, 20: 0, 21: 0,
            22: 0, 23: 0
        }

        for root, subdirs, files in os.walk(os.path.join(widgetsPath, "TableOrderView", "orders")):
            for filename in files:
                if filename == "dummy.txt":
                    continue

                now = datetime.now()
                date = datetime.fromtimestamp(int(os.path.splitext(filename)[0]))

                if now.year != date.year or now.month != date.month or now.day != date.day:
                    continue

                t[date.hour] += 1
                filePath = os.path.join(root, filename)
                with open(filePath) as file:
                    data = json.load(file)
                    for item in data['order-list']:
                        if item['name'] in d:
                            d[item['name']] += int(item['qty'])
                        else:
                            d[item['name']] = int(item['qty'])

        d = collections.OrderedDict(sorted(d.items(), key=lambda kv: kv[1], reverse=True))

        c = 0
        for name, qty in d.items():
            c += 1
            if c >= 4:
                if 'Others' in self.items:
                    self.items['Others'] += qty
                else:
                    self.items['Others'] = qty
            else:
                self.items[name] = qty

        self.clients = dict(map(lambda kv: (self.convertHourToString(kv[0]), kv[1]), t.items()))

    def convertHourToString(self, value):
        if value > 12:
            return f"{value - 12} p.m."
        else:
            return f"{value} a.m."
