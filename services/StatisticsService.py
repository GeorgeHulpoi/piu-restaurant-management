class StatisticsService:
    widget = None

    @staticmethod
    def setWidget(widget):
        StatisticsService.widget = widget

    @staticmethod
    def showWidget():
        if StatisticsService.widget is not None:
            StatisticsService.widget.setVisible(True)

    @staticmethod
    def hideWidget():
        if StatisticsService.widget is not None:
            StatisticsService.widget.setVisible(False)
