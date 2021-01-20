from PyQt5.QtChart import QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis, QHorizontalBarSeries
from PyQt5.QtGui import QPainter, QFont, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout


class BarChartWidget(QWidget):
    def __init__(self, title, labels, values, parent=None):
        super(BarChartWidget, self).__init__(parent)

        self.title = title
        if len(labels) != len(values):
            raise Exception('Labels have different value than values!')
        self.labels = labels
        self.values = values

        series = self.createSeries()
        chart = self.createChart(series)
        self.chartView = self.createChartView(chart, parent)

        self.setLayout(QHBoxLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().addWidget(self.chartView)

    def createSeries(self):
        series = QHorizontalBarSeries()
        set = QBarSet("value")
        for i in range(len(self.values)):
            set.append(self.values[i])
        series.append(set)
        return series


    def createChart(self, series):
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(self.title)

        axisX = QBarCategoryAxis()
        axisX.append(self.labels)
        labelsFont = QFont(axisX.labelsFont())
        labelsFont.setPixelSize(14)
        axisX.setLabelsFont(labelsFont)
        axisX.setLabelsColor(QColor(Qt.white))

        axisY = QValueAxis()
        axisY.setTitleBrush(QBrush(QColor(Qt.white)))
        axisY.setTitleText("Clients")
        labelsFont = QFont(axisY.labelsFont())
        labelsFont.setPixelSize(14)
        axisY.setLabelsFont(labelsFont)
        axisY.setLabelsColor(QColor(Qt.white))
        axisY.setRange(0, max(self.values))
        axisY.applyNiceNumbers()

        chart.addAxis(axisX, Qt.AlignLeft)
        chart.addAxis(axisY, Qt.AlignBottom)
        chart.setBackgroundVisible(False)
        titleFont = QFont(chart.titleFont())
        titleFont.setPixelSize(22)
        chart.setTitleFont(titleFont)
        chart.setTitleBrush(QBrush(Qt.white))
        chart.legend().setVisible(False)

        return chart

    def createChartView(self, chart, parent=None):
        chartView = QChartView(chart, parent)
        chartView.setRenderHint(QPainter.Antialiasing)
        return chartView
