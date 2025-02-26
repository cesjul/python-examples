#dunder method __call__



class Machine:
    def __init__(self, name) -> None:
        self.name = name
        self.status = False
    
    def __call__(self, who_calling):
        return f'The {self.name} has been activated by {who_calling}'

engine = Machine('engine')
print(engine('Director'))