# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles\high_coal_dlg.ui'
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

class Ui_high_coal_dlg(object):
    def setupUi(self, high_coal_dlg):
        high_coal_dlg.setObjectName(_fromUtf8("high_coal_dlg"))
        high_coal_dlg.resize(531, 631)
        font = QtGui.QFont()
        font.setPointSize(12)
        high_coal_dlg.setFont(font)
        high_coal_dlg.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.widget_title = QtGui.QWidget(high_coal_dlg)
        self.widget_title.setGeometry(QtCore.QRect(0, 0, 531, 31))
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
        self.lab_Title.setGeometry(QtCore.QRect(40, 0, 441, 31))
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
        self.btnMenu_Close.setGeometry(QtCore.QRect(490, 0, 41, 31))
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
        self.widget_main = QtGui.QWidget(high_coal_dlg)
        self.widget_main.setGeometry(QtCore.QRect(0, 30, 531, 601))
        self.widget_main.setObjectName(_fromUtf8("widget_main"))
        self.label_5 = QtGui.QLabel(self.widget_main)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 181, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_4 = QtGui.QLabel(self.widget_main)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 151, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label = QtGui.QLabel(self.widget_main)
        self.label.setGeometry(QtCore.QRect(10, 160, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tecl_table = QtGui.QTableWidget(self.widget_main)
        self.tecl_table.setGeometry(QtCore.QRect(10, 190, 511, 241))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tecl_table.setFont(font)
        self.tecl_table.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tecl_table.setGridStyle(QtCore.Qt.DashLine)
        self.tecl_table.setObjectName(_fromUtf8("tecl_table"))
        self.tecl_table.setColumnCount(3)
        self.tecl_table.setRowCount(7)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tecl_table.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(3, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(4, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(5, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(5, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(6, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(6, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(6, 2, item)
        self.tecl_table.horizontalHeader().setVisible(True)
        self.tecl_table.verticalHeader().setVisible(False)
        self.tecl_table.verticalHeader().setHighlightSections(False)
        self.label_3 = QtGui.QLabel(self.widget_main)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 511, 61))
        self.label_3.setToolTip(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self.widget_main)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_6 = QtGui.QLabel(self.widget_main)
        self.label_6.setGeometry(QtCore.QRect(10, 440, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tecl_table_2 = QtGui.QTableWidget(self.widget_main)
        self.tecl_table_2.setGeometry(QtCore.QRect(10, 470, 511, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tecl_table_2.setFont(font)
        self.tecl_table_2.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tecl_table_2.setGridStyle(QtCore.Qt.DashLine)
        self.tecl_table_2.setObjectName(_fromUtf8("tecl_table_2"))
        self.tecl_table_2.setColumnCount(2)
        self.tecl_table_2.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.tecl_table_2.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table_2.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table_2.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table_2.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table_2.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table_2.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table_2.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table_2.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table_2.setItem(2, 1, item)
        self.tecl_table_2.horizontalHeader().setVisible(True)
        self.tecl_table_2.verticalHeader().setVisible(False)
        self.tecl_table_2.verticalHeader().setHighlightSections(False)
        self.tBtn = QtGui.QPushButton(self.widget_main)
        self.tBtn.setGeometry(QtCore.QRect(330, 110, 171, 41))
        self.tBtn.setToolTip(_fromUtf8(""))
        self.tBtn.setObjectName(_fromUtf8("tBtn"))

        self.retranslateUi(high_coal_dlg)
        QtCore.QMetaObject.connectSlotsByName(high_coal_dlg)

    def retranslateUi(self, high_coal_dlg):
        high_coal_dlg.setWindowTitle(_translate("high_coal_dlg", "中高渗单一煤层条件井下规模化抽采技术模式", None))
        self.lab_Ico.setText(_translate("high_coal_dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_5.setText(_translate("high_coal_dlg", "这种模式的典型代表为：", None))
        self.label_4.setText(_translate("high_coal_dlg", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ff557f;\">晋 城 矿 区</span></p></body></html>", None))
        self.label.setText(_translate("high_coal_dlg", "采掘作业各阶段推荐采用的煤层气抽采技术分别为：", None))
        item = self.tecl_table.verticalHeaderItem(0)
        item.setText(_translate("high_coal_dlg", "1", None))
        item = self.tecl_table.verticalHeaderItem(1)
        item.setText(_translate("high_coal_dlg", "2", None))
        item = self.tecl_table.verticalHeaderItem(2)
        item.setText(_translate("high_coal_dlg", "3", None))
        item = self.tecl_table.verticalHeaderItem(3)
        item.setText(_translate("high_coal_dlg", "4", None))
        item = self.tecl_table.verticalHeaderItem(4)
        item.setText(_translate("high_coal_dlg", "5", None))
        item = self.tecl_table.verticalHeaderItem(5)
        item.setText(_translate("high_coal_dlg", "6", None))
        item = self.tecl_table.verticalHeaderItem(6)
        item.setText(_translate("high_coal_dlg", "7", None))
        item = self.tecl_table.horizontalHeaderItem(0)
        item.setText(_translate("high_coal_dlg", "序号", None))
        item = self.tecl_table.horizontalHeaderItem(1)
        item.setText(_translate("high_coal_dlg", "抽采技术", None))
        item = self.tecl_table.horizontalHeaderItem(2)
        item.setText(_translate("high_coal_dlg", "抽采区域", None))
        __sortingEnabled = self.tecl_table.isSortingEnabled()
        self.tecl_table.setSortingEnabled(False)
        item = self.tecl_table.item(0, 0)
        item.setText(_translate("high_coal_dlg", "1", None))
        item = self.tecl_table.item(0, 1)
        item.setText(_translate("high_coal_dlg", "定向长钻孔条带预抽技术", None))
        item = self.tecl_table.item(0, 2)
        item.setText(_translate("high_coal_dlg", "掘进工作面", None))
        item = self.tecl_table.item(1, 0)
        item.setText(_translate("high_coal_dlg", "2", None))
        item = self.tecl_table.item(1, 1)
        item.setText(_translate("high_coal_dlg", "近距离顶板梳状钻孔抽采技术", None))
        item = self.tecl_table.item(1, 2)
        item.setText(_translate("high_coal_dlg", "掘进工作面", None))
        item = self.tecl_table.item(2, 0)
        item.setText(_translate("high_coal_dlg", "3", None))
        item = self.tecl_table.item(2, 1)
        item.setText(_translate("high_coal_dlg", "近距离底板梳状钻孔抽采技术", None))
        item = self.tecl_table.item(2, 2)
        item.setText(_translate("high_coal_dlg", "掘进工作面", None))
        item = self.tecl_table.item(3, 0)
        item.setText(_translate("high_coal_dlg", "4", None))
        item = self.tecl_table.item(3, 1)
        item.setText(_translate("high_coal_dlg", "本煤层顺层钻孔预抽技术", None))
        item = self.tecl_table.item(3, 2)
        item.setText(_translate("high_coal_dlg", "回采工作面", None))
        item = self.tecl_table.item(4, 0)
        item.setText(_translate("high_coal_dlg", "5", None))
        item = self.tecl_table.item(4, 1)
        item.setText(_translate("high_coal_dlg", "区域递进式模块化抽采技术", None))
        item = self.tecl_table.item(4, 2)
        item.setText(_translate("high_coal_dlg", "回采工作面", None))
        item = self.tecl_table.item(5, 0)
        item.setText(_translate("high_coal_dlg", "6", None))
        item = self.tecl_table.item(5, 1)
        item.setText(_translate("high_coal_dlg", "采空区插（埋）管抽采技术", None))
        item = self.tecl_table.item(5, 2)
        item.setText(_translate("high_coal_dlg", "采空区", None))
        item = self.tecl_table.item(6, 0)
        item.setText(_translate("high_coal_dlg", "7", None))
        item = self.tecl_table.item(6, 1)
        item.setText(_translate("high_coal_dlg", "地面采动区井（或L型井）抽采技术", None))
        item = self.tecl_table.item(6, 2)
        item.setText(_translate("high_coal_dlg", "采空区", None))
        self.tecl_table.setSortingEnabled(__sortingEnabled)
        self.label_3.setWhatsThis(_translate("high_coal_dlg", "<html><head/><body><p><br/></p></body></html>", None))
        self.label_3.setText(_translate("high_coal_dlg", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ff557f;\">中高渗单一煤层条件井下规模化抽采技术模式</span></p></body></html>", None))
        self.label_2.setText(_translate("high_coal_dlg", "该矿井井下煤层气抽采属于：", None))
        self.label_6.setText(_translate("high_coal_dlg", "现阶段重点攻克的关键技术为：", None))
        item = self.tecl_table_2.verticalHeaderItem(0)
        item.setText(_translate("high_coal_dlg", "1", None))
        item = self.tecl_table_2.verticalHeaderItem(1)
        item.setText(_translate("high_coal_dlg", "2", None))
        item = self.tecl_table_2.verticalHeaderItem(2)
        item.setText(_translate("high_coal_dlg", "3", None))
        item = self.tecl_table_2.horizontalHeaderItem(0)
        item.setText(_translate("high_coal_dlg", "序号", None))
        item = self.tecl_table_2.horizontalHeaderItem(1)
        item.setText(_translate("high_coal_dlg", "关键技术", None))
        __sortingEnabled = self.tecl_table_2.isSortingEnabled()
        self.tecl_table_2.setSortingEnabled(False)
        item = self.tecl_table_2.item(0, 0)
        item.setText(_translate("high_coal_dlg", "1", None))
        item = self.tecl_table_2.item(0, 1)
        item.setText(_translate("high_coal_dlg", "中硬煤层顺煤层井下长钻孔钻进工艺", None))
        item = self.tecl_table_2.item(1, 0)
        item.setText(_translate("high_coal_dlg", "2", None))
        item = self.tecl_table_2.item(1, 1)
        item.setText(_translate("high_coal_dlg", "软硬复合破碎煤层顺煤层抽采技术工艺", None))
        item = self.tecl_table_2.item(2, 0)
        item.setText(_translate("high_coal_dlg", "3", None))
        item = self.tecl_table_2.item(2, 1)
        item.setText(_translate("high_coal_dlg", "CO2预裂爆破增透技术工艺", None))
        self.tecl_table_2.setSortingEnabled(__sortingEnabled)
        self.tBtn.setText(_translate("high_coal_dlg", "时空衔接关系示意图", None))

import usecad_rc
