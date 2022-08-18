class Singleton(type):

    # Define an Instance operation that lets clients access its uniqueinstance.

    def init(cls, name, bases, attrs, kwargs):
        super().init(name, bases, attrs)
        cls._instance = None

    def call(cls, *args, kwargs):
        if cls._instance is None:
            cls._instance = super().call(*args, **kwargs)
        return cls._instance