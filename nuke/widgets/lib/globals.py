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
import base64

def aboutDialog(self, version, year, description):
    CUSTOM_VERSION = str(version)
    CUSTOM_YEAR = str(year)
    CUSTOM_DESCRIPTION = description

    self.about = QtWidgets.QDialog()
    self.about.setMinimumSize(700, 318)
    self.about.setMaximumSize(700, 318)
    self.about.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            
    #defines a function, 'closeAboutDialog,' that will close the 'self.about' widget when called
    def closeAboutDialog(*args, **kwargs):
        self.about.close()        
    #when the 'mousePressEvent' is triggered, call the function 'closeAboutDialog'
    self.about.mousePressEvent = closeAboutDialog
    
    #--- BEGIN IMAGE PREPARATION ---#
    #stores images as base64 encoded strings so that the images may be self contained within the script
    mfxLogo256w_encoded = "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"
    toolTitle256w_encoded = "iVBORw0KGgoAAAANSUhEUgAAAQkAAAAWCAYAAADTn2meAAAACXBIWXMAAAsSAAALEgHS3X78AAAE7UlEQVR4nO1crXfbMBC/fZBB00LTQg8OunAwhYMe3JgLC9s/ofkTEjoW07GaliV0bKZl2vPb3es9TbKlkxJn2/3e05vjWJf70unu5PWVMQYUCoXCh9eqGYVCMQUNEgqFYhIaJBQKxSTeAkADAJXjoQEA1gBwSFDhBuffCOZWyJsPPfI3hwIA7tgza5zru78ESssOPep/K9D/SGeF1+Pc+0gaxMdg2c3W1w0+M4UWZQPLXrasIXb0+Skhxn45fT6Xn4KlLxdCdA4OW0n5+Q1jTGGMac1vVMaYEkdjjPlpjKnH5qZgVDh/L5w/8rRBXirkr8XP9F0oLT6f36899085RnkeUd/0uyvUXSPQ2Q5pEp1H9jlkcH+w9VJa9OdGgc/v8ZqeH68fUL5CwBf30wp9IcYffLTuUO/VQn5a4PN7xlOJfrqP9NMS5zw46MTwBHTRoHC28VtUWqgh7bmPHrohY8OMVSIdvmh2kQqz50/dP+V4REO69Oe67xsU8OygvonUFfnD3mP7WFo+H9oJ/MrnpxJ6Plr7SBlz+imgzV0baxm7uFmQsO3h8hPvmOtJDJi6TKV5PlQsrZHM72fSx7iU6TzRWnpKka/FNLmz7o+fa4ENeGmQAirtakaDUuqQ1DkU15nodTMpv41T+elo288Z6Gzx32AZQxuXEuWXrL6TBIn7me+3M9//DahRPy4nGyKcggK5HSCA3asd302BeiIt0peC+ivcKWsPrxKskL9cAaeK7Emcwk8pUOeQkdZisIxzQaIKiJS+ecREJ3DQ/wVlpmZpEbCQY3ZHAi2AlGxiQBm5D/gCmgSrxCDGUaOezm0DWgU8E0Orj9H/W+tzgUoqkFgtTHFq5vz9EaK9FCthVnMMlDhyLRbw7A6HhBOqA8smJCcthI5lJAPbfKR4YPNq4ekZocV/KdDenEEpO/Kxs/iSomL6KtGG1zG07CDBd4zRiO+FC7tiu1DHatKlI3Rn8VBkqLn/ddxjcG0TauKelURD4rE6IB9EY5NIa80W5fWZZBGjjq7wukiUsUcb3iGtaBvaQSL2TN0FcgZ+Tku7x9IGsB1UkoLn5GXImCqDR54yUU5616INqL996JkPQObsqUvMUAeWfjdnWGoMGfR1wGC4k/SDjvHGJaWSV2xoX+JPDNbCcSE0gAwBCyUl+FP63c485wPvS+Su+deZytgt2mLJjcMHaXDm6FjpH4VjBgmOnvU6FC/YTtSchVV7T4F2G1fA4W82SjGwskNqw44twmP0pqrEfhMFrpxNwtxoEtfQVmLDYwQJVzrjOitXvDimqy/SRjbQ7nEB2guF7JGashIvUiclHzjWq+/SLIdAr2SnHvkeC3SYkBJgRe++UJDIpRTenOKgVHfpIGHLubQz9Kzeb1j/4E5Qi3JaJBed5sQ2q1x6GRLT3j5Dfe3ii/SVemICrMm+ZDbhkpFOKFL7hYOk5Hhze3s7LtxLAHgCgAsA+JEQrW5RkEvLGRom4HOksDUKNfL3TvhuQWP95gHpfGJ0Dwsd0X7H3x55+QIAH9mCl9Aq0A6f8Pqr4D94XTBn5XOf2O/E4hmf/8auY2D76QccH9F+2wi/oDdQn5DmgTW1n5G+LXsIzRx+WrA1RDLWyNca12cIWubPF4wX0t9lqB31L1MpFIpJ6N+TUCgUk9AgoVAoJqFBQqFQ+AEAvwDkKpNN+CldLQAAAABJRU5ErkJggg=="
    #'base64.decodestring()' is a method used to decode a base64 encoded string
    mfxLogo_decoded = base64.decodestring(mfxLogo256w_encoded)
    toolTitle_decoded = base64.decodestring(toolTitle256w_encoded)
    #'QtGui.QPixmap()' is an object for containing image representations
    pixMap_logo = QtGui.QPixmap()
    pixMap_title = QtGui.QPixmap()
    #'loadFromData' is a function within the 'QtGui.QPixmap' object that loads an image that was encoded as a base64 string
    pixMap_logo.loadFromData(mfxLogo_decoded)
    pixMap_title.loadFromData(toolTitle_decoded)
    #--- END IMAGE PREPARATION ---#
    
    #creates a 'QtWidgets.QLabel' object and assigns a given 'QtGui.QPixmap()' object to it using the 'QtGui.setPixmap()' method
    img_mfxLogo = QtWidgets.QLabel()
    img_toolTitle = QtWidgets.QLabel()
    img_mfxLogo.setPixmap(pixMap_logo)
    img_toolTitle.setPixmap(pixMap_title)
    
    #creates a 'QtWidgets.QLabel()' object that stores this tool's version number and calendar year
    txt_versionNum = QtWidgets.QLabel()
    txt_versionNum.setText('Version ' + CUSTOM_VERSION + ' (' + CUSTOM_YEAR + ')')
    
    #creates a 'QtWidgets.QPlainTextEdit' object and sets it's 'readOnly()' method to 'true' for displaying typical disclaimer text
    txt_disclaimer = QtWidgets.QPlainTextEdit(CUSTOM_DESCRIPTION)
    txt_disclaimer.setReadOnly(1)

    #creates 'QtWidgets.QLabel()' objects and arranges them into a 'QtWidgets.QHBoxLayout()' object for simplfied grouping
    txt_email = QtWidgets.QLabel()
    txt_email.setText('Eric@MercadoFX.com')
    txt_phone = QtWidgets.QLabel()
    txt_phone.setText('(816) 786-4189')
    contactLayout = QtWidgets.QVBoxLayout()
    contactLayout.addWidget(txt_email)
    contactLayout.addWidget(txt_phone)
    
    leftSide = QtWidgets.QVBoxLayout()
    leftSide.addWidget(img_mfxLogo)
    rightSide = QtWidgets.QVBoxLayout()
    rightSide.addWidget(img_toolTitle)
    rightSide.addWidget(txt_versionNum)
    rightSide.addWidget(txt_disclaimer)
    rightSide.addLayout(contactLayout)
    
    #----------------------------------------------------------------------#
    #--- BEGIN STYLING for 'self.about', a 'QtWidgets.QDialog()' object ---#
    #----------------------------------------------------------------------#
    #initializes the 'pixMap_BG' object that will serve has a containing widget for the generated 'painter' background
    pixMap_BG = QtGui.QPixmap(700, 318)
    pixMap_BG.fill(QtGui.QColor(0, 0, 0, 255))

    #creates the 'QtGui.QPainter()' object, and begins the painting operations
    BG_painter = QtGui.QPainter(self.about)
    BG_painter.begin(pixMap_BG)

    #initializes a 'QtCore.QRectF()' object that will serve has the basic shape for the background.  In this case, it should be the same size as the 'QtWidgets.Dialog()' object
    rectangle = QtCore.QRectF(0, 0, 700, 318)

    #--- BEGIN LAYER 01 ---#
    solid_brush = QtGui.QBrush(QtGui.QColor(36, 36, 36, 255), QtCore.Qt.SolidPattern)
    BG_painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceOver)        
    BG_painter.setBrush(solid_brush)
    BG_painter.drawRect(rectangle)
    #---- END LAYER 01 ----#
    #--- BEGIN LAYER 02 ---#
    stripes_brush = QtGui.QBrush(QtGui.QColor(50, 50, 50, 255), QtCore.Qt.BDiagPattern)
    BG_painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceOver) 
    BG_painter.setBrush(stripes_brush)
    BG_painter.drawRect(rectangle)
    #---- END LAYER 02 ----#
    #--- BEGIN LAYER 03 ---#
    gradient_style = QtGui.QLinearGradient(0, 0, 0, rectangle.height()) #QtGui.QLinearGradient(startX, startY, endX, endY)
    gradient_style.setColorAt(0.80, QtGui.QColor(255, 255, 255, 255)) #QtGui.QLinearGradient().setColorAt(positionFloat, color)
    gradient_style.setColorAt(1.00, QtGui.QColor(128, 128, 128, 255)) #QtGui.QLinearGradient().setColorAt(positionFloat, color)
    BG_painter.setCompositionMode(QtGui.QPainter.CompositionMode_Multiply)
    gradient_brush = QtGui.QBrush(gradient_style)
    BG_painter.setBrush(gradient_brush)
    BG_painter.drawRect(rectangle)
    #---- END LAYER 03 ----#

    #'BG_painter.end()' ends the painting instance
    BG_painter.end()

    #converts the 'QtGui.QPixMap()' object into a 'QtGui.QImage' object
    BG_converted = pixMap_BG.toImage()
    #creates a 'QtGui.QBrush()' object that uses 'BG_converted' as a 'QtCore.Qt.TexturePattern'
    palette_brush = QtGui.QBrush(QtCore.Qt.TexturePattern)
    palette_brush.setTextureImage(BG_converted)
    #creates a new 'QtGui.QPalette()' object, with the previously created 'palette_brush' object to fill the 'QtGui.QPalette.Background' color role
    dialogPalette = QtGui.QPalette()
    dialogPalette.setBrush(QtGui.QPalette.Background, palette_brush)
    #applies the newly created 'dialogPalette' to the 'self.about' dialog object 
    self.about.setPalette(dialogPalette)
    #----------------------------------------------------------------------#
    #---- END STYLING for 'self.about', a 'QtWidgets.QDialog()' object ----#
    #----------------------------------------------------------------------#

    dialogLayout_about = QtWidgets.QHBoxLayout()
    dialogLayout_about.addLayout(leftSide)
    dialogLayout_about.addLayout(rightSide)

    self.about.setLayout(dialogLayout_about)
    self.about.exec_()