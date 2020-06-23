import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class filedialogdemo(QWidget):
   def __init__(self, parent = None):
      super(filedialogdemo, self).__init__(parent)
		
      layout = QVBoxLayout()
      self.bb = QPushButton("QFileDialog static method demo")
      self.bb.clicked.connect(self.getfile)
		
      layout.addWidget(self.bb)

      self.le = QLabel("Hello")	
      layout.addWidget(self.le)

		
      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.setLayout(layout)
      self.setWindowTitle("File Dialog demo")
		
   def getfile(self):
      fname = QFileDialog.getOpenFileName(self, 'Find file', 'd:/temp')
      self.contents.append(fname);

				
def main():
   app = QApplication(sys.argv)
   ex = filedialogdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()