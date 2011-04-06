# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfase.ui'
#
# Created: Wed Jun 27 23:11:44 2007
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,346,301).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.lineResultado = QtGui.QLineEdit(self.groupBox)

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(152,152,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Light,brush)

        brush = QtGui.QBrush(QtGui.QColor(53,53,53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,178,254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.BrightText,brush)

        brush = QtGui.QBrush(QtGui.QColor(218,255,129))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(152,152,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Light,brush)

        brush = QtGui.QBrush(QtGui.QColor(53,53,53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,178,254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.BrightText,brush)

        brush = QtGui.QBrush(QtGui.QColor(218,255,129))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(152,152,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Light,brush)

        brush = QtGui.QBrush(QtGui.QColor(117,117,117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,178,254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.BrightText,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Base,brush)
        self.lineResultado.setPalette(palette)

        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.lineResultado.setFont(font)
        self.lineResultado.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineResultado.setAcceptDrops(False)
        self.lineResultado.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineResultado.setReadOnly(True)
        self.lineResultado.setObjectName("lineResultado")
        self.vboxlayout1.addWidget(self.lineResultado)
        self.vboxlayout.addWidget(self.groupBox)

        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(2)
        self.gridlayout.setObjectName("gridlayout")

        self.btn_op_mul = QtGui.QPushButton(self.centralwidget)

        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btn_op_mul.setFont(font)
        self.btn_op_mul.setObjectName("btn_op_mul")
        self.gridlayout.addWidget(self.btn_op_mul,2,4,1,1)

        self.btn_op_add = QtGui.QPushButton(self.centralwidget)

        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btn_op_add.setFont(font)
        self.btn_op_add.setObjectName("btn_op_add")
        self.gridlayout.addWidget(self.btn_op_add,0,4,1,1)

        self.btn_digit_9 = QtGui.QPushButton(self.centralwidget)
        self.btn_digit_9.setObjectName("btn_digit_9")
        self.gridlayout.addWidget(self.btn_digit_9,2,3,1,1)

        self.btn_digit_6 = QtGui.QPushButton(self.centralwidget)
        self.btn_digit_6.setObjectName("btn_digit_6")
        self.gridlayout.addWidget(self.btn_digit_6,1,3,1,1)

        self.btn_op_sub = QtGui.QPushButton(self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.btn_op_sub.setFont(font)
        self.btn_op_sub.setObjectName("btn_op_sub")
        self.gridlayout.addWidget(self.btn_op_sub,1,4,1,1)

        self.btn_digit_3 = QtGui.QPushButton(self.centralwidget)
        self.btn_digit_3.setObjectName("btn_digit_3")
        self.gridlayout.addWidget(self.btn_digit_3,0,3,1,1)

        self.btn_op_res = QtGui.QPushButton(self.centralwidget)

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.WindowText,brush)

        brush = QtGui.QBrush(QtGui.QColor(248,100,103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Button,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.ButtonText,brush)

        brush = QtGui.QBrush(QtGui.QColor(208,197,232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.AlternateBase,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.WindowText,brush)

        brush = QtGui.QBrush(QtGui.QColor(248,100,103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Button,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.ButtonText,brush)

        brush = QtGui.QBrush(QtGui.QColor(208,197,232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.AlternateBase,brush)

        brush = QtGui.QBrush(QtGui.QColor(117,117,117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.WindowText,brush)

        brush = QtGui.QBrush(QtGui.QColor(248,100,103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Button,brush)

        brush = QtGui.QBrush(QtGui.QColor(117,117,117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(117,117,117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.ButtonText,brush)

        brush = QtGui.QBrush(QtGui.QColor(208,197,232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.AlternateBase,brush)
        self.btn_op_res.setPalette(palette)

        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.btn_op_res.setFont(font)
        self.btn_op_res.setObjectName("btn_op_res")
        self.gridlayout.addWidget(self.btn_op_res,3,3,2,1)

        self.btn_op_div = QtGui.QPushButton(self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.btn_op_div.setFont(font)
        self.btn_op_div.setObjectName("btn_op_div")
        self.gridlayout.addWidget(self.btn_op_div,3,4,2,1)

        self.btn_digit_2 = QtGui.QPushButton(self.centralwidget)
        self.btn_digit_2.setObjectName("btn_digit_2")
        self.gridlayout.addWidget(self.btn_digit_2,0,2,1,1)

        self.btn_digit_5 = QtGui.QPushButton(self.centralwidget)
        self.btn_digit_5.setObjectName("btn_digit_5")
        self.gridlayout.addWidget(self.btn_digit_5,1,2,1,1)

        self.btn_digit_8 = QtGui.QPushButton(self.centralwidget)
        self.btn_digit_8.setObjectName("btn_digit_8")
        self.gridlayout.addWidget(self.btn_digit_8,2,2,1,1)

        self.btn_clear = QtGui.QPushButton(self.centralwidget)
        self.btn_clear.setObjectName("btn_clear")
        self.gridlayout.addWidget(self.btn_clear,3,2,2,1)

        self.btn_digit_1 = QtGui.QPushButton(self.centralwidget)
        self.btn_digit_1.setObjectName("btn_digit_1")
        self.gridlayout.addWidget(self.btn_digit_1,0,1,1,1)

        self.btn_digit_4 = QtGui.QPushButton(self.centralwidget)
        self.btn_digit_4.setObjectName("btn_digit_4")
        self.gridlayout.addWidget(self.btn_digit_4,1,1,1,1)

        self.btn_digit_7 = QtGui.QPushButton(self.centralwidget)
        self.btn_digit_7.setObjectName("btn_digit_7")
        self.gridlayout.addWidget(self.btn_digit_7,2,1,1,1)

        self.btn_digit_0 = QtGui.QPushButton(self.centralwidget)
        self.btn_digit_0.setObjectName("btn_digit_0")
        self.gridlayout.addWidget(self.btn_digit_0,3,1,2,1)
        self.vboxlayout.addLayout(self.gridlayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,346,29))
        self.menubar.setObjectName("menubar")

        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Calculadora", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Resultado:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineResultado.setToolTip(QtGui.QApplication.translate("MainWindow", "Resultado", None, QtGui.QApplication.UnicodeUTF8))
        self.lineResultado.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_op_mul.setText(QtGui.QApplication.translate("MainWindow", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_op_add.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_digit_9.setText(QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_digit_6.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_op_sub.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_digit_3.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_op_res.setText(QtGui.QApplication.translate("MainWindow", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_op_div.setText(QtGui.QApplication.translate("MainWindow", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_digit_2.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_digit_5.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_digit_8.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_clear.setText(QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_digit_1.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_digit_4.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_digit_7.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_digit_0.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("MainWindow", "Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))

