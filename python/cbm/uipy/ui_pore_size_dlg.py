# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles\pore_size_dlg.ui'
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

class Ui_pore_size_dlg(object):
    def setupUi(self, pore_size_dlg):
        pore_size_dlg.setObjectName(_fromUtf8("pore_size_dlg"))
        pore_size_dlg.resize(390, 350)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/cbm.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pore_size_dlg.setWindowIcon(icon)
        self.widget_main = QtGui.QWidget(pore_size_dlg)
        self.widget_main.setGeometry(QtCore.QRect(0, 30, 391, 321))
        self.widget_main.setObjectName(_fromUtf8("widget_main"))
        self.groupBox = QtGui.QGroupBox(self.widget_main)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 351, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.hint = QtGui.QPushButton(self.groupBox)
        self.hint.setGeometry(QtCore.QRect(270, 30, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hint.setFont(font)
        self.hint.setObjectName(_fromUtf8("hint"))
        self.sigma = QtGui.QLineEdit(self.groupBox)
        self.sigma.setGeometry(QtCore.QRect(110, 120, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sigma.setFont(font)
        self.sigma.setObjectName(_fromUtf8("sigma"))
        self.mineName_label_11 = QtGui.QLabel(self.groupBox)
        self.mineName_label_11.setGeometry(QtCore.QRect(20, 90, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label_11.setFont(font)
        self.mineName_label_11.setObjectName(_fromUtf8("mineName_label_11"))
        self.mineName_label_12 = QtGui.QLabel(self.groupBox)
        self.mineName_label_12.setGeometry(QtCore.QRect(20, 30, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label_12.setFont(font)
        self.mineName_label_12.setObjectName(_fromUtf8("mineName_label_12"))
        self.mineName_label_10 = QtGui.QLabel(self.groupBox)
        self.mineName_label_10.setGeometry(QtCore.QRect(20, 120, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label_10.setFont(font)
        self.mineName_label_10.setObjectName(_fromUtf8("mineName_label_10"))
        self.mineName_label_13 = QtGui.QLabel(self.groupBox)
        self.mineName_label_13.setGeometry(QtCore.QRect(20, 60, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label_13.setFont(font)
        self.mineName_label_13.setObjectName(_fromUtf8("mineName_label_13"))
        self.mineName_label_9 = QtGui.QLabel(self.groupBox)
        self.mineName_label_9.setGeometry(QtCore.QRect(180, 60, 151, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label_9.setFont(font)
        self.mineName_label_9.setObjectName(_fromUtf8("mineName_label_9"))
        self.p = QtGui.QLineEdit(self.groupBox)
        self.p.setGeometry(QtCore.QRect(170, 90, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p.setFont(font)
        self.p.setObjectName(_fromUtf8("p"))
        self.q = QtGui.QLineEdit(self.groupBox)
        self.q.setGeometry(QtCore.QRect(190, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.q.setFont(font)
        self.q.setObjectName(_fromUtf8("q"))
        self.v = QtGui.QLineEdit(self.groupBox)
        self.v.setGeometry(QtCore.QRect(110, 60, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.v.setFont(font)
        self.v.setObjectName(_fromUtf8("v"))
        self.hint2 = QtGui.QPushButton(self.groupBox)
        self.hint2.setGeometry(QtCore.QRect(190, 120, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hint2.setFont(font)
        self.hint2.setObjectName(_fromUtf8("hint2"))
        self.cacl = QtGui.QPushButton(self.widget_main)
        self.cacl.setGeometry(QtCore.QRect(120, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cacl.setFont(font)
        self.cacl.setObjectName(_fromUtf8("cacl"))
        self.groupBox_2 = QtGui.QGroupBox(self.widget_main)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 190, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.d = QtGui.QLineEdit(self.groupBox_2)
        self.d.setGeometry(QtCore.QRect(110, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.d.setFont(font)
        self.d.setObjectName(_fromUtf8("d"))
        self.mineName_label_8 = QtGui.QLabel(self.groupBox_2)
        self.mineName_label_8.setGeometry(QtCore.QRect(20, 30, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label_8.setFont(font)
        self.mineName_label_8.setObjectName(_fromUtf8("mineName_label_8"))
        self.delta = QtGui.QLineEdit(self.groupBox_2)
        self.delta.setGeometry(QtCore.QRect(280, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delta.setFont(font)
        self.delta.setObjectName(_fromUtf8("delta"))
        self.mineName_label_7 = QtGui.QLabel(self.groupBox_2)
        self.mineName_label_7.setGeometry(QtCore.QRect(190, 30, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label_7.setFont(font)
        self.mineName_label_7.setObjectName(_fromUtf8("mineName_label_7"))
        self.save = QtGui.QPushButton(self.widget_main)
        self.save.setGeometry(QtCore.QRect(210, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save.setFont(font)
        self.save.setObjectName(_fromUtf8("save"))
        self.widget_title = QtGui.QWidget(pore_size_dlg)
        self.widget_title.setGeometry(QtCore.QRect(0, 0, 391, 31))
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
        self.lab_Title.setGeometry(QtCore.QRect(40, 0, 301, 31))
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
        self.btnMenu_Close.setGeometry(QtCore.QRect(350, 0, 41, 31))
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

        self.retranslateUi(pore_size_dlg)
        QtCore.QMetaObject.connectSlotsByName(pore_size_dlg)
        pore_size_dlg.setTabOrder(self.q, self.hint)
        pore_size_dlg.setTabOrder(self.hint, self.v)
        pore_size_dlg.setTabOrder(self.v, self.p)
        pore_size_dlg.setTabOrder(self.p, self.sigma)
        pore_size_dlg.setTabOrder(self.sigma, self.hint2)
        pore_size_dlg.setTabOrder(self.hint2, self.d)
        pore_size_dlg.setTabOrder(self.d, self.delta)
        pore_size_dlg.setTabOrder(self.delta, self.cacl)
        pore_size_dlg.setTabOrder(self.cacl, self.save)

    def retranslateUi(self, pore_size_dlg):
        pore_size_dlg.setWindowTitle(_translate("pore_size_dlg", "抽采管径大小辅助计算", None))
        self.groupBox.setTitle(_translate("pore_size_dlg", "管路参数", None))
        self.hint.setText(_translate("pore_size_dlg", "提 示", None))
        self.mineName_label_11.setText(_translate("pore_size_dlg", "管路最大工作压力P", None))
        self.mineName_label_12.setText(_translate("pore_size_dlg", "管路内混合瓦斯流量Q", None))
        self.mineName_label_10.setText(_translate("pore_size_dlg", "容许压力σ", None))
        self.mineName_label_13.setText(_translate("pore_size_dlg", "经济流速V", None))
        self.mineName_label_9.setText(_translate("pore_size_dlg", "(注：可取5～12m/s)", None))
        self.hint2.setText(_translate("pore_size_dlg", "提 示", None))
        self.cacl.setText(_translate("pore_size_dlg", "计 算", None))
        self.groupBox_2.setTitle(_translate("pore_size_dlg", "计算结果", None))
        self.mineName_label_8.setText(_translate("pore_size_dlg", "管路内径D", None))
        self.mineName_label_7.setText(_translate("pore_size_dlg", "管路壁厚δ", None))
        self.save.setText(_translate("pore_size_dlg", "保 存", None))
        self.lab_Ico.setText(_translate("pore_size_dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

import usecad_rc
