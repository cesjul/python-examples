from log import LogFilesMixin, LogPrintMixin, Path

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False
    
    def ligar(self):
        if not self._ligado:
            self._ligado = True
    
    def desligar(self):
        if self._ligado:
            self._ligado = False

#Usando Log com Herenca Multipla
class Celular(Eletronico, LogFilesMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._bateria = False
    
    def carregar_bateria(self):
        if not self._bateria:
            self._bateria = True

    def ligar(self):
        super().ligar()
        self.log_sucess(f'{self._nome} foi ligado')
    
    def desligar(self):
        super().desligar()
        self.log_sucess(f'{self._nome} foi desligado')

#Usando Log com Composicao
class Tevelisao(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)
        self._log = None

    @property
    def log(self):
        return self._log
    
    @log.setter
    def log(self, value):
        self._log = value


    def ligar(self):
        super().ligar()
        return f'{self._nome} foi ligada'
    
    def desligar(self):
        super().desligar()


    def creat_log(self, msg):
        self._log.log_sucess(msg)

#Log com Composicao, porem instanciando internamente em Computador
class Computador(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)
        self._log_instance = None
        self._log_cls = None

    @property
    def log(self):
        return self._log_instance
    
    @log.setter
    def log(self, value):
        self._log_instance = value
    
    def create_instance_log(self, cls):
        self._log_cls = cls
        self._log_instance = self._log_cls()
    
    def ligar(self):
        super().ligar()
        self._log_instance.log_sucess(f'{self._nome} esta ligado at the module:{Path(__file__)}')
    
    

# celular = Celular('celular')
# celular.ligar()

# tele = Tevelisao('Televisao')
# log = LogPrintMixin()
# tele.log = log
# tele.creat_log(tele.ligar())

computador = Computador('PC')
computador.log = 'log'
computador.create_instance_log(LogFilesMixin)
computador.ligar()