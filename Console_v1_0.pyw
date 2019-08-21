# Консоль управления 10 портами Arduino Uno

from pyfirmata import Arduino
import sys, sets, time #, pygame
from time import sleep

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QCoreApplication

#from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets


# Окно пользователя
from window import Ui_Dialog

board = Arduino('COM3') # Выбор порта USB
#board = Arduino(Arduino.AUTODETECT)

def key_exit(): # Кнопка "Закрыть"
    sys.exit(app.exec_())

def invert (value): # Инвертируем значение порта
    if value == 0:
        value = 1
    else:
        value = 0
    return value

def check_on():
    global port1
    port1 = invert(port1)
    print("check_on 1 =", port1)
    board.digital[13].write(port1)

def check_on2():
    global port2
    port2 = invert(port2)
    print("check_on 2 =", port2)
    board.digital[12].write(port2)

def check_on3():
    global port3
    port3 = invert(port3)
    print("check_on 3 =", port3)
    board.digital[11].write(port3)

def check_on4():
    global port4
    port4 = invert(port4)
    print("check_on 4 =", port4)
    board.digital[10].write(port4)

def check_on5():
    global port5
    port5 = invert(port5)
    print("check_on 5 =", port5)
    board.digital[9].write(port5)

def check_on6():
    global port6
    port6 = invert(port6)
    print("check_on 6 =", port6)
    board.digital[8].write(port6)

def check_on7():
    global port7
    port7 = invert(port7)
    print("check_on 7 =", port7)
    board.digital[7].write(port7)

def check_on8():
    global port8
    port8 = invert(port8)
    print("check_on 8 =", port8)
    board.digital[6].write(port8)

def check_on9():
    global port9
    port9 = invert(port9)
    print("check_on 9 =", port9)
    board.digital[5].write(port9)

def check_on10():
    global port10
    port10 = invert(port10)
    print("check_on 10 =", port10)
    board.digital[4].write(port10)
    
# Начальное значение портов
port1 = 0
port2 = 0
port3 = 0
port4 = 0
port5 = 0
port6 = 0
port7 = 0
port8 = 0
port9 = 0
port10 = 0

# Инициализация приложения
app = QtWidgets.QApplication(sys.argv)

# Вывод формы
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

# -----------------
# Обработка событий
# -----------------

# Проверка нажатия кнопки с именем "pushButton"
# для запуска функции "key_exit"
ui.pushButton.clicked.connect(key_exit)

ui.checkBox.clicked.connect(check_on)
ui.checkBox_2.clicked.connect(check_on2)
ui.checkBox_3.clicked.connect(check_on3)
ui.checkBox_4.clicked.connect(check_on4)
ui.checkBox_5.clicked.connect(check_on5)
ui.checkBox_6.clicked.connect(check_on6)
ui.checkBox_7.clicked.connect(check_on7)
ui.checkBox_8.clicked.connect(check_on8)
ui.checkBox_9.clicked.connect(check_on9)
ui.checkBox_10.clicked.connect(check_on10)

# Закрытие приложения
sys.exit(app.exec_())
