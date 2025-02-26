from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QGridLayout,
                               QMainWindow)
import sys



class MyWindow(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.font_size = 80
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setWindowTitle('PySide6 App')

        self.button = QPushButton('Aumenta')
        self.button1 = QPushButton('Diminui')
        self.button2 = QPushButton('Main Button')

        self.button.setStyleSheet('font-size:80px ;')
        self.button1.setStyleSheet('font-size:80px ;')
        self.button2.setStyleSheet('font-size:80px ;')

        layout = QGridLayout()
        self.central_widget.setLayout(layout)
        layout.addWidget(self.button, 2, 1)
        layout.addWidget(self.button1, 2, 2)
        layout.addWidget(self.button2, 1, 1, 1, 2)

        self.menu_bar = self.menuBar()
        self.first_menu = self.menu_bar.addMenu('Ola')
        self.first_action = self.first_menu.addAction('First Action')
        self.second_action = self.first_menu.addAction('Second Action')
        self.second_action.setCheckable(True)


        self.first_action.triggered.connect(self.slot_example)
        self.second_action.toggled.connect(self.another_slot)
        self.second_action.hovered.connect(self.another_slot)
        self.button.clicked.connect(self.increase_font_size)
        self.button1.clicked.connect(self.decrease_font_size)

        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Saiba mais')


    @Slot()
    def slot_example(self):
        self.status_bar.showMessage('the slot has been clicked')

    @Slot()
    def another_slot(self):
        print(self.second_action.isChecked())

    @Slot()
    def increase_font_size(self):
        self.font_size += 1
        self.button2.setStyleSheet(f'font-size:{self.font_size}px;')
        return self.font_size

    @Slot()
    def decrease_font_size(self):
        self.font_size -= 1
        self.button2.setStyleSheet(f'font-size:{self.font_size}px;')
        return self.font_size

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()