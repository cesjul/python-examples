from PySide6.QtCore import Slot
from PySide6.QtWidgets import ( QWidget, QVBoxLayout, QGridLayout,
                               QMainWindow, QHBoxLayout, QMessageBox, )
from PySide6.QtGui import QIcon
from variables import ICON_PATH

class MainWindow(QMainWindow):
    def __init__(self, parent : QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.central_widget = QWidget()
        self.side_widget = QWidget()
        self.vLayout = QGridLayout()
        self.vSideLayout = QHBoxLayout()
        self.central_widget.setLayout(self.vLayout)
        self.central_widget.setLayout(self.vSideLayout)
        # self.side_widget.setLayout(self.vSideLayout)
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Calculadora')

        icon = QIcon(str(ICON_PATH))
        self.setWindowIcon(icon)

    def window_adjustment(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVlayout(self, widget: QWidget, *args):
        self.vLayout.addWidget(widget, *args)
    
    def makeMessageBox(self):
        return QMessageBox(self)