# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles\gas_design_p1_1_dlg.ui'
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

class Ui_gas_design_p1_1_dlg(object):
    def setupUi(self, gas_design_p1_1_dlg):
        gas_design_p1_1_dlg.setObjectName(_fromUtf8("gas_design_p1_1_dlg"))
        gas_design_p1_1_dlg.resize(861, 461)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/cbm.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        gas_design_p1_1_dlg.setWindowIcon(icon)
        self.widget_main = QtGui.QWidget(gas_design_p1_1_dlg)
        self.widget_main.setGeometry(QtCore.QRect(0, 30, 861, 431))
        self.widget_main.setObjectName(_fromUtf8("widget_main"))
        self.groupBox_6 = QtGui.QGroupBox(self.widget_main)
        self.groupBox_6.setGeometry(QtCore.QRect(440, 210, 401, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.ws = QtGui.QLineEdit(self.groupBox_6)
        self.ws.setGeometry(QtCore.QRect(290, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ws.setFont(font)
        self.ws.setObjectName(_fromUtf8("ws"))
        self.label_25 = QtGui.QLabel(self.groupBox_6)
        self.label_25.setGeometry(QtCore.QRect(210, 30, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.ls = QtGui.QLineEdit(self.groupBox_6)
        self.ls.setGeometry(QtCore.QRect(100, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ls.setFont(font)
        self.ls.setObjectName(_fromUtf8("ls"))
        self.label_26 = QtGui.QLabel(self.groupBox_6)
        self.label_26.setGeometry(QtCore.QRect(20, 30, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gs = QtGui.QLineEdit(self.groupBox_6)
        self.gs.setGeometry(QtCore.QRect(290, 70, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gs.setFont(font)
        self.gs.setObjectName(_fromUtf8("gs"))
        self.label_27 = QtGui.QLabel(self.groupBox_6)
        self.label_27.setGeometry(QtCore.QRect(20, 70, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.groupBox_6)
        self.label_28.setGeometry(QtCore.QRect(210, 70, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.hs = QtGui.QLineEdit(self.groupBox_6)
        self.hs.setGeometry(QtCore.QRect(100, 70, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hs.setFont(font)
        self.hs.setObjectName(_fromUtf8("hs"))
        self.label_33 = QtGui.QLabel(self.groupBox_6)
        self.label_33.setGeometry(QtCore.QRect(170, 30, 31, 25))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(self.groupBox_6)
        self.label_34.setGeometry(QtCore.QRect(360, 30, 31, 25))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.label_35 = QtGui.QLabel(self.groupBox_6)
        self.label_35.setGeometry(QtCore.QRect(170, 70, 31, 25))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_36 = QtGui.QLabel(self.groupBox_6)
        self.label_36.setGeometry(QtCore.QRect(360, 70, 31, 25))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.groupBox_5 = QtGui.QGroupBox(self.widget_main)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 210, 411, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.hd = QtGui.QLineEdit(self.groupBox_5)
        self.hd.setGeometry(QtCore.QRect(300, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hd.setFont(font)
        self.hd.setObjectName(_fromUtf8("hd"))
        self.label_21 = QtGui.QLabel(self.groupBox_5)
        self.label_21.setGeometry(QtCore.QRect(210, 30, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.wd = QtGui.QLineEdit(self.groupBox_5)
        self.wd.setGeometry(QtCore.QRect(110, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wd.setFont(font)
        self.wd.setObjectName(_fromUtf8("wd"))
        self.label_22 = QtGui.QLabel(self.groupBox_5)
        self.label_22.setGeometry(QtCore.QRect(20, 30, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.h_offset = QtGui.QLineEdit(self.groupBox_5)
        self.h_offset.setGeometry(QtCore.QRect(300, 90, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.h_offset.setFont(font)
        self.h_offset.setObjectName(_fromUtf8("h_offset"))
        self.label_23 = QtGui.QLabel(self.groupBox_5)
        self.label_23.setGeometry(QtCore.QRect(20, 60, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.groupBox_5)
        self.label_24.setGeometry(QtCore.QRect(20, 90, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.v_offset = QtGui.QLineEdit(self.groupBox_5)
        self.v_offset.setGeometry(QtCore.QRect(300, 60, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.v_offset.setFont(font)
        self.v_offset.setObjectName(_fromUtf8("v_offset"))
        self.label_29 = QtGui.QLabel(self.groupBox_5)
        self.label_29.setGeometry(QtCore.QRect(180, 30, 31, 25))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(self.groupBox_5)
        self.label_30.setGeometry(QtCore.QRect(370, 30, 31, 25))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(self.groupBox_5)
        self.label_31.setGeometry(QtCore.QRect(370, 60, 41, 25))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_32 = QtGui.QLabel(self.groupBox_5)
        self.label_32.setGeometry(QtCore.QRect(370, 90, 41, 25))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.groupBox_2 = QtGui.QGroupBox(self.widget_main)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 100, 411, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.l2 = QtGui.QLineEdit(self.groupBox_2)
        self.l2.setGeometry(QtCore.QRect(300, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l2.setFont(font)
        self.l2.setObjectName(_fromUtf8("l2"))
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(210, 30, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.l1 = QtGui.QLineEdit(self.groupBox_2)
        self.l1.setGeometry(QtCore.QRect(100, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l1.setFont(font)
        self.l1.setObjectName(_fromUtf8("l1"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(20, 30, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.h = QtGui.QLineEdit(self.groupBox_2)
        self.h.setGeometry(QtCore.QRect(300, 60, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.h.setFont(font)
        self.h.setObjectName(_fromUtf8("h"))
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(20, 60, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(210, 60, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.w = QtGui.QLineEdit(self.groupBox_2)
        self.w.setGeometry(QtCore.QRect(100, 60, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.w.setFont(font)
        self.w.setObjectName(_fromUtf8("w"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(170, 30, 31, 25))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(370, 30, 41, 25))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(170, 60, 41, 25))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(370, 60, 41, 25))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.head_graph = QtGui.QPushButton(self.widget_main)
        self.head_graph.setGeometry(QtCore.QRect(450, 360, 130, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.head_graph.setFont(font)
        self.head_graph.setObjectName(_fromUtf8("head_graph"))
        self.save = QtGui.QPushButton(self.widget_main)
        self.save.setGeometry(QtCore.QRect(130, 360, 130, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save.setFont(font)
        self.save.setObjectName(_fromUtf8("save"))
        self.groupBox = QtGui.QGroupBox(self.widget_main)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.dip_angle = QtGui.QLineEdit(self.groupBox)
        self.dip_angle.setGeometry(QtCore.QRect(300, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dip_angle.setFont(font)
        self.dip_angle.setObjectName(_fromUtf8("dip_angle"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(210, 30, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.thick = QtGui.QLineEdit(self.groupBox)
        self.thick.setGeometry(QtCore.QRect(100, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thick.setFont(font)
        self.thick.setObjectName(_fromUtf8("thick"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(170, 30, 41, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(370, 30, 41, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.groupBox_3 = QtGui.QGroupBox(self.widget_main)
        self.groupBox_3.setGeometry(QtCore.QRect(440, 20, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gp = QtGui.QLineEdit(self.groupBox_3)
        self.gp.setGeometry(QtCore.QRect(290, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gp.setFont(font)
        self.gp.setObjectName(_fromUtf8("gp"))
        self.label_15 = QtGui.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(210, 30, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.dp = QtGui.QLineEdit(self.groupBox_3)
        self.dp.setGeometry(QtCore.QRect(100, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dp.setFont(font)
        self.dp.setObjectName(_fromUtf8("dp"))
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(20, 30, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(170, 30, 31, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(360, 30, 31, 25))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.dip_graph = QtGui.QPushButton(self.widget_main)
        self.dip_graph.setGeometry(QtCore.QRect(610, 360, 130, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dip_graph.setFont(font)
        self.dip_graph.setObjectName(_fromUtf8("dip_graph"))
        self.plane_graph = QtGui.QPushButton(self.widget_main)
        self.plane_graph.setGeometry(QtCore.QRect(290, 360, 130, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plane_graph.setFont(font)
        self.plane_graph.setObjectName(_fromUtf8("plane_graph"))
        self.groupBox_4 = QtGui.QGroupBox(self.widget_main)
        self.groupBox_4.setGeometry(QtCore.QRect(440, 100, 401, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.bottom = QtGui.QLineEdit(self.groupBox_4)
        self.bottom.setGeometry(QtCore.QRect(210, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bottom.setFont(font)
        self.bottom.setObjectName(_fromUtf8("bottom"))
        self.label_16 = QtGui.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(160, 30, 31, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.top = QtGui.QLineEdit(self.groupBox_4)
        self.top.setGeometry(QtCore.QRect(70, 30, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.top.setFont(font)
        self.top.setObjectName(_fromUtf8("top"))
        self.label_18 = QtGui.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(20, 30, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.right = QtGui.QLineEdit(self.groupBox_4)
        self.right.setGeometry(QtCore.QRect(210, 60, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.right.setFont(font)
        self.right.setObjectName(_fromUtf8("right"))
        self.label_19 = QtGui.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(20, 60, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(160, 60, 31, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.left = QtGui.QLineEdit(self.groupBox_4)
        self.left.setGeometry(QtCore.QRect(70, 60, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.left.setFont(font)
        self.left.setObjectName(_fromUtf8("left"))
        self.help = QtGui.QPushButton(self.groupBox_4)
        self.help.setGeometry(QtCore.QRect(290, 30, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.help.setFont(font)
        self.help.setObjectName(_fromUtf8("help"))
        self.widget_title = QtGui.QWidget(gas_design_p1_1_dlg)
        self.widget_title.setGeometry(QtCore.QRect(0, 0, 861, 31))
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
        self.lab_Title.setGeometry(QtCore.QRect(40, 0, 771, 31))
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
        self.btnMenu_Close.setGeometry(QtCore.QRect(820, 0, 41, 31))
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

        self.retranslateUi(gas_design_p1_1_dlg)
        QtCore.QMetaObject.connectSlotsByName(gas_design_p1_1_dlg)
        gas_design_p1_1_dlg.setTabOrder(self.thick, self.dip_angle)
        gas_design_p1_1_dlg.setTabOrder(self.dip_angle, self.dp)
        gas_design_p1_1_dlg.setTabOrder(self.dp, self.gp)
        gas_design_p1_1_dlg.setTabOrder(self.gp, self.l1)
        gas_design_p1_1_dlg.setTabOrder(self.l1, self.l2)
        gas_design_p1_1_dlg.setTabOrder(self.l2, self.top)
        gas_design_p1_1_dlg.setTabOrder(self.top, self.bottom)
        gas_design_p1_1_dlg.setTabOrder(self.bottom, self.w)
        gas_design_p1_1_dlg.setTabOrder(self.w, self.h)
        gas_design_p1_1_dlg.setTabOrder(self.h, self.left)
        gas_design_p1_1_dlg.setTabOrder(self.left, self.right)
        gas_design_p1_1_dlg.setTabOrder(self.right, self.help)
        gas_design_p1_1_dlg.setTabOrder(self.help, self.wd)
        gas_design_p1_1_dlg.setTabOrder(self.wd, self.hd)
        gas_design_p1_1_dlg.setTabOrder(self.hd, self.v_offset)
        gas_design_p1_1_dlg.setTabOrder(self.v_offset, self.h_offset)
        gas_design_p1_1_dlg.setTabOrder(self.h_offset, self.ls)
        gas_design_p1_1_dlg.setTabOrder(self.ls, self.ws)
        gas_design_p1_1_dlg.setTabOrder(self.ws, self.hs)
        gas_design_p1_1_dlg.setTabOrder(self.hs, self.gs)
        gas_design_p1_1_dlg.setTabOrder(self.gs, self.save)
        gas_design_p1_1_dlg.setTabOrder(self.save, self.plane_graph)
        gas_design_p1_1_dlg.setTabOrder(self.plane_graph, self.head_graph)
        gas_design_p1_1_dlg.setTabOrder(self.head_graph, self.dip_graph)

    def retranslateUi(self, gas_design_p1_1_dlg):
        gas_design_p1_1_dlg.setWindowTitle(_translate("gas_design_p1_1_dlg", "底板岩巷密集穿层钻孔抽采煤巷条带瓦斯", None))
        self.groupBox_6.setTitle(_translate("gas_design_p1_1_dlg", "钻场参数", None))
        self.label_25.setText(_translate("gas_design_p1_1_dlg", "钻场宽度", None))
        self.label_26.setText(_translate("gas_design_p1_1_dlg", "钻场长度", None))
        self.label_27.setText(_translate("gas_design_p1_1_dlg", "钻场高度", None))
        self.label_28.setText(_translate("gas_design_p1_1_dlg", "钻场间距", None))
        self.label_33.setText(_translate("gas_design_p1_1_dlg", "(m)", None))
        self.label_34.setText(_translate("gas_design_p1_1_dlg", "(m)", None))
        self.label_35.setText(_translate("gas_design_p1_1_dlg", "(m)", None))
        self.label_36.setText(_translate("gas_design_p1_1_dlg", "(m)", None))
        self.groupBox_5.setTitle(_translate("gas_design_p1_1_dlg", "底板巷参数", None))
        self.label_21.setText(_translate("gas_design_p1_1_dlg", "底板巷高度", None))
        self.label_22.setText(_translate("gas_design_p1_1_dlg", "底板巷宽度", None))
        self.label_23.setText(_translate("gas_design_p1_1_dlg", "底板巷与工作面垂距", None))
        self.label_24.setText(_translate("gas_design_p1_1_dlg", "底板巷与工作面风巷水平投影距离", None))
        self.label_29.setText(_translate("gas_design_p1_1_dlg", "(m)", None))
        self.label_30.setText(_translate("gas_design_p1_1_dlg", "(m)", None))
        self.label_31.setText(_translate("gas_design_p1_1_dlg", "(m)", None))
        self.label_32.setText(_translate("gas_design_p1_1_dlg", "(m)", None))
        self.groupBox_2.setTitle(_translate("gas_design_p1_1_dlg", "工作面参数", None))
        self.label_11.setText(_translate("gas_design_p1_1_dlg", "工作面长度", None))
        self.label_13.setText(_translate("gas_design_p1_1_dlg", "顺槽长度", None))
        self.label_14.setText(_translate("gas_design_p1_1_dlg", "巷道宽度", None))
        self.label_12.setText(_translate("gas_design_p1_1_dlg", "巷道高度", None))
        self.label_3.setText(_translate("gas_design_p1_1_dlg", "(m)", None))
        self.label_4.setText(_translate("gas_design_p1_1_dlg", "(m)", None))
        self.label_5.setText(_translate("gas_design_p1_1_dlg", "(m)", None))
        self.label_8.setText(_translate("gas_design_p1_1_dlg", "(m)", None))
        self.head_graph.setText(_translate("gas_design_p1_1_dlg", "走 向 剖 面 图", None))
        self.save.setText(_translate("gas_design_p1_1_dlg", "保 存", None))
        self.groupBox.setTitle(_translate("gas_design_p1_1_dlg", "煤层参数", None))
        self.label_10.setText(_translate("gas_design_p1_1_dlg", "煤层倾角", None))
        self.label_7.setText(_translate("gas_design_p1_1_dlg", "<html><head/><body><p>(m)</p></body></html>", None))
        self.label_9.setText(_translate("gas_design_p1_1_dlg", "<html><head/><body><p>(°)</p></body></html>", None))
        self.label_6.setText(_translate("gas_design_p1_1_dlg", "煤层厚度", None))
        self.groupBox_3.setTitle(_translate("gas_design_p1_1_dlg", "钻孔参数", None))
        self.label_15.setText(_translate("gas_design_p1_1_dlg", "钻孔间距", None))
        self.label_17.setText(_translate("gas_design_p1_1_dlg", "钻孔直径", None))
        self.label.setText(_translate("gas_design_p1_1_dlg", "(m)", None))
        self.label_2.setText(_translate("gas_design_p1_1_dlg", "(m)", None))
        self.dip_graph.setText(_translate("gas_design_p1_1_dlg", "倾 向 剖 面 图", None))
        self.plane_graph.setText(_translate("gas_design_p1_1_dlg", "平 面 图", None))
        self.groupBox_4.setTitle(_translate("gas_design_p1_1_dlg", "回采巷道控制范围", None))
        self.label_16.setText(_translate("gas_design_p1_1_dlg", "下帮", None))
        self.label_18.setText(_translate("gas_design_p1_1_dlg", "上帮", None))
        self.label_19.setText(_translate("gas_design_p1_1_dlg", "左帮", None))
        self.label_20.setText(_translate("gas_design_p1_1_dlg", "右帮", None))
        self.help.setText(_translate("gas_design_p1_1_dlg", "参考取值", None))
        self.lab_Ico.setText(_translate("gas_design_p1_1_dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

import usecad_rc
