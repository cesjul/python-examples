from typing import TYPE_CHECKING
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from variables import MAX_FONT_SIZE, TEXT_MARGIN, MIN_WIDTH
from PySide6.QtCore import Qt, Signal
from utils import isEmpty

class Display(QLineEdit):
    eqTriggered = Signal()
    eraseTriggered = Signal()
    clearTriggered = Signal()
    numTriggered = Signal(str)
    opTriggered = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        self.setStyleSheet(F'font-size:{MAX_FONT_SIZE}px;')
        self.setMinimumHeight(MAX_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN , TEXT_MARGIN)
        self.setMinimumWidth(MIN_WIDTH)
        
        

    def keyPressEvent(self, event: QKeyEvent) -> None:
        key = event.key()
        name = event.keyCombination()
        text = event.text().strip()
        KEYS = Qt.Key
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isErase = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isESC = key in [KEYS.Key_Escape]
        isNumOrDot = key in [KEYS.Key_0,KEYS.Key_1,KEYS.Key_2,KEYS.Key_3,
                         KEYS.Key_4,KEYS.Key_5,KEYS.Key_6,KEYS.Key_7,
                         KEYS.Key_8, KEYS.Key_9, KEYS.Key_Period]
        
        isOperator = key in [KEYS.Key_Plus, KEYS.Key_Minus,KEYS.Key_Slash,
                             KEYS.Key_Asterisk]
        
        
        if isEnter or text == '=' :
            self.eqTriggered.emit()
            return event.ignore()
        
        if isErase :
            self.eraseTriggered.emit()
            return event.ignore()

        if isESC :
            self.clearTriggered.emit()
            return event.ignore()

        if isNumOrDot:
            self.numTriggered.emit(text)
            return event.ignore()
        
        if isOperator :
            self.opTriggered.emit(text)
            return event.ignore()

        if isEmpty(text):
            return event.ignore()