class Sinleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super(Sinleton, self).__call__(*args, **kwargs)
        return self._instance
