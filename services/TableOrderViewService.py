class TableOrderViewService:
    widget = None

    @staticmethod
    def setWidget(widget):
        TableOrderViewService.widget = widget

    @staticmethod
    def showWidget(model):
        if TableOrderViewService.widget is not None:
            TableOrderViewService.widget.setVisible(True)

    @staticmethod
    def hideWidget():
        if TableOrderViewService.widget is not None:
            TableOrderViewService.widget.setVisible(False)

