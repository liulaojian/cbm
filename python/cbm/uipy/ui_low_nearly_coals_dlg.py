# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifiles\low_nearly_coals_dlg.ui'
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

class Ui_low_nearly_coals_dlg(object):
    def setupUi(self, low_nearly_coals_dlg):
        low_nearly_coals_dlg.setObjectName(_fromUtf8("low_nearly_coals_dlg"))
        low_nearly_coals_dlg.resize(521, 381)
        self.widget_main = QtGui.QWidget(low_nearly_coals_dlg)
        self.widget_main.setGeometry(QtCore.QRect(0, 30, 521, 351))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widget_main.setFont(font)
        self.widget_main.setObjectName(_fromUtf8("widget_main"))
        self.disc_text = QtGui.QTextEdit(self.widget_main)
        self.disc_text.setEnabled(True)
        self.disc_text.setGeometry(QtCore.QRect(10, 10, 501, 71))
        self.disc_text.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.disc_text.setFrameShape(QtGui.QFrame.NoFrame)
        self.disc_text.setFrameShadow(QtGui.QFrame.Sunken)
        self.disc_text.setLineWidth(0)
        self.disc_text.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.disc_text.setReadOnly(True)
        self.disc_text.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.disc_text.setObjectName(_fromUtf8("disc_text"))
        self.label = QtGui.QLabel(self.widget_main)
        self.label.setGeometry(QtCore.QRect(10, 90, 371, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.tecl_table = QtGui.QTableWidget(self.widget_main)
        self.tecl_table.setGeometry(QtCore.QRect(10, 120, 500, 221))
        self.tecl_table.setObjectName(_fromUtf8("tecl_table"))
        self.tecl_table.setColumnCount(3)
        self.tecl_table.setRowCount(6)
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
        self.tecl_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tecl_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tecl_table.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tecl_table.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tecl_table.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tecl_table.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tecl_table.setItem(3, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tecl_table.setItem(4, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tecl_table.setItem(5, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tecl_table.setItem(5, 2, item)
        self.tecl_table.horizontalHeader().setVisible(True)
        self.tecl_table.verticalHeader().setVisible(False)
        self.tecl_table.verticalHeader().setHighlightSections(True)
        self.widget_title = QtGui.QWidget(low_nearly_coals_dlg)
        self.widget_title.setGeometry(QtCore.QRect(0, 0, 521, 31))
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
        self.lab_Title.setGeometry(QtCore.QRect(40, 0, 431, 31))
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
        self.btnMenu_Close.setGeometry(QtCore.QRect(480, 0, 41, 31))
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

        self.retranslateUi(low_nearly_coals_dlg)
        QtCore.QMetaObject.connectSlotsByName(low_nearly_coals_dlg)

    def retranslateUi(self, low_nearly_coals_dlg):
        low_nearly_coals_dlg.setWindowTitle(_translate("low_nearly_coals_dlg", "低渗近距离煤层群上保护层开采条件井下规模化抽采技术模式", None))
        self.disc_text.setHtml(_translate("low_nearly_coals_dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">该矿井井下煤层气抽采属于：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-weight:600; color:#ff0000;\">低渗近距离煤层群上保护层开采条件井下规模化抽采技术模式</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">这种模式的典型代表为</span><span style=\" font-family:\'宋体\'; font-size:11pt;\">松藻矿区</span><span style=\" font-family:\'宋体\';\">。</span></p></body></html>", None))
        self.label.setText(_translate("low_nearly_coals_dlg", "采掘作业各阶段推荐采用的煤层气抽采技术分别为：", None))
        item = self.tecl_table.horizontalHeaderItem(0)
        item.setText(_translate("low_nearly_coals_dlg", "抽采区域", None))
        item = self.tecl_table.horizontalHeaderItem(1)
        item.setText(_translate("low_nearly_coals_dlg", "抽采技术", None))
        item = self.tecl_table.horizontalHeaderItem(2)
        item.setText(_translate("low_nearly_coals_dlg", "关键技术", None))
        __sortingEnabled = self.tecl_table.isSortingEnabled()
        self.tecl_table.setSortingEnabled(False)
        item = self.tecl_table.item(0, 0)
        item.setText(_translate("low_nearly_coals_dlg", "掘进工作面", None))
        item = self.tecl_table.item(0, 1)
        item.setText(_translate("low_nearly_coals_dlg", "专用瓦斯抽采巷穿层钻孔抽采煤气气技术", None))
        item = self.tecl_table.item(0, 2)
        item.setText(_translate("low_nearly_coals_dlg", "否", None))
        item = self.tecl_table.item(1, 0)
        item.setText(_translate("low_nearly_coals_dlg", "回采工作面", None))
        item = self.tecl_table.item(1, 1)
        item.setText(_translate("low_nearly_coals_dlg", "本煤层顺层钻孔预抽技术", None))
        item = self.tecl_table.item(1, 2)
        item.setText(_translate("low_nearly_coals_dlg", "否", None))
        item = self.tecl_table.item(2, 0)
        item.setText(_translate("low_nearly_coals_dlg", "采空区", None))
        item = self.tecl_table.item(2, 1)
        item.setText(_translate("low_nearly_coals_dlg", "采空区插（埋）管抽采技术", None))
        item = self.tecl_table.item(2, 2)
        item.setText(_translate("low_nearly_coals_dlg", "否", None))
        item = self.tecl_table.item(3, 0)
        item.setText(_translate("low_nearly_coals_dlg", "采空区", None))
        item = self.tecl_table.item(3, 1)
        item.setText(_translate("low_nearly_coals_dlg", "顶板走向高位钻孔抽采技术", None))
        item = self.tecl_table.item(3, 2)
        item.setText(_translate("low_nearly_coals_dlg", "否", None))
        item = self.tecl_table.item(4, 1)
        item.setText(_translate("low_nearly_coals_dlg", "松软突出煤层顺层连续套管护孔技术", None))
        item = self.tecl_table.item(4, 2)
        item.setText(_translate("low_nearly_coals_dlg", "是", None))
        item = self.tecl_table.item(5, 1)
        item.setText(_translate("low_nearly_coals_dlg", "高压水力压裂增透技术", None))
        item = self.tecl_table.item(5, 2)
        item.setText(_translate("low_nearly_coals_dlg", "是", None))
        self.tecl_table.setSortingEnabled(__sortingEnabled)
        self.lab_Ico.setText(_translate("low_nearly_coals_dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

