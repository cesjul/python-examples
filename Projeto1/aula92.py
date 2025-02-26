class Open:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self._file = None

    def __enter__(self):
        self._file = open(self.path, self.mode, encoding= 'utf-8')
        return self._file
    
    def __exit__(self, class_exception, exeception_, traceback_):
        self._file.close()

my_file = Open('Aula92.txt', 'w')

with my_file as file:
    ...