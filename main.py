import sys

from PyQt5.QtWidgets import QApplication


from MainWindow import MainWindow


# MAIN APP
app = QApplication(sys.argv)

# MAIN WINDOW
window = MainWindow(title="Management Restaurant")

# series = QPieSeries()
# series.append("Jane", 1)
# series.append("Joe", 2)
# series.append("Andy", 3)
# series.append("Barbara", 4)
# series.append("Axel", 5)

# slice = series.slices()[1]
# slice.setExploded()
# slice.setLabelVisible()
# slice.setPen(QPen(Qt.darkGreen, 2))
# slice.setBrush(Qt.green)

# for slice in series.slices():
#     slice.setBorderColor(Qt.red)
#     slice.setLabelColor(Qt.white)
#     slice.setLabelVisible()
#
# chart = QChart()
# chart.addSeries(series)
# chart.setTitle("Simple piechart example")
# chart.legend().hide()
# chart.setBackgroundVisible(False)
#
# chartView = QChartView(chart)
# chartView.setRenderHint(QPainter.Antialiasing)
#
# window = QMainWindow()
# window.setCentralWidget(chartView)
# window.resize(400, 300)
# window.setStyleSheet("background-color: red")
# window.show()

# RUN APP
if __name__ == "__main__":
    sys.exit(app.exec_())
