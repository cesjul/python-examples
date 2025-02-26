from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, Signal, Slot, QThread
from worker import Ui_Form
import sys
from time import sleep

class Worker(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            sleep(1)
        self.finished.emit(value)

class MyWidget(QWidget, Ui_Form):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.hardWork1)
        self.pushButton_2.clicked.connect(self.hardWork2)
        
    def hardWork1(self):
        self._worker = Worker()
        self._thread = QThread()

        worker =  self._worker
        thread = self._thread

        worker.moveToThread(thread)

        thread.started.connect(worker.run)
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1Progressed)
        worker.finished.connect(self.worker1Finished)

        thread.start()

    def worker1Started(self, value):
        self.pushButton.setDisabled(True)
        self.label1.setText(value)
        print('iniciating process')
    
    def worker1Progressed(self, value): 
         print('in progress')
         self.label1.setText(value)
    
    def worker1Finished(self, value):
        self.pushButton.setDisabled(False)
        self.label1.setText(value)
        print('process finished')
    
    def hardWork2(self):
        self._worker2 = Worker()
        self._thread2 = QThread()

        worker2 =  self._worker2
        thread2 = self._thread2

        worker2.moveToThread(thread2)

        thread2.started.connect(worker2.run)
        worker2.finished.connect(thread2.quit)

        thread2.finished.connect(thread2.deleteLater)
        worker2.finished.connect(worker2.deleteLater)

        worker2.started.connect(self.worker2Started)
        worker2.progressed.connect(self.worker2Progressed)
        worker2.finished.connect(self.worker2Finished)

        thread2.start()

    def worker2Started(self, value):
        self.pushButton_2.setDisabled(True)
        self.label1.setText(value)
        print('iniciating process')
    
    def worker2Progressed(self, value): 
         print('in progress')
         self.label2.setText(value)
    
    def worker2Finished(self, value):
        self.pushButton_2.setDisabled(False)
        self.label2.setText(value)
        print('process finished')

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()

    widget.show()
    app.exec()