# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles\high_drilling_pore_dlg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_high_drilling_pore_dlg(object):
    def setupUi(self, high_drilling_pore_dlg):
        high_drilling_pore_dlg.setObjectName(_fromUtf8("high_drilling_pore_dlg"))
        high_drilling_pore_dlg.resize(411, 441)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/cbm.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        high_drilling_pore_dlg.setWindowIcon(icon)
        self.widget_main = QtGui.QWidget(high_drilling_pore_dlg)
        self.widget_main.setGeometry(QtCore.QRect(0, 30, 411, 411))
        self.widget_main.setObjectName(_fromUtf8("widget_main"))
        self.beta = QtGui.QLineEdit(self.widget_main)
        self.beta.setGeometry(QtCore.QRect(300, 320, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.beta.setFont(font)
        self.beta.setObjectName(_fromUtf8("beta"))
        self.label_13 = QtGui.QLabel(self.widget_main)
        self.label_13.setGeometry(QtCore.QRect(20, 140, 421, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.n2 = QtGui.QLineEdit(self.widget_main)
        self.n2.setGeometry(QtCore.QRect(200, 100, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n2.setFont(font)
        self.n2.setObjectName(_fromUtf8("n2"))
        self.label_14 = QtGui.QLabel(self.widget_main)
        self.label_14.setGeometry(QtCore.QRect(20, 210, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lw = QtGui.QLineEdit(self.widget_main)
        self.lw.setGeometry(QtCore.QRect(200, 20, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lw.setFont(font)
        self.lw.setObjectName(_fromUtf8("lw"))
        self.save = QtGui.QPushButton(self.widget_main)
        self.save.setGeometry(QtCore.QRect(210, 360, 90, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save.setFont(font)
        self.save.setObjectName(_fromUtf8("save"))
        self.cacl = QtGui.QPushButton(self.widget_main)
        self.cacl.setGeometry(QtCore.QRect(100, 360, 90, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cacl.setFont(font)
        self.cacl.setObjectName(_fromUtf8("cacl"))
        self.label_11 = QtGui.QLabel(self.widget_main)
        self.label_11.setGeometry(QtCore.QRect(20, 60, 181, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_15 = QtGui.QLabel(self.widget_main)
        self.label_15.setGeometry(QtCore.QRect(20, 280, 281, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_12 = QtGui.QLabel(self.widget_main)
        self.label_12.setGeometry(QtCore.QRect(20, 100, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_18 = QtGui.QLabel(self.widget_main)
        self.label_18.setGeometry(QtCore.QRect(90, 240, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_10 = QtGui.QLabel(self.widget_main)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.ld = QtGui.QLineEdit(self.widget_main)
        self.ld.setGeometry(QtCore.QRect(20, 240, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ld.setFont(font)
        self.ld.setObjectName(_fromUtf8("ld"))
        self.label_16 = QtGui.QLabel(self.widget_main)
        self.label_16.setGeometry(QtCore.QRect(20, 320, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.lc = QtGui.QLineEdit(self.widget_main)
        self.lc.setGeometry(QtCore.QRect(20, 170, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lc.setFont(font)
        self.lc.setObjectName(_fromUtf8("lc"))
        self.label_17 = QtGui.QLabel(self.widget_main)
        self.label_17.setGeometry(QtCore.QRect(90, 170, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.lk = QtGui.QLineEdit(self.widget_main)
        self.lk.setGeometry(QtCore.QRect(300, 280, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lk.setFont(font)
        self.lk.setObjectName(_fromUtf8("lk"))
        self.n1 = QtGui.QLineEdit(self.widget_main)
        self.n1.setGeometry(QtCore.QRect(200, 60, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n1.setFont(font)
        self.n1.setObjectName(_fromUtf8("n1"))
        self.label = QtGui.QLabel(self.widget_main)
        self.label.setGeometry(QtCore.QRect(370, 320, 31, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.widget_title = QtGui.QWidget(high_drilling_pore_dlg)
        self.widget_title.setGeometry(QtCore.QRect(0, 0, 411, 31))
        self.widget_title.setObjectName(_fromUtf8("widget_title"))
        self.lab_Ico = QtGui.QLabel(self.widget_title)
        self.lab_Ico.setGeometry(QtCore.QRect(0, 0, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_Ico.sizePolicy().hasHeightForWidth())
        self.lab_Ico.setSizePolicy(sizePolicy)
        self.lab_Ico.setMinimumSize(QtCore.QSize(30, 0))
        self.lab_Ico.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_Ico.setObjectName(_fromUtf8("lab_Ico"))
        self.lab_Title = QtGui.QLabel(self.widget_title)
        self.lab_Title.setGeometry(QtCore.QRect(30, 0, 331, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_Title.sizePolicy().hasHeightForWidth())
        self.lab_Title.setSizePolicy(sizePolicy)
        self.lab_Title.setStyleSheet(_fromUtf8("font: 10pt \"微软雅黑\";"))
        self.lab_Title.setText(_fromUtf8(""))
        self.lab_Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_Title.setObjectName(_fromUtf8("lab_Title"))
        self.btnMenu_Close = QtGui.QPushButton(self.widget_title)
        self.btnMenu_Close.setGeometry(QtCore.QRect(370, 0, 41, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMenu_Close.sizePolicy().hasHeightForWidth())
        self.btnMenu_Close.setSizePolicy(sizePolicy)
        self.btnMenu_Close.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnMenu_Close.setFont(font)
        self.btnMenu_Close.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnMenu_Close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMenu_Close.setText(_fromUtf8(""))
        self.btnMenu_Close.setIconSize(QtCore.QSize(32, 32))
        self.btnMenu_Close.setFlat(True)
        self.btnMenu_Close.setObjectName(_fromUtf8("btnMenu_Close"))

        self.retranslateUi(high_drilling_pore_dlg)
        QtCore.QMetaObject.connectSlotsByName(high_drilling_pore_dlg)

    def retranslateUi(self, high_drilling_pore_dlg):
        high_drilling_pore_dlg.setWindowTitle(_translate("high_drilling_pore_dlg", "高位抽采钻孔有效布设范围计算", None))
        self.label_13.setText(_translate("high_drilling_pore_dlg", "重叠区长度,即钻孔沿工作面推进方向上的搭接长度Lc", None))
        self.label_14.setText(_translate("high_drilling_pore_dlg", "钻孔沿工作面方向水平投影长度Ld", None))
        self.save.setText(_translate("high_drilling_pore_dlg", "保 存", None))
        self.cacl.setText(_translate("high_drilling_pore_dlg", "计 算", None))
        self.label_11.setText(_translate("high_drilling_pore_dlg", "ABC 范围内钻孔总数n1", None))
        self.label_15.setText(_translate("high_drilling_pore_dlg", "钻孔沿工作面推进方向的控制范围Lk", None))
        self.label_12.setText(_translate("high_drilling_pore_dlg", "BCD 范围内钻孔总数n2", None))
        self.label_18.setText(_translate("high_drilling_pore_dlg", "(注：Ld=(2/3~3/4)L)", None))
        self.label_10.setText(_translate("high_drilling_pore_dlg", "工作面水平投影长度L", None))
        self.label_16.setText(_translate("high_drilling_pore_dlg", "ABCD 范围内抽放钻孔的范围控制角β", None))
        self.label_17.setText(_translate("high_drilling_pore_dlg", "(注：依据生产实际Lc不小于20m)", None))
        self.label.setText(_translate("high_drilling_pore_dlg", "(°)", None))
        self.lab_Ico.setText(_translate("high_drilling_pore_dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

import usecad_rc
