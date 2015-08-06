# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewmainwindow.ui'
#
# Created: Wed Aug  5 18:39:39 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ViewMainWindow(object):
    def setupUi(self, ViewMainWindow):
        ViewMainWindow.setObjectName(_fromUtf8("ViewMainWindow"))
        ViewMainWindow.resize(465, 155)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ViewMainWindow.sizePolicy().hasHeightForWidth())
        ViewMainWindow.setSizePolicy(sizePolicy)
        ViewMainWindow.setMinimumSize(QtCore.QSize(465, 155))
        ViewMainWindow.setMaximumSize(QtCore.QSize(465, 155))
        self.centralWidget = QtGui.QWidget(ViewMainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.searchButton = QtGui.QPushButton(self.centralWidget)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.gridLayout.addWidget(self.searchButton, 0, 0, 1, 1)
        self.filePath = QtGui.QLineEdit(self.centralWidget)
        self.filePath.setReadOnly(True)
        self.filePath.setObjectName(_fromUtf8("filePath"))
        self.gridLayout.addWidget(self.filePath, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelButton = QtGui.QPushButton(self.centralWidget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.convertButton = QtGui.QPushButton(self.centralWidget)
        self.convertButton.setObjectName(_fromUtf8("convertButton"))
        self.horizontalLayout.addWidget(self.convertButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        ViewMainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(ViewMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 465, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        ViewMainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(ViewMainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        ViewMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(ViewMainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        ViewMainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(ViewMainWindow)
        QtCore.QMetaObject.connectSlotsByName(ViewMainWindow)
        ViewMainWindow.setTabOrder(self.searchButton, self.filePath)
        ViewMainWindow.setTabOrder(self.filePath, self.convertButton)
        ViewMainWindow.setTabOrder(self.convertButton, self.cancelButton)

    def retranslateUi(self, ViewMainWindow):
        ViewMainWindow.setWindowTitle(_translate("ViewMainWindow", "Convertidor CSV a XML para el BNCR", None))
        self.searchButton.setText(_translate("ViewMainWindow", "Buscar", None))
        self.cancelButton.setText(_translate("ViewMainWindow", "Cancelar", None))
        self.convertButton.setText(_translate("ViewMainWindow", "Convertir", None))

