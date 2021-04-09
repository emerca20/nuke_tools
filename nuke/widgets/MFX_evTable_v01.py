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
		t = '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'
		
		globals.aboutDialog(self, version=v, year=y, description=d, title=t)
	
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