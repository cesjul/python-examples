from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import AVG_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValid
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from typing import TYPE_CHECKING
from variables import HISTORY_ICON_PATH, MIN_WIDTH
import math

if TYPE_CHECKING:
    from display import Display
    from info import InfoLabel, HistoryLabel
    from main_window import MainWindow
    from styles import DARKEST_PRIMARY_COLOR
   
    

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        fontSize = self.font()
        fontSize.setPixelSize(AVG_FONT_SIZE)
        self.setFont(fontSize)
        self.setMinimumSize(75, 75)
        
        

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'InfoLabel', window : 'MainWindow', history : 'HistoryLabel', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]
        
        self.window = window     
        self.display = display
    
        self.info = info
        self._left_part = None
        self._right_part = None
        self._operator = None
        self._equation = ''
        self._equationInitialValue = 'Sua Conta'
        self.equation = self._equationInitialValue
        self.equations_list = []
        self.history = history
        self.menu = self.window.menuBar()
        self.historyMenu = self.menu.addMenu('Histórico')
        self.historyAction = self.historyMenu.addAction('Ver Histórico')
        self.createGridMask()
        
    
    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    

    def createGridMask(self):
        self.display.eqTriggered.connect(self._equal)
        self.display.eraseTriggered.connect(self._eraseTriggered)
        self.display.clearTriggered.connect(self._clear)
        self.display.numTriggered.connect(self.display.insert)
        self.display.opTriggered.connect(self._operatorSentByKeyboard)

        for i, row in enumerate(self._grid_mask):
            for j, column in enumerate(row):
                button = Button(column)
                
                if not isNumOrDot(column) and not isEmpty(column):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButtons(button)
                    
                self.addWidget(button, i, j)
                buttonSlot = self._makeSlot(
                    self._writeButtonTextOnDisplay, button
                )
                self._connectButtonClicked(button, buttonSlot)
                self.display.setFocus()
        
    def _connectButtonClicked(self, button: Button, slot):
        self.display.setFocus()
        button.clicked.connect(slot)
        

    def _configSpecialButtons(self, button: Button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text in '+-*/^':
            self._connectButtonClicked(
                button, 
                self._makeSlot(self._operatorClicked, button)
            )

        if text == '=':
            self._connectButtonClicked(
                button, self._equal
                
            )

        if text == '◀':
            self._connectButtonClicked(
                button, self._backSpace
            )

        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def slot():
            func(*args, **kwargs)
        return slot

    def _invertNumber(self):
        displayText = self.display.text()

        if not isValid(displayText):
            return
        
        invertedNumber = -float(displayText)
        self.display.setText(str(invertedNumber))
        self.display.setFocus()


    def _writeButtonTextOnDisplay(self, button: Button):
        newDisplayValue = self.display.text() + button.text()
        

        if not isValid(newDisplayValue):
            return
        else:
            self.display.insert(button.text())
    
    def _eraseTriggered(self):
        self.display.backspace()
        self.display.setFocus()
    

    def _clear(self):
        self._left_part = None
        self._right_part = None
        self._operator = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()

    def _operatorClicked(self, button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()
        
        if not isValid(displayText) and self._left_part is None:
            self._showError('Operação Inválida')
            return
        
        if self._left_part is None:
            self._left_part = float(displayText)
        
        self._operator = button.text()
        self.equation = f'{self._left_part} {self._operator} ...'
        self.display.setFocus()
    
    def _operatorSentByKeyboard(self, operator):
        text = operator

        displayText = self.display.text()
        self.display.clear()
        
        if not isValid(displayText) and self._left_part is None:
            self._showError('Operação Inválida')
            return
        
        if self._left_part is None:
            self._left_part = float(displayText)
        
        self._operator = text
        self.equation = f'{self._left_part} {self._operator} ...'
        self.display.setFocus()

    def _equal(self):
        displayText = self.display.text()

        if not isValid(displayText):
            self._showError('Digite um valor válido')
            return
        
        if self._left_part is None or self._operator is None:
            self._showError('Digite a operação')
            return

        self._right_part = float(displayText)
        self.equation = f'{self._left_part} {self._operator} '\
                        f'{self._right_part}'
        result = 0.0


        try:
            if '^' in self.equation and isinstance(self._left_part, float):
                result = math.pow(self._left_part, self._right_part) 
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            result = 'error'
            self._showError('Não é possivel dividir por zero')
            self._clear()

        except OverflowError:
            result = 'error'
            self._showStackOverFlowError('Não é possivel calcular numeros deste tamanho')
            self._clear()

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        
        self._left_part = result
        self._right_part = None

        if result == 'error':
            self._left_part = None
        self.display.setFocus()

    #     self.historyAction.triggered.connect(self.showHistory)

    # def showHistory(self):
    #     self.equations_list.append(self.equation)
       
    #     for equation in self.equations_list:
    #         self.history.setText(equation + '=' + str(eval(equation)) + '\n')

    #     self.history.show()

    
            
    def _backSpace(self):
        self.display.backspace()
        self.display.setFocus()
    
    def _showError(self, text):
        msgBox = self.window.makeMessageBox()
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.setText(text)
        msgBox.setWindowTitle('Calculadora')
        msgBox.exec()
        
    def _showStackOverFlowError(self, text):
        msgBox = self.window.makeMessageBox()
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.setStandardButtons(
            msgBox.StandardButton.Ok 
        )
        
        msgBox.setText(text)
        msgBox.setWindowTitle('Calculadora')
        result = msgBox.exec()

        # if result ==  msgBox.StandardButton.Help:
        #     msgBox.setButtonText(2,
        #         '''
        #         As máquinas usam o esquema binário, que adota apenas
        #         o 0 e o 1 como os únicos números
        #         para representar todos os outros.
        #         Apesar das vantagens na adoção desse conceito, 
        #         a união dele com a arquitetura de 32 bits de computadores
        #         acabou criando uma limitação que não pôde ser prevista.
        #         '''
        #     )

# class HistoryButton(QPushButton):
#     def __init__(self, history: 'HistoryLabel', window : 'MainWindow', display: 'Display', *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.configStyle()
#         self.setCheckable(True)
#         self.setChecked(True)
#         self.toggled.connect(self._slot(self._checked))
#         self.history : list = []
#         self.historyLabel = history
#         self.window_ = window
#         self.display = display
#         self._equation = None
#         self.defaultsize = (718, 584)
#         self.windowSize = (718, 584)
#         self.defaultWindowWidth = self.window_.width()
#         self.biggerItem = 0
#         self.reverseTimes = 0

#     def configStyle(self):
#         fontSize = self.font()
#         fontSize.setPixelSize(AVG_FONT_SIZE)
#         self.setFont(fontSize)
#         self.setFixedSize(110, 30)
    
    
#     def _slot(self, func, *args, **kwargs):
#         def inner():
#             return func(*args, **kwargs)
#         return inner

#     def _checked(self):
        # while self.isChecked():
        #     storaged_equations = ''
        #     currentItem = 0
        #     first_split = ''
        #     second_split = ''
            
        #     # self.window_.addWidgetToVlayout(self.historyLabel, 3, 2)
            
        #     for equation in self.history:
        #         if 'error' in equation :
        #             if self.historyLabel.text() == '':
        #                 self.historyLabel.hide()
        #                 self.window_.setFixedWidth(418)
        #                 return
        #             else:
        #                 continue
                
                
        #         print(equation, len(equation))
                
        #         if len(equation) >= 38:
        #             first_split, second_split = equation[:19], equation[19:]
        #             print(equation, len(equation))
        #             self.historyLabel.setText(first_split + '\n' + second_split)
                    
        #         if len(equation) < 38:
        #             storaged_equations += equation
        #             print(equation, len(equation))
        #             print(storaged_equations)
        #             self.historyLabel.setText(storaged_equations + '\n\r')
                    

                    

        #     if self.history == []:
        #         return
            
        #     self.historyLabel.show()

        #     if len(self.history[-1]) > 0:
        #         currentItem = len(self.history[-1])
        #         if currentItem > self.biggerItem:
        #             self.biggerItem = currentItem
                
        #     if self.biggerItem > 37 and self.biggerItem < 40:
        #         self.window_.setFixedWidth(int(440 + (11 * self.biggerItem)))
                
        #         print(self.historyLabel.size())
        #         self.window_.window_adjustment()
        #         return
            
        #     if self.biggerItem > 41 and self.biggerItem < 45:
        #         self.window_.setFixedWidth(int(450 + (11 * self.biggerItem)))
                
        #         print(self.historyLabel.size())
        #         self.window_.window_adjustment()
        #         return

        #     self.window_.setFixedWidth(int(428 + (11 * self.biggerItem)))
        #     self.window_.window_adjustment()

        #     if len(self.history) > 15:
        #         self.history.pop()

        #     break
        
        # while not self.isChecked():   
        #     self.display.setMaximumWidth(MIN_WIDTH)
        #     self.historyLabel.clear()
        #     self.historyLabel.hide()
        #     self.windowSize = (418, 584)
        #     self.window_.setFixedSize(*self.windowSize)
            
        #     break
        
        ...