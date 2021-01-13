from rx.subject import Subject


class WindowService:
    instance = None
    resizeSubject = Subject()

    @staticmethod
    def setInstance(instance):
        WindowService.instance = instance
