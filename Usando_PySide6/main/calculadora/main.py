from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QVBoxLayout,
                               QMainWindow, QLabel, )
import sys
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import ICON_PATH
from display import Display
from info import InfoLabel, HistoryLabel
from styles import setupTheme
from button import Button, ButtonsGrid

equations_list = []

if __name__ == '__main__':
    # create app and window
    app = QApplication(sys.argv)
    window = MainWindow()
    setupTheme(app)

    #create window icon
    icon = QIcon(str(ICON_PATH))
    
    #history label
    history = HistoryLabel('')
    
    #info label
    info = InfoLabel('')
    window.vLayout.addWidget(info, 0, 1)

    #create display
    display = Display()
    window.vLayout.addWidget(display, 1, 1)
    display.setPlaceholderText('Insira um número')

    #history button
    
    # window.vLayout.addWidget(historyButton, 2, 1)

    #grid
    button_grid = ButtonsGrid(display, info, window, history)
    window.vLayout.addLayout(button_grid, 3, 1)
    
    # set app and window icon
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.show()
    app.exec()