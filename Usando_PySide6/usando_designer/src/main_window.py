from window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import QKeyEvent
from typing import cast
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.sendButton.clicked.connect(self._slot(
                self.sendClicked
        ))

        self.lineName.installEventFilter(self)
    
    def _slot(self, func, *args, **kwargs):
        def inner():
            return func(*args, **kwargs)
        return inner
    
    def sendClicked(self):
        text = self.lineName.text()
        self.labelResult.setText(text)
        
    def eventFilter(self, watched : QObject, event: QEvent) -> bool:

        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            print(event.text())

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
