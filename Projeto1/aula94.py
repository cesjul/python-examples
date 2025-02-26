# decorators em classes

def add_repr(cls):
    def repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = repr
    return cls

@add_repr
class Class_:
    def __init__(self, attr):
        self.attr = attr
    
Class_('attribut')
print(Class_('attribut'))