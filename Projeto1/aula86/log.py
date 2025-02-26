from pathlib import Path
import datetime

LOG_FILE = Path(__file__).parent / 'log.text'

class Log:
    def _log(self, msg):
        raise NotImplementedError ('Implemente o metodo log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')

class LogFilesMixin(Log):
    def _log(self, msg):
        formatted_msg = f'{msg} using the class: {self.__class__.__name__} at {datetime.date.today()} {datetime.datetime.now().strftime("%H:%M:%S")}'
        with open(LOG_FILE, 'a', encoding='utf-8') as file:
            file.write(formatted_msg)
            file.write('\r')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} from {self.__class__.__name__}')


if __name__ == '__main__':
    log_file = LogFilesMixin()
    log_file.log_error('Something went wrong')
    log_file.log_sucess('Well done')
    l = LogPrintMixin()
    l.log_error('Something went wrong')
    l.log_sucess('Well done')