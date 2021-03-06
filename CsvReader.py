import csv
import xlwt
from xlwt import Font
from xlwt import XFStyle
from xlwt import Alignment
from xlwt import Borders

from sys import argv

class ExcelCreator():


   def __init__(self):
       self.createFile()
       self.setupFormat()

   def createFile(self):
        self.book = xlwt.Workbook(encoding="utf-8")
        self.sheet1 = self.book.add_sheet("Reporte")

   def setupFormat(self):
        headFont = Font()
        headFont.bold = True
        alignmentSetup = Alignment()
        alignmentSetup.wrap = True
        borders = Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1

        self.header_style = XFStyle()
        self.header_style.font = headFont

        self.table_style = XFStyle()
        self.table_style.borders = borders
        self.table_style.alignment = alignmentSetup
        
   def saveFile(self, filename):
      filename = str(filename)
      if filename.endswith(".xls"):
         self.book.save(filename)
      else:
         self.book.save(filename + ".xls")

   def inputData(self, row, column, data):
      if row == 0:
         self.sheet1.write(row, column, data, self.header_style)
      elif row > 1:
         self.sheet1.write(row - 1, column, data, self.table_style)   

def open_csv_file(inputFilename, outputFilename):
   try:
      excelCreator = ExcelCreator()
      csvfile = open(inputFilename, 'rb')
      filedata = csv.reader(csvfile, delimiter=';')
      for linenumber, row in enumerate(filedata):
         totalcolumns = len(row)
         for columnnumber, column in enumerate(row):
            if column.strip() or columnnumber + 1 < totalcolumns:
               excelCreator.inputData(linenumber, columnnumber, column)
      excelCreator.saveFile(outputFilename)
      return True

   except:
      return False
      print "No se puede leer el archivo"

if __name__ == "__main__":
   try:
      script, filename = argv
      open_csv_file(filename)
   except:
      print "Uso: python CsvReader.py archivo.csv"


