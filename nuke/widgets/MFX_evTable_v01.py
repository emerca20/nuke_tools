try:
	#nuke < v11.0 expects PySide <= v1.2.2
	import PySide.QtCore as QtCore
	import PySide.QtGui as QtGui
	import PySide.QtGui as QtWidgets
except:
	#nuke < v11.0 expects Pyside >= v2.0
	import PySide2.QtWidgets as QtWidgets
	import PySide2.QtCore as QtCore
	import PySide2.QtGui as QtGui
from .lib import globals
import nuke
import __future__
import math

class exposureWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None, GRADE=None):
		super(exposureWindow, self).__init__(parent)
		self.GRADE = GRADE

		self.ISO = ['100', '200', '400', '800', '1600', '3200', '6400', '12800', '25600']
		self.SSPEED = ['15', '8', '4', '2', '1', '1/2', '1/4', '1/8', '1/15', '1/30', '1/60', '1/125', '1/250', '1/500', '1/1000', '1/2000', '1/4000', '1/8000']
		self.FSTOP = ['1', '1.4', '2', '2.8', '4', '5.6', '8', '11', '16', '22', '32', '45', '64']

		try:
			self.italicFont = QtGui.QApplication.font()
		except:
			self.italicFont = QtGui.QGuiApplication.font()
		self.italicFont.setItalic(True)

		self.setObjectName('mfx_ev')
		if self.GRADE is not None:
        		self.setWindowTitle('MFX Exposure Value(EV) [' + self.GRADE.name() + ']')
		else:
			self.setWindowTitle('MFX Exposure Value(EV)')
		self.resize(493, 488)
		self.setWindowFlags(QtCore.Qt.Tool)

		MFX_MENU = QtWidgets.QMainWindow.menuBar(self)
		helpMenu = QtWidgets.QMenu('Help')
		aboutAction = QtWidgets.QAction('About', helpMenu)
		self.connect(aboutAction, QtCore.SIGNAL('triggered()'), self.showAboutDialog)
		helpMenu.addAction(aboutAction)
		MFX_MENU.addMenu(helpMenu)

		self.coreWidget = QtWidgets.QWidget()
		self.MFX_LAYOUT = QtWidgets.QVBoxLayout(self.coreWidget)
		self.setCentralWidget(self.coreWidget)
        	
		self.generate_ui()
		
	def showAboutDialog(self):
		v = 1.0
		y = 2020
		d = 'This is a free tool for conveniently adjusting brightness based on an Exposure Value (EV) scale, and was made by Eric A. Mercado.\n\nThis tool was written using Python 3.8.5, and Qt for Python (PySide), as to align with the software trends described by www.vfxplatform.com/.\n\nPlease feel free to contact me with any issues, comments, or concerns and I will address them as soon as I can.\n\nThank you.'
		globals.aboutDialog(self, version=v, year=y, description=d)
	
	def generate_ui(self):
		self.evTable = QtWidgets.QTableWidget()
		self.evTable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
		self.evTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
		self.evTable.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignRight)
		self.evTable.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
		self.evTable.verticalHeader().setToolTip('shutter speed')
		self.evTable.horizontalHeader().setToolTip('f number')
		self.evTable.setColumnCount(13)
		self.evTable.setRowCount(18)
		self.evTable.setVerticalHeaderLabels(self.SSPEED)
		self.evTable.setHorizontalHeaderLabels(self.FSTOP)
		self.evTable.itemSelectionChanged.connect(self.__changeSelection)

		isoLabel = QtWidgets.QLabel()
		isoLabel.setText('ISO =')
		isoLabel.setMaximumWidth(33)
		self.isoField = QtWidgets.QComboBox()
		self.isoField.setToolTip('iso')
		self.isoField.addItems(self.ISO)
		self.connect(self.isoField, QtCore.SIGNAL('currentIndexChanged(int)'), self.update_tableWidget)
		isoLayout = QtWidgets.QHBoxLayout()
		isoLayout.addWidget(isoLabel)
		isoLayout.addWidget(self.isoField)
		self.MFX_LAYOUT.addLayout(isoLayout)
		
		if self.GRADE is not None:
			iso = self.GRADE.knob('iso').value()
		else:
			iso = float(100)
		self.create_tableWidget(iso=iso)
		
		self.MFX_LAYOUT.addWidget(self.evTable)
		
		footerLabel = QtWidgets.QLabel()
		footerLabel.setFont(self.italicFont)
		footerLabel.setAlignment(QtCore.Qt.AlignRight)
		if self.GRADE is not None:
			footerLabel.setStyleSheet('QLabel { color : #A9FFFF }')
			footerLabel.setText(self.GRADE.name())
		else:
			footerLabel.setStyleSheet('QLabel { color : #FF0000; }')
			footerLabel.setText('Not linked with any existing Grade nodes.')
		self.MFX_LAYOUT.addWidget(footerLabel)

	def update_tableWidget(self):
		self.create_tableWidget(int(self.isoField.currentText()))
	
	def create_tableWidget(self, iso):
		for row in range(0, self.evTable.rowCount(), 1):
			ss = eval(compile(self.evTable.verticalHeaderItem(row).text(), '<string>', 'eval', __future__.division.compiler_flag))
			for col in range(0, self.evTable.columnCount(), 1):
				f = float(self.evTable.horizontalHeaderItem(col).text())
				ev = int(round(math.log(pow(f, 2)/ss, 2)) - math.log(iso/100, 2))
				currentCell = QtWidgets.QTableWidgetItem()
				currentCell.setTextAlignment(QtCore.Qt.AlignCenter)
				currentCell.setText(str(ev))
				self.evTable.setItem(row, col, currentCell)
				if ev < 0:
					self.evTable.item(row, col).setBackground(QtGui.QBrush(QtGui.QColor(int(207*0.5), int(226*0.5), int(243*0.5), 255), QtCore.Qt.SolidPattern))
				if ev == 0:
					self.evTable.item(row, col).setBackground(QtGui.QBrush(QtGui.QColor(int(183*0.5), int(225*0.5), int(205*0.5), 255), QtCore.Qt.SolidPattern))
				if ev > 0:
					self.evTable.item(row, col).setBackground(QtGui.QBrush(QtGui.QColor(int(252*0.5), int(229*0.5), int(205*0.5), 255), QtCore.Qt.SolidPattern))
		
		self.__changeSelection()

	def __changeSelection(self):
		if self.GRADE is not None:
			#mult = self.GRADE.knob('multiply').value()
			#ev = int(round(math.log(mult, 2), 0))
			#for row in range(0, self.evTable.rowCount(), 1):
			#	if int(self.evTable.item(row, 0).text()) == ev:
			#		self.evTable.item(row, 0).setSelected(1)
			cur = self.evTable.selectedItems()
			if len(cur) == 1:
				iso = int(self.isoField.currentText())
				self.GRADE.knob('iso').setValue(iso)
				
				f = self.evTable.horizontalHeaderItem(self.evTable.column(cur[0])).text()
				self.GRADE.knob('f').setTooltip('f/' + f)
				f = float(f)
				self.GRADE.knob('f').setValue(f)
				
				ss = self.evTable.verticalHeaderItem(self.evTable.row(cur[0])).text()
				self.GRADE.knob('ss').setTooltip(ss)
				ss = eval(compile(ss, '<string>', 'eval', __future__.division.compiler_flag))
				self.GRADE.knob('ss').setValue(ss)

				self.GRADE.knob('multiply').setValue(pow(2, int(cur[0].text()) * -1))

def getNukeMainWindow():
    #-----Referenced codeblock found at: http://community.foundry.com/discuss/topic/107662-----#
    #-Credit for this codeblock should go the Foundry Community forums member, Fredrik Averpil-#
    """Returns Nuke's main window"""
    for obj in QtWidgets.QApplication.instance().topLevelWidgets():
    	if (obj.inherits('QMainWindow') and obj.metaObject().className() == 'Foundry::UI::DockMainWindow'):
        	return obj
    else:
    	raise RuntimeError('Could not find DockMainWindow instance')
    #-------------------------------- End referenced codeblock --------------------------------#

thisInstance = None
def create_window(GRADE=None):
    global thisInstance
    if thisInstance is not None:
        thisInstance.deleteLater()
        thisInstance = None
    if thisInstance is None:
        thisInstance = exposureWindow(parent=getNukeMainWindow(), GRADE=GRADE)
    thisInstance.show()
    thisInstance.raise_()
    thisInstance.activateWindow()