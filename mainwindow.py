# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 881)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_12.addWidget(self.label_18)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.line_3 = QtWidgets.QFrame(self.groupBox_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_9.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_13.addWidget(self.label_19)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_13.addWidget(self.pushButton_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_8.addWidget(self.lineEdit_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_7.addWidget(self.lineEdit_5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_10.addWidget(self.label_15)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_3.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_3.addWidget(self.radioButton_4)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.line_4 = QtWidgets.QFrame(self.groupBox_4)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_8.addWidget(self.line_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_6.addWidget(self.label_17)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_6.addWidget(self.pushButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_9.addWidget(self.groupBox_4)
        self.horizontalLayout_15.addLayout(self.verticalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = PlotWidget(self.groupBox)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_11.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.graphicsView_2 = PlotWidget(self.groupBox_2)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_4.addWidget(self.graphicsView_2)
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_11.addWidget(self.groupBox_2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 12)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setTearOffEnabled(False)
        self.menu.setObjectName("menu")
        self.menuSave_as_CSV = QtWidgets.QMenu(self.menu)
        self.menuSave_as_CSV.setObjectName("menuSave_as_CSV")
        MainWindow.setMenuBar(self.menuBar)
        self.actionaaa = QtWidgets.QAction(MainWindow)
        self.actionaaa.setObjectName("actionaaa")
        self.menuSave_as_CSV.addSeparator()
        self.menu.addAction(self.menuSave_as_CSV.menuAction())
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VLC Demod"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Channel-1 Config"))
        self.label_18.setText(_translate("MainWindow", "选择数据源"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "len4020_32QAM_80M_Sym_60M_Cen.csv"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "zeros_len4020_32QAM_80M_Sym_60M_Cen.csv"))
        self.label.setText(_translate("MainWindow", "解调方式"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Qam32"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Qam64"))
        self.label_7.setText(_translate("MainWindow", "码元速率"))
        self.label_8.setText(_translate("MainWindow", "载波频率"))
        self.label_9.setText(_translate("MainWindow", "滤波器系数"))
        self.label_14.setText(_translate("MainWindow", "数字均衡"))
        self.radioButton.setText(_translate("MainWindow", "Run"))
        self.radioButton_2.setText(_translate("MainWindow", "Hold"))
        self.label_16.setText(_translate("MainWindow", "通道状态 ："))
        self.pushButton.setText(_translate("MainWindow", "START DEMOD"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP DEMOD"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Channel-2 Config"))
        self.label_19.setText(_translate("MainWindow", "选择数据源"))
        self.pushButton_6.setText(_translate("MainWindow", "文件"))
        self.label_11.setText(_translate("MainWindow", "解调方式"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Qam32"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Qam64"))
        self.label_13.setText(_translate("MainWindow", "码元速率"))
        self.label_12.setText(_translate("MainWindow", "载波频率"))
        self.label_10.setText(_translate("MainWindow", "滤波器系数"))
        self.label_15.setText(_translate("MainWindow", "数字均衡"))
        self.radioButton_3.setText(_translate("MainWindow", "Run"))
        self.radioButton_4.setText(_translate("MainWindow", "Hold"))
        self.label_17.setText(_translate("MainWindow", "通道状态 ："))
        self.pushButton_3.setText(_translate("MainWindow", "START DEMOD"))
        self.pushButton_4.setText(_translate("MainWindow", "STOP DEMOD"))
        self.groupBox.setTitle(_translate("MainWindow", "Channel-1"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">实时通信速率:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">误码率:</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Channel-2"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">实时通信速率:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">误码率:</span></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.menuSave_as_CSV.setTitle(_translate("MainWindow", "Save as CSV"))
        self.actionaaa.setText(_translate("MainWindow", "aaa"))

from pyqtgraph import PlotWidget
