class Meta(type):
    def __new__(mcs, cls_name, base, dict):
        cls = super().__new__(mcs, cls_name, base, dict)
        print(cls.__dict__)
        cls.defaut_value = 1
        return cls
    
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        print(instance.__dict__)
        return instance

class Num(metaclass = Meta):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name):
        self._name = name
        self.default_value = 1

    
num = Num('int')