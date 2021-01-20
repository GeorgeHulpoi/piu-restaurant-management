class OrderHistoryService:
    widget = None

    @staticmethod
    def setWidget(widget):
        OrderHistoryService.widget = widget

    @staticmethod
    def showWidget():
        if OrderHistoryService.widget is not None:
            OrderHistoryService.widget.setVisible(True)

    @staticmethod
    def hideWidget():
        if OrderHistoryService.widget is not None:
            OrderHistoryService.widget.setVisible(False)
