
class StatisticsWidgetService:
    widget = None

    @staticmethod
    def setWidget(widget):
        StatisticsWidgetService.widget = widget

    @staticmethod
    def showWidget():
        if StatisticsWidgetService.widget is not None:
            StatisticsWidgetService.widget.setVisible(True)

    @staticmethod
    def hideWidget():
        if StatisticsWidgetService.widget is not None:
            StatisticsWidgetService.widget.setVisible(False)
