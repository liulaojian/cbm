# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles\mine_base_param_dlg.ui'
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

class Ui_mine_base_param_dlg(object):
    def setupUi(self, mine_base_param_dlg):
        mine_base_param_dlg.setObjectName(_fromUtf8("mine_base_param_dlg"))
        mine_base_param_dlg.resize(541, 270)
        self.widget_main = QtGui.QWidget(mine_base_param_dlg)
        self.widget_main.setGeometry(QtCore.QRect(0, 30, 541, 241))
        self.widget_main.setObjectName(_fromUtf8("widget_main"))
        self.hydr_geo = QtGui.QComboBox(self.widget_main)
        self.hydr_geo.setGeometry(QtCore.QRect(380, 140, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hydr_geo.setFont(font)
        self.hydr_geo.setObjectName(_fromUtf8("hydr_geo"))
        self.hydr_geo.addItem(_fromUtf8(""))
        self.hydr_geo.addItem(_fromUtf8(""))
        self.hydr_geo.addItem(_fromUtf8(""))
        self.hydr_geo.addItem(_fromUtf8(""))
        self.topo_geo = QtGui.QComboBox(self.widget_main)
        self.topo_geo.setGeometry(QtCore.QRect(130, 140, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.topo_geo.setFont(font)
        self.topo_geo.setObjectName(_fromUtf8("topo_geo"))
        self.topo_geo.addItem(_fromUtf8(""))
        self.topo_geo.addItem(_fromUtf8(""))
        self.topo_geo.addItem(_fromUtf8(""))
        self.mineName_label = QtGui.QLabel(self.widget_main)
        self.mineName_label.setGeometry(QtCore.QRect(21, 20, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label.setFont(font)
        self.mineName_label.setObjectName(_fromUtf8("mineName_label"))
        self.mineName_label_8 = QtGui.QLabel(self.widget_main)
        self.mineName_label_8.setGeometry(QtCore.QRect(170, 60, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label_8.setFont(font)
        self.mineName_label_8.setObjectName(_fromUtf8("mineName_label_8"))
        self.mineName_label_5 = QtGui.QLabel(self.widget_main)
        self.mineName_label_5.setGeometry(QtCore.QRect(360, 60, 21, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label_5.setFont(font)
        self.mineName_label_5.setObjectName(_fromUtf8("mineName_label_5"))
        self.label_4 = QtGui.QLabel(self.widget_main)
        self.label_4.setGeometry(QtCore.QRect(260, 140, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.name = QtGui.QLineEdit(self.widget_main)
        self.name.setGeometry(QtCore.QRect(100, 20, 155, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setObjectName(_fromUtf8("name"))
        self.mineName_label_7 = QtGui.QLabel(self.widget_main)
        self.mineName_label_7.setGeometry(QtCore.QRect(20, 60, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label_7.setFont(font)
        self.mineName_label_7.setObjectName(_fromUtf8("mineName_label_7"))
        self.mineName_label_2 = QtGui.QLabel(self.widget_main)
        self.mineName_label_2.setGeometry(QtCore.QRect(20, 100, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label_2.setFont(font)
        self.mineName_label_2.setObjectName(_fromUtf8("mineName_label_2"))
        self.next = QtGui.QPushButton(self.widget_main)
        self.next.setGeometry(QtCore.QRect(90, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next.setFont(font)
        self.next.setObjectName(_fromUtf8("next"))
        self.label_3 = QtGui.QLabel(self.widget_main)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.region = QtGui.QComboBox(self.widget_main)
        self.region.setGeometry(QtCore.QRect(380, 100, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.region.setFont(font)
        self.region.setObjectName(_fromUtf8("region"))
        self.province = QtGui.QLineEdit(self.widget_main)
        self.province.setGeometry(QtCore.QRect(290, 60, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.province.setFont(font)
        self.province.setObjectName(_fromUtf8("province"))
        self.cancel = QtGui.QPushButton(self.widget_main)
        self.cancel.setGeometry(QtCore.QRect(350, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel.setFont(font)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.base = QtGui.QComboBox(self.widget_main)
        self.base.setGeometry(QtCore.QRect(100, 100, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.base.setFont(font)
        self.base.setObjectName(_fromUtf8("base"))
        self.save = QtGui.QPushButton(self.widget_main)
        self.save.setGeometry(QtCore.QRect(220, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save.setFont(font)
        self.save.setObjectName(_fromUtf8("save"))
        self.mineName_label_4 = QtGui.QLabel(self.widget_main)
        self.mineName_label_4.setGeometry(QtCore.QRect(230, 60, 54, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label_4.setFont(font)
        self.mineName_label_4.setObjectName(_fromUtf8("mineName_label_4"))
        self.city = QtGui.QLineEdit(self.widget_main)
        self.city.setGeometry(QtCore.QRect(380, 60, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.city.setFont(font)
        self.city.setObjectName(_fromUtf8("city"))
        self.mineName_label_3 = QtGui.QLabel(self.widget_main)
        self.mineName_label_3.setGeometry(QtCore.QRect(300, 100, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label_3.setFont(font)
        self.mineName_label_3.setObjectName(_fromUtf8("mineName_label_3"))
        self.capacity = QtGui.QLineEdit(self.widget_main)
        self.capacity.setGeometry(QtCore.QRect(100, 60, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.capacity.setFont(font)
        self.capacity.setObjectName(_fromUtf8("capacity"))
        self.ground_cond = QtGui.QCheckBox(self.widget_main)
        self.ground_cond.setGeometry(QtCore.QRect(280, 20, 211, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ground_cond.setFont(font)
        self.ground_cond.setObjectName(_fromUtf8("ground_cond"))
        self.mineName_label_6 = QtGui.QLabel(self.widget_main)
        self.mineName_label_6.setGeometry(QtCore.QRect(450, 60, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mineName_label_6.setFont(font)
        self.mineName_label_6.setObjectName(_fromUtf8("mineName_label_6"))
        self.widget_title = QtGui.QWidget(mine_base_param_dlg)
        self.widget_title.setGeometry(QtCore.QRect(0, 0, 541, 31))
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
        self.lab_Title.setGeometry(QtCore.QRect(40, 0, 451, 31))
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
        self.btnMenu_Close.setGeometry(QtCore.QRect(500, 0, 41, 31))
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

        self.retranslateUi(mine_base_param_dlg)
        QtCore.QMetaObject.connectSlotsByName(mine_base_param_dlg)

    def retranslateUi(self, mine_base_param_dlg):
        mine_base_param_dlg.setWindowTitle(_translate("mine_base_param_dlg", "请输入目标矿井基本信息", None))
        self.hydr_geo.setItemText(0, _translate("mine_base_param_dlg", "简单", None))
        self.hydr_geo.setItemText(1, _translate("mine_base_param_dlg", "中等", None))
        self.hydr_geo.setItemText(2, _translate("mine_base_param_dlg", "复杂", None))
        self.hydr_geo.setItemText(3, _translate("mine_base_param_dlg", "极复杂", None))
        self.topo_geo.setItemText(0, _translate("mine_base_param_dlg", "简单", None))
        self.topo_geo.setItemText(1, _translate("mine_base_param_dlg", "中等", None))
        self.topo_geo.setItemText(2, _translate("mine_base_param_dlg", "复杂", None))
        self.mineName_label.setText(_translate("mine_base_param_dlg", "矿井名称", None))
        self.mineName_label_8.setText(_translate("mine_base_param_dlg", "(Mt/a)", None))
        self.mineName_label_5.setText(_translate("mine_base_param_dlg", "省", None))
        self.label_4.setText(_translate("mine_base_param_dlg", "水文地质条件", None))
        self.name.setToolTip(_translate("mine_base_param_dlg", "<html><head/><body><p>输入矿井名称</p></body></html>", None))
        self.name.setWhatsThis(_translate("mine_base_param_dlg", "<html><head/><body><p>用户名</p></body></html>", None))
        self.mineName_label_7.setText(_translate("mine_base_param_dlg", "矿井产能", None))
        self.mineName_label_2.setText(_translate("mine_base_param_dlg", "煤炭基地", None))
        self.next.setText(_translate("mine_base_param_dlg", "下 一 步", None))
        self.label_3.setText(_translate("mine_base_param_dlg", "地形地貌特征", None))
        self.cancel.setText(_translate("mine_base_param_dlg", "取  消", None))
        self.save.setText(_translate("mine_base_param_dlg", "保  存", None))
        self.mineName_label_4.setText(_translate("mine_base_param_dlg", "所在地", None))
        self.mineName_label_3.setText(_translate("mine_base_param_dlg", "所在矿区", None))
        self.ground_cond.setText(_translate("mine_base_param_dlg", "是否具备地面井开发条件", None))
        self.mineName_label_6.setText(_translate("mine_base_param_dlg", "市（地区）", None))
        self.lab_Ico.setText(_translate("mine_base_param_dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

