from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox #импорт обьекта для всплывающих окон

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 401, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(255, 255, 255);")
        self.label_result.setObjectName("label_result")
        self.btn_zero = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zero.setGeometry(QtCore.QRect(0, 340, 301, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_zero.setFont(font)
        self.btn_zero.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_zero.setObjectName("btn_zero")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(0, 420, 401, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 260, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 260, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 260, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 180, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 180, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 180, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 100, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 100, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 100, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_9.setObjectName("btn_9")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(300, 100, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(300, 180, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_mult = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mult.setGeometry(QtCore.QRect(300, 260, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mult.setFont(font)
        self.btn_mult.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.btn_mult.setObjectName("btn_mult")
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(300, 340, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_divide.setFont(font)
        self.btn_divide.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.btn_divide.setObjectName("btn_divide")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions() # добавили функцию обработчика нажатия кнопок

        self.is_equal = False #метод для обнуления алгоритма при выводе результата

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.btn_zero.setText(_translate("MainWindow", "0"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_mult.setText(_translate("MainWindow", "*"))
        self.btn_divide.setText(_translate("MainWindow", "/"))

    def add_functions(self):
        self.btn_zero.clicked.connect(lambda: self.write_number(self.btn_zero.text())) #при нажатии на кнопку вызывается метод и передается в переменную number текст на кнопке
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_mult.clicked.connect(lambda: self.write_number(self.btn_mult.text()))
        self.btn_divide.clicked.connect(lambda: self.write_number(self.btn_divide.text()))

        self.btn_equal.clicked.connect(self.results)

    def write_number(self, number): #
        if self.label_result.text() == "0" or self.is_equal: #условие чтоб убрать 0
            self.label_result.setText(number)
            self.is_equal = False
        else:
            self.label_result.setText(self.label_result.text() + number)

    def results(self):
        if not self.is_equal:
            res = eval(self.label_result.text()) #eval высчитывает мат.действие представленное ввиде строки, разбивает строку на действия и цифры
            self.label_result.setText("Результат: " + str(res))
            self.is_equal = True
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Сейчас это действие выполнить нельзя")
            error.setIcon (QMessageBox.Icon.Information)
            error.setStandardButtons(QMessageBox.StandardButton.Reset|QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel)

            error.setDefaultButton(QMessageBox.StandardButton.Ok)
            error.setInformativeText("Два раза действие не выполнить")
            error.setDetailedText("Детали")

            error.buttonClicked.connect(self.popup_action)


            error.exec()

    def popup_action(self, btn):
        if btn.text() == "Ok":
            print("Print Ok")
        elif btn.text() == "Reset":
            self.label_result.setText("")
            self.is_equal: False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
