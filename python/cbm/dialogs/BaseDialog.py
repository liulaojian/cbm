# -*- coding: utf-8 -*-

# from IconHelper import *
from PyQt4 import QtGui,QtCore,Qt

class BaseDialog(QtGui.QDialog):
	def __init__(self, parent=None):
		super(BaseDialog, self).__init__(parent)

	# 自定义ui风格(标题栏、窗体字体、背景透明、图标等)
	def initUi(self, ui):
		self.setStyleSheet(u"font: 12pt \"微软雅黑\";")
		self.setWindowFlags(Qt.Qt.WindowCloseButtonHint | Qt.Qt.WindowCloseButtonHint | Qt.Qt.FramelessWindowHint) 
		self.setWindowOpacity(1)
		self.mousePressed = False
		closePix = self.style().standardPixmap(Qt.QStyle.SP_TitleBarCloseButton)
		ui.btnMenu_Close.setIcon(Qt.QIcon(closePix))
		icoPix = QtGui.QPixmap(u":/images/cbm.ico")
		ui.lab_Ico.setPixmap(icoPix.scaled(Qt.QSize(31,33)))
		# icon1 = QtGui.QIcon()
		# icon1.addPixmap(QtGui.QPixmap(u":/images/close.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		# ui.btnMenu_Close.setIcon(icon1)
		# instance().setIcon(ui.btnMenu_Close, QtCore.QString(QtCore.QChar(0xf00d)), 12)
		# instance().setIcon(ui.btnMenu_Close, u'\uf00d', 12)
		ui.btnMenu_Close.clicked.connect(self.close)
		self.FormInCenter(self)

	# 设置标题
	def setTitle(self, title):
		if hasattr(self.ui, 'lab_Title'):
			self.ui.lab_Title.setText(title)

	#窗体居中显示
	def FormInCenter(self, frm):
		frmX = frm.width()
		frmY = frm.height()
		w = QtGui.QDesktopWidget()
		deskWidth = w.width()
		deskHeight = w.height()
		movePoint = QtCore.QPoint(deskWidth / 2 - frmX / 2, deskHeight / 2 - frmY / 2);
		frm.move(movePoint);

	def mousePressEvent(self,e):
		if e.button() == QtCore.Qt.LeftButton:
			self.mousePressed = True
			self.mousePoint = e.globalPos() - self.pos()
			e.accept()

	def mouseReleaseEvent(self,e):
		self.mousePressed = False

	def mouseMoveEvent(self,e):
		if self.mousePressed and e.buttons() and QtCore.Qt.LeftButton:
			self.move(e.globalPos()-self.mousePoint)
			e.accept()