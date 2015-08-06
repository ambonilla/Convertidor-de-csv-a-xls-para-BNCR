#!/bin/usr/env/python
# -*- coding: utf-8 -*-

from ViewMainWindow import Ui_ViewMainWindow
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QMessageBox
from CsvReader import ExcelCreator
import csv
import sys

class MainWindow(QMainWindow):

   def __init__(self):
      super(MainWindow, self).__init__()
      self.ui = Ui_ViewMainWindow()
      self.ui.setupUi(self)
      self.show()
      self.setupButtons()
      self.openFilePath = ""

   def setupButtons(self):
      self.ui.cancelButton.clicked.connect(self.close)
      self.ui.searchButton.clicked.connect(self.getData)
      self.ui.convertButton.clicked.connect(self.exportData)

   def getData(self):
      self.openFilePath = QFileDialog.getOpenFileName(filter=u'Archivo CSV (*.csv)')
      self.ui.filePath.setText(self.openFilePath)


   def exportData(self):
      
      if str(self.openFilePath).strip():
        queryStr = u'¿Desea convertir el archivo?'
        reply = QMessageBox.question(self, u'Confirmación',
                                     queryStr,
                                     "No",
                                     button1Text = "Si")
        if reply == 1:
           self.saveFilePath = QFileDialog.getSaveFileName(filter=u'Hoja de Cálculo (*.xls)')
           self.openCsvFile()
      else:
         QMessageBox.critical(self, "Error", u'Por favor seleccione el archivo a convertir.')

           
   def openCsvFile(self):
      try:
         self.excelCreator = ExcelCreator()
         csvfile = open(self.openFilePath, 'rb')
         filedata = csv.reader(csvfile, delimiter=';')
         for linenumber, row in enumerate(filedata):
            totalcolumns = len(row)
            for columnnumber, column in enumerate(row):
               if column.strip() or columnnumber + 1 < totalcolumns:
                  self.excelCreator.inputData(linenumber, columnnumber, column)
         self.excelCreator.saveFile(self.saveFilePath)
         QMessageBox.information(self, "Aviso", u'Archivo guardado.')
         self.ui.filePath.setText("")


      except:
         QMessageBox.critical(self, "Error", u'El archivo no se pudo convertir.\nPor favor revise que esté en formato csv y sea del Banco Nacional.')






def main():
   app = QApplication(sys.argv)
   newWindow = MainWindow()
   sys.exit(app.exec_())



if __name__ == "__main__":
   main()
