import threading


class OAPThread(threading.Thread):
    def __init__(self, **kwargs):
        threading.Thread.__init__(self)
        self.name = kwargs.get('name')
        self.func = kwargs['target']
        self.args = kwargs.get('args', None)
        self.result = ''

    def run(self):
        if self.args is not None:
            self.result = self.func(*self.args)
        else:
            self.result = self.func()

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None
