import os
import json
import collections

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from widgets.Statistics.BarChartWidget import BarChartWidget
from widgets.Statistics.PieChartWidget import PieChartWidget


class ContentWidget(QWidget):

    def __init__(self, parent):
        super(ContentWidget, self).__init__(parent)

        self.setUi()

    def setUi(self):
        piechart_data = {}          # initialise empty dictionary for piechart data
        piechart_labels = []        # initialise empty list for piechart labels
        piechart_quantities = []    # initialise empty list for piechart percentages

        # read the data recursevly from existing files
        self.readDataPieChart(
            f"{os.path.dirname(__file__)}/../TableOrderView/orders",
            piechart_data)

        # extract the data from the dictionary and append it to it's specific list
        for x in piechart_data:
            piechart_labels.append(x)
            piechart_quantities.append(piechart_data[x])

        self.setLayout(QHBoxLayout())
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.layout().setContentsMargins(32, 0, 32, 32)
        self.layout().setSpacing(0)
        self.layout().addWidget(PieChartWidget('Most Bought Products',
                                               piechart_labels, piechart_quantities, self))
        self.layout().addWidget(BarChartWidget('Time Clients', [
            '12:00 AM', '01:00 PM', '02:00 PM', '03:00 PM'], [3, 10, 20, 1], self))

    def readDataPieChart(self, dirname, out_dictionary):
        try:
            # auxiliary dictionary for local use
            dictionary = {}

            # access from root folder, subdirectories and files
            for root, subdirs, files in os.walk(dirname):

                # for every file in files
                for filename in files:

                    # ignore if the file indicates the dummy.txt
                    if not filename.__eq__("dummy.txt"):

                        # get the relative path from root to the actual file
                        file_path = os.path.join(root, filename)

                        # open the file
                        with open(file_path) as json_file:

                            # read and load data
                            data = json.load(json_file)

                            # iterate and create a dictionary where the key is name of the product
                            # and the value is the quantity of the product. also, if product already
                            # exists, increment they value for that key
                            for item in data["order-list"]:
                                if item["name"] in dictionary:
                                    dictionary[item["name"]] += item["qty"]
                                else:
                                    dictionary[item["name"]] = item["qty"]

            # order dictionary in descending order
            sorted_dictionary = collections.OrderedDict(
                sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True))

            # try get first top 4 most sold items
            if len(sorted_dictionary) >= 4:
                count = 0
                for x in sorted_dictionary:
                    out_dictionary[x] = sorted_dictionary[x]

                    if count < 3:
                        count += 1
                    else:
                        break
            # if there are not 4 items but len still is greater than 0
            elif len(sorted_dictionary) > 0:
                for x in sorted_dictionary:
                    out_dictionary[x] = sorted_dictionary[x]
            else:
                out_dictionary["Product"] = 1
        except Exception as e:
            print(e)
