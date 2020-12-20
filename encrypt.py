import random
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from encrypt_window import Ui_MainWindow


class window(QMainWindow):
	def __init__(self,parent=None):
		super(window,self).__init__(parent=None)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.lineEdit.setMaxLength(50)
		self.ui.pushButton.clicked.connect(self.encrypt)

	def encrypt(self):
		st = self.ui.lineEdit.text()
		n1 = self.ui.spinBox.text()
		n1 = int(n1)
		n2 = self.ui.spinBox_2.text()
		n2 = int(n2)
		n3 = self.ui.spinBox_3.text()
		n3 = int(n3)
		n4 = self.ui.spinBox_4.text()
		n4 = int(n4)

		key = []
		key.extend([n1,n2,n3,n4])

		count = 0

		encr = ""
		encrlist = []

		ordlist = []

		for x in st:
			ordlist.append(ord(x))

		for m in ordlist:
			if count%2==0:
				m = m+key[3]+key[2]-key[1]+key[0]
			else:
				m = m-key[3]-key[2]+key[1]+key[0]
			encrlist.append(m)
			count+=1

		for x in encrlist:
			encr = encr+chr(x)

		file = open("key_code.txt",'w')
		file.write("")
		file.close()

		self.ui.lineEdit_2.setText(encr)

def main():
	app = QApplication(sys.argv)
	ex = window()
	ex.show()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()