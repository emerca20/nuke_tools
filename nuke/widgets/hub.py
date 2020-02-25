#--------------------------------------------------------------------#
#---- imports the correct PyQt modules dependent on Nuke version ----#
try:
	#nuke < v11.0 expects PySide <= v1.2.2
	from PySide import QtGui as QtWidgets
	from PySide import QtGui
	from PySide import QtCore
except:
	#nuke > v12.0 expects Pyside >= v2.0
	from PySide2 import QtWidgets
	from PySide2 import QtCore
#--------------------------------------------------------------------#

#creates a child class, that inherits the functionality of parent class 'QtWidgets.QMainWindow'
class nukeTestWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
    	super(nukeTestWindow, self).__init__(parent)
    	self.setObjectName('myhub')
    	self.setWindowTitle('myHUB')
    	self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    	self.generate_ui()

	def generate_ui(self):
    	#--------------------------------------------------------
    	#---- menuBar
    	self.aboutAction = QtWidgets.QAction(u'About', QtCore.QObject(parent=self))
    	self.helpMenu = QtWidgets.QMenu('Help')
    	self.helpMenu.addAction(self.aboutAction)
    	self.menuBar = QtWidgets.QMenuBar()
    	self.menuBar.addMenu(self.helpMenu)
    	self.setMenuBar(self.menuBar)

    	#--------------------------------------------------------
    	#---- toolBar
    	self.tools = QtWidgets.QToolBar('tools')
    	self.tools.setMovable(False)

    	self.advMerge = QtWidgets.QAction(u'Advanced Merge', QtCore.QObject(parent=self))
    	self.addKey = QtWidgets.QAction(u'Additive Keyer', QtCore.QObject(parent=self))
    	self.addInvert = QtWidgets.QAction(u'Additive Inverse', QtCore.QObject(parent=self))
    	self.chromaBlur = QtWidgets.QAction(u'Chroma Blur', QtCore.QObject(parent=self))
    	self.colorDilate = QtWidgets.QAction(u'Color Dilate', QtCore.QObject(parent=self))
    	self.contrast = QtWidgets.QAction(u'Contrast', QtCore.QObject(parent=self))
    	self.ioGraph = QtWidgets.QAction(u"I/O Graph", QtCore.QObject(parent=self))
    	self.lift = QtWidgets.QAction(u'Lift', QtCore.QObject(parent=self))
    	self.multKey = QtWidgets.QAction(u'Multiplicative Keyer', QtCore.QObject(parent=self))
    	self.multInvert = QtWidgets.QAction(u'Multiplicative Inverse', QtCore.QObject(parent=self))
    	self.saturate = QtWidgets.QAction(u'Saturation', QtCore.QObject(parent=self))
    	self.saturate.setIcon(QtGui.QPixmap(":qrc/images/ToolbarImage.png"))
    	self.toe = QtWidgets.QAction(u'Toe', QtCore.QObject(parent=self))

    	self.imageBtn = QtWidgets.QToolButton(parent=self)
    	self.imageBtn.setToolTip('Image')
    	#self.imageBtn.setPopupMode(QtWidgets.QToolButton.InstantPopup)
    	self.imageBtn.setIcon(QtGui.QPixmap(":qrc/images/ToolbarImage.png"))
    	self.imageMenu = QtWidgets.QMenu()
    	self.imageBtn.setMenu(self.imageMenu)

    	self.colorBtn = QtWidgets.QToolButton(parent=self)
    	self.colorBtn.setToolTip('Color')
    	self.colorBtn.setPopupMode(QtWidgets.QToolButton.InstantPopup)
    	self.colorBtn.setIcon(QtGui.QPixmap(":qrc/images/ToolbarColor.png"))
    	self.colorMenu = QtWidgets.QMenu()
    	self.mathMenu = QtWidgets.QMenu('Math')
    	self.mathMenu.addAction(self.addInvert)
    	self.mathMenu.addAction(self.ioGraph)
    	self.mathMenu.addAction(self.multInvert)
    	self.colorMenu.addMenu(self.mathMenu)
    	self.colorMenu.addAction(self.contrast)
    	self.colorMenu.addAction(self.lift)
    	self.colorMenu.addAction(self.saturate)
    	self.colorMenu.addAction(self.toe)
    	self.colorBtn.setMenu(self.colorMenu)
  	 
    	self.filterBtn = QtWidgets.QToolButton(parent=self)
    	self.filterBtn.setToolTip('Filter')
    	self.filterBtn.setPopupMode(QtWidgets.QToolButton.InstantPopup)
    	self.filterBtn.setIcon(QtGui.QPixmap(":qrc/images/ToolbarFilter.png"))
    	self.filterMenu = QtWidgets.QMenu()
    	self.filterMenu.addAction(self.chromaBlur)
    	self.filterMenu.addAction(self.colorDilate)
    	self.filterBtn.setMenu(self.filterMenu)

    	self.keyerBtn = QtWidgets.QToolButton(parent=self)
    	self.keyerBtn.setToolTip('Keyer')
    	self.keyerBtn.setPopupMode(QtWidgets.QToolButton.InstantPopup)
    	self.keyerBtn.setIcon(QtGui.QPixmap(":qrc/images/ToolbarKeyer.png"))
    	self.keyerMenu = QtWidgets.QMenu()
    	self.keyerMenu.addAction(self.addKey)
    	self.keyerMenu.addAction(self.multKey)
    	self.keyerBtn.setMenu(self.keyerMenu)

    	self.mergeBtn = QtWidgets.QToolButton(parent=self)
    	self.mergeBtn.setToolTip('Merge')
    	self.mergeBtn.setPopupMode(QtWidgets.QToolButton.InstantPopup)
    	self.mergeBtn.setIcon(QtGui.QPixmap(":qrc/images/ToolbarMerge.png"))
    	self.mergeMenu = QtWidgets.QMenu()
    	self.mergeMenu.addAction(self.advMerge)
    	self.mergeBtn.setMenu(self.mergeMenu)

    	self.tools.addWidget(self.imageBtn)
    	self.tools.addWidget(self.colorBtn)
    	self.tools.addWidget(self.filterBtn)
    	self.tools.addWidget(self.keyerBtn)
    	self.tools.addWidget(self.mergeBtn)
    	self.addToolBar(QtCore.Qt.ToolBarArea.LeftToolBarArea, self.tools)

    	#--------------------------------------------------------
    	#---- statusBar
    	self.statusBar = QtWidgets.QStatusBar()
    	self.statusBar.showMessage('This is a test message!')
    	self.setStatusBar(self.statusBar)

    	#--------------------------------------------------------
    	#---- centralWidget
    	self.centralWidget = QtWidgets.QWidget()
    	#self.centralWidget.setBackgroundRole()
    	self.centralLayout = QtWidgets.QVBoxLayout()

    	self.b1=QtWidgets.QPushButton("hello world!")
    	self.b2=QtWidgets.QPushButton("hello another world!")
    	self.centralLayout.addWidget(self.b1)
    	self.centralLayout.addWidget(self.b2)
  	 
    	self.centralWidget.setLayout(self.centralLayout)
    	self.setCentralWidget(self.centralWidget)

thisInstance = nukeTestWindow()
thisInstance.show()
