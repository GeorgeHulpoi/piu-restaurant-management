class TableOrderService:
    widget = None

    @staticmethod
    def setWidget(widget):
        TableOrderService.widget = widget

    @staticmethod
    def showWidget():
        if TableOrderService.widget is not None:
            TableOrderService.widget.setVisible(True)

    @staticmethod
    def hideWidget():
        if TableOrderService.widget is not None:
            TableOrderService.widget.setVisible(False)
