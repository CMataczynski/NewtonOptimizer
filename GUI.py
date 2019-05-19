# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scaled.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import _thread
import time

from contextlib import redirect_stdout
from io import StringIO


from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import algorithm
import parse



class Ui_MainWindow(object):
    def setupUi(self, MainWindow,screen_resolution):
        self.browser_length = 0
        self.painting = False
        self.optimizing = False
        self.log = []
        self.function_accepted = False
        self.optimization_done = False
        self.function_list = [
            "x1^4+x2^4-0.62*x1^2-0.62*x2^2",
            "100*(x2-x1^2)^2+(1-x1)^2",
            "(x1-x2+x3)^2+(-x1+x2+x3)^2+(x1+x2-x3)^2",
            "(1+((x1+x2+1)^2)*(19-14*x1+3*x1^2-14*x2+6*x1*x2+3*x2^2))*((30+(2*x1-3*x2)^2)*(18-32*x1+12*x1^2+48*x2-36*x1*x2+27*x2^2))"
        ]
        self.function_names_list = [
            "Cztery minima lokalne",
            "Funkcja Zangwill'a",
            "Funkcja Rosenbrock'a",
            "Funkcja Goldstein'a-Price'a"
        ]
        self.help_list = [
            "Operatory: +, -, *, ^, /, (, )",
            "Stałe: e, pi, tau",
            "Funkcje Trygonometryczne: sin(), cos(), tan()",
            "Funkcje hiperbiliczne: sinh(), cosh(), tanh()",
            "Pierwiastek kwadratowy: sqrt()",
            "Logarytmy: log(), log10(), log2()",
            "Eksponenta: exp()"
        ]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(screen_resolution[0]/1.9, screen_resolution[1]/1.5)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_4.addWidget(self.comboBox_2,0,0,1,1)
        self.tabWidget.addTab(self.tab_3,"")
        self.verticalLayout.addWidget(self.tabWidget)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.groupBox = QtWidgets.QGroupBox(self.splitter_2)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 350))
        self.groupBox.setMaximumSize(QtCore.QSize(500, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.gridLayout_3.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_4.addWidget(self.lineEdit_7)
        self.gridLayout_3.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_5.addWidget(self.lineEdit_8)
        self.gridLayout_3.addWidget(self.groupBox_6, 0, 1, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_3.addWidget(self.lineEdit_9)
        self.gridLayout_3.addWidget(self.groupBox_7, 1, 1, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_8.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_2.addWidget(self.lineEdit_11)
        self.horizontalLayout_3.addWidget(self.groupBox_9)
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_6.addWidget(self.lineEdit_12)
        self.horizontalLayout_3.addWidget(self.groupBox_10)
        self.verticalLayout_7.addWidget(self.groupBox_8)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setMinimumSize(QtCore.QSize(100, 0))
        self.splitter.setMaximumSize(QtCore.QSize(190, 14989629))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setMaximumSize(QtCore.QSize(190, 150))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setMaximumSize(QtCore.QSize(190, 150))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_11 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_11.setMinimumSize(QtCore.QSize(100, 100))
        self.groupBox_11.setMaximumSize(QtCore.QSize(190, 14989319))
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_11)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_12.setObjectName("groupBox_12")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_12)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_12)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_9.addWidget(self.lineEdit_13)
        self.verticalLayout_8.addWidget(self.groupBox_12)
        self.widget = QtWidgets.QVBoxLayout(self.splitter_2)
        #self.widget.setMinimumSize(QtCore.QSize(300, 300))
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.splitter_2)
        self.textBrowser = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setMinimumSize(QtCore.QSize(500, 0))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        MainWindow.setCentralWidget(self.centralwidget)

        self.comboBox.addItems(self.function_list)
        self.comboBox_2.addItems(self.help_list)
        self.function_string = self.comboBox.itemText(self.comboBox.currentIndex())
        self.input_daemon()
        self.comboBox.currentTextChanged.connect(self.combobox_input_daemon)

        self.pushButton.clicked.connect(self.threaded_optimize)
        self.pushButton_2.clicked.connect(self.threaded_paint)
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)

        #Wprowadzanie punktu początkowego
        self.lineEdit.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_2.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_3.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_4.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_4.setValidator(QtGui.QDoubleValidator())

        #Parametry
        self.lineEdit_6.setValidator(QtGui.QIntValidator())
        self.lineEdit_7.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_8.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_9.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_11.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_12.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_13.setValidator(QtGui.QIntValidator())
        self.lineEdit_10.setStyleSheet("background-color: red;")
        self.lineEdit_10.textChanged.connect(self.user_input_daemon)

        #Wykres
        self.figure = Figure()
        self.figure.set_tight_layout(True)
        self.canvas = FigureCanvas(self.figure)
        self.widget.addWidget(self.canvas)
        self.figure.set_facecolor("silver")
        self.ax = self.figure.add_subplot(111)
        self.ax.clear()
        self.ax.set_facecolor("silver")


        try:
            _thread.start_new_thread(self.daemon,())
        except:
            print("Nie mozna wystartowac watku dla daemona")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Optymalizacja"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Wybierz funkcję"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "Tutaj wpisz własną funkcję"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Wpisz własną funkcję"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Pomoc"))
        self.groupBox.setTitle(_translate("MainWindow", "Parametry"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Punkt początkowy x0"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Parametry algorytmu Newtona"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Liczba iteracji"))
        self.lineEdit_6.setText(_translate("MainWindow", "1000"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Epsilon 1"))
        self.lineEdit_7.setText(_translate("MainWindow", "1e-8"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Epsilon 2"))
        self.lineEdit_8.setText(_translate("MainWindow", "1e-8"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Epsilon 3"))
        self.lineEdit_9.setText(_translate("MainWindow", "1e-8"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Parametry minimalizacji w kierunku"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Początkowy krok"))
        self.lineEdit_11.setText(_translate("MainWindow", "10"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Współczynnik testu"))
        self.lineEdit_12.setText(_translate("MainWindow", "0.6"))
        self.pushButton.setText(_translate("MainWindow", "Optymalizuj"))
        self.pushButton_2.setText(_translate("MainWindow", "Rysiuj"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Wykres"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Rozdzielczość"))
        self.lineEdit_13.setText(_translate("MainWindow", "256"))

    def daemon(self):
        while True:
            time.sleep(0.1)
            if not self.painting and not self.optimizing:
                if self.function_accepted is False:
                    self.pushButton.setEnabled(False)
                elif self.lineEdit.isEnabled() and self.lineEdit.text() is "":
                    self.pushButton.setEnabled(False)
                elif self.lineEdit_2.isEnabled() and self.lineEdit_2.text() is "":
                    self.pushButton.setEnabled(False)
                elif self.lineEdit_3.isEnabled() and self.lineEdit_3.text() is "":
                    self.pushButton.setEnabled(False)
                elif self.lineEdit_4.isEnabled() and self.lineEdit_4.text() is "":
                    self.pushButton.setEnabled(False)
                elif self.lineEdit_5.isEnabled() and self.lineEdit_5.text() is "":
                    self.pushButton.setEnabled(False)
                elif self.lineEdit_6.isEnabled() and self.lineEdit_6.text() is "":
                    self.pushButton.setEnabled(False)
                elif self.lineEdit_7.isEnabled() and self.lineEdit_7.text() is "":
                    self.pushButton.setEnabled(False)
                elif self.lineEdit_8.isEnabled() and self.lineEdit_8.text() is "":
                    self.pushButton.setEnabled(False)
                elif self.lineEdit_9.isEnabled() and self.lineEdit_9.text() is "":
                    self.pushButton.setEnabled(False)
                elif self.lineEdit_11.isEnabled() and self.lineEdit_11.text() is "":
                    self.pushButton.setEnabled(False)
                elif self.lineEdit_12.isEnabled() and self.lineEdit_12.text() is "":
                    self.pushButton.setEnabled(False)
                else:
                    self.pushButton.setEnabled(True)

                if self.optimization_done is True and self.lineEdit_13.text() is not "":
                    if self.Optimizer.function.number_of_variables == 2:
                        self.pushButton_2.setEnabled(True)
                    else:
                        self.pushButton_2.setEnabled(False)
                else:
                    self.pushButton_2.setEnabled(False)



    def combobox_input_daemon(self):
        self.function_string = self.comboBox.itemText(self.comboBox.currentIndex())
        self.input_daemon()

    def user_input_daemon(self):
        self.function_string = self.lineEdit_10.text()
        self.input_daemon()

    def input_daemon(self):
        try:
            self.function = parse.FunctionParse(self.function_string)
            self.lineEdit_10.setStyleSheet("background-color: white;")
            num = self.function.nov()
            if num == 0:
                raise Exception("brak zmiennych")
            if num >= 1:
                self.lineEdit.setEnabled(True)
                self.lineEdit.setText("0")
                self.lineEdit_2.setText("")
                self.lineEdit_2.setEnabled(False)
                self.lineEdit_3.setText("")
                self.lineEdit_3.setEnabled(False)
                self.lineEdit_4.setText("")
                self.lineEdit_4.setEnabled(False)
                self.lineEdit_5.setText("")
                self.lineEdit_5.setEnabled(False)
            if num >= 2:
                self.lineEdit_2.setEnabled(True)
                self.lineEdit_2.setText("0")
                self.lineEdit_3.setText("")
                self.lineEdit_3.setEnabled(False)
                self.lineEdit_4.setText("")
                self.lineEdit_4.setEnabled(False)
                self.lineEdit_5.setText("")
                self.lineEdit_5.setEnabled(False)
            if num >= 3:
                self.lineEdit_3.setEnabled(True)
                self.lineEdit_3.setText("0")
                self.lineEdit_4.setText("")
                self.lineEdit_4.setEnabled(False)
                self.lineEdit_5.setText("")
                self.lineEdit_5.setEnabled(False)
            if num >= 4:
                self.lineEdit_4.setEnabled(True)
                self.lineEdit_4.setText("0")
                self.lineEdit_5.setText("")
                self.lineEdit_5.setEnabled(False)
            if num >= 5:
                self.lineEdit_5.setEnabled(True)
                self.lineEdit_5.setText("0")
            self.function_accepted = True
        except:
            self.lineEdit.setEnabled(False)
            self.lineEdit.setText("")
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_2.setText("")
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_3.setText("")
            self.lineEdit_4.setEnabled(False)
            self.lineEdit_4.setText("")
            self.lineEdit_5.setEnabled(False)
            self.lineEdit_5.setText("")
            self.lineEdit_10.setStyleSheet("background-color: red;")
            self.function_accepted = False

    def threaded_optimize(self):
        if not self.optimizing:
            try:
                self.optimizing = True
                self.textBrowser.clear()
                self.ax.clear()
                self.figure.clear()
                self.pushButton.setEnabled(False)
                _thread.start_new_thread(self.optimize, ())
                while not self.optimization_done:
                    time.sleep(0.2)
                message = ""
                for l in self.log:
                    message += l
                self.textBrowser.setPlainText(message)
                self.textBrowser.moveCursor(QtGui.QTextCursor.End)
            except:
                print("Nie udalo sie utworzyc watku dla optymalizacji")

    def optimize(self):
        self.log = []

        point = {}
        if self.lineEdit.isEnabled():
            point["x1"] = float(self.lineEdit.text())
        if self.lineEdit_2.isEnabled():
            point["x2"] = float(self.lineEdit_2.text())
        if self.lineEdit_3.isEnabled():
            point["x3"] = float(self.lineEdit_3.text())
        if self.lineEdit_4.isEnabled():
            point["x4"] = float(self.lineEdit_4.text())
        if self.lineEdit_5.isEnabled():
            point["x5"] = float(self.lineEdit_5.text())

        self.starting_point = point
        self.epsilon_1 = float(self.lineEdit_7.text())
        self.epsilon_2 = float(self.lineEdit_8.text())
        self.epsilon_3 = float(self.lineEdit_9.text())
        self.number_of_iterations = int(self.lineEdit_6.text())
        self.step = float(self.lineEdit_11.text())
        self.test = float(self.lineEdit_12.text())
        self.Optimizer = algorithm.NewtonOptimizer(self.function, self.starting_point, self.epsilon_1,
                                                   self.epsilon_2, self.epsilon_3, self.number_of_iterations,
                                                   self.step, self.test)
        print("optimization start")
        self.log.append(str(self.Optimizer))
        while self.Optimizer.optimize_step():
            print(len(self.Optimizer))
            self.log.append('krok: ' + str(len(self.Optimizer))+'\n')
            self.log.append(str(self.Optimizer))

        self.log.append('krok: ' + str(len(self.Optimizer))+'\n')
        self.log.append(str(self.Optimizer))
        self.log.append(str(self.Optimizer.why()))
        self.pushButton.setEnabled(True)
        self.optimization_done = True
        self.optimizing = False
        print("optimization done")


    def threaded_paint(self):
        try:
            self.painting = True
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(False)
            _thread.start_new_thread(self.paint, ())
        except:
            print("Nie udalo sie utworzyc watku dla rysowania")

    def paint(self):
        self.figure.clear()
        img = self.Optimizer.show_image()
        self.ax = self.figure.add_subplot(111)
        self.ax.clear()
        self.ax.set_autoscale_on(True)
        self.ax.set_facecolor("silver")
        mappable = self.ax.imshow(img["imshow"][0], cmap="hot", extent=img["imshow"][1], aspect=img["imshow"][2])
        self.ax.plot(img["plot1"][0],img["plot1"][1],linestyle='-',marker = 's', color = 'grey')
        self.ax.plot(img["plot2"][0],img["plot2"][1],marker = 's',color = 'blue')
        self.figure.colorbar(mappable,ax=self.ax)
        self.canvas.draw()
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.painting = False
        _thread.exit()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen = app.desktop().screenGeometry()
    width = screen.width()
    height = screen.height()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, [width, height])
    MainWindow.show()
    sys.exit(app.exec_())
