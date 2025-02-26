from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt
from variables import AVG_FONT_SIZE, MIN_FONT_SIZE


class InfoLabel(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setStyleSheet(f'font-size: {MIN_FONT_SIZE}px;')

class HistoryLabel(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()
        

    def configStyle(self):
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setStyleSheet(f'font-size: {MIN_FONT_SIZE}px;')