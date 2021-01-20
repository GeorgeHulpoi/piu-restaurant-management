from PyQt5.QtChart import QPieSeries, QChart, QChartView, QPieSlice
from PyQt5.QtGui import QPainter, QFont, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout


class PieChartWidget(QWidget):
    def __init__(self, title, labels, values, parent=None):
        super(PieChartWidget, self).__init__(parent)

        self.title = title
        if len(labels) != len(values):
            raise Exception('Labels have different value than values!')
        self.labels = labels
        self.values = values
        self.colors = [QColor("#004D2F"), QColor("#00331F"), QColor("#00995E"), QColor("#05374D"), QColor("#056C99"), QColor("#031F2B")]

        series = self.createSeries()
        chart = self.createChart(series)
        self.chartView = self.createChartView(chart, parent)

        self.setLayout(QHBoxLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().addWidget(self.chartView)

    def createSeries(self):
        series = QPieSeries()
        for i in range(len(self.labels)):
            series.append(self.labels[i], self.values[i])
        series.setLabelsPosition(QPieSlice.LabelInsideHorizontal)
        for slice in series.slices():
            slice.setLabelColor(Qt.white)
            slice.setLabelVisible(True)
            slice.setLabel("{:.2f}%".format(100 * slice.percentage()))
            slice.setColor(self.colors.pop())

        return series


    def createChart(self, series):
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(self.title)
        for i in range(len(self.labels)):
            font = QFont(chart.legend().markers(series)[i].font())
            font.setPixelSize(16)
            chart.legend().markers(series)[i].setFont(font)
            chart.legend().markers(series)[i].setLabel(self.labels[i])
        chart.legend().setLabelColor(Qt.white)
        chart.legend().setShowToolTips(True)
        chart.legend().setAlignment(Qt.AlignRight)
        chart.setBackgroundVisible(False)
        titleFont = QFont(chart.titleFont())
        titleFont.setPixelSize(22)
        chart.setTitleFont(titleFont)
        chart.setTitleBrush(QBrush(Qt.white));
        return chart

    def createChartView(self, chart, parent=None):
        chartView = QChartView(chart, parent)
        chartView.setRenderHint(QPainter.Antialiasing)
        return chartView
