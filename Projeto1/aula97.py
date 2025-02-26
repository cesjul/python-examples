#essa conversao nao funciona para numeros maiores de que 100

class BaseConverter:
    def __init__(self, func):
        self._base = 8
        self.func = func
        

    def __call__(self, *args, **kwargs):
        a, b = args
        if a <= self._base:
            result_a = a
        else:
            result_a = int(str((a // self._base)) + str((a % self._base)))
        
        if b <= self._base:
            result_b = b
        else:
            result_b = int(str((b // self._base)) + str((b % self._base)))

        
        return result_a, result_b

@BaseConverter
def plus(x,y):
    return x + y

s = plus(30, 20)
print(s)