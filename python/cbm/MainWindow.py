#coding:utf-8

from uipy.ui_mainwin import *
from dialogs.LoginDlg import *
from dialogs.SampleManageDlg import *
from dialogs.MineDeginDlg import *
from dialogs.MineBaseParamDlg import *
from dialogs.DifficultEvalDlg import *
from dialogs.MineGasReservesPredictDlg import *
from dialogs.MineGasFlowPredictDlg import *
from dialogs.TwsGasFlowPredictDlg import *
from dialogs.WsGasFlowPredictDlg import *
from dialogs.HighDrillingTunnelDlg import *
from dialogs.HighDrillingDesignDlg import *
from dialogs.DrillingRadiusDlg import *
from dialogs.PoreSizeDlg import *
from dialogs.PoreFlowDlg import *
from dialogs.GasDesignDlg import *
import doc

from rpc import CbmUtil, SQLClientHelper, CbmClientHelper
from cbm.ttypes import *

import DataHelper
from DataHelper import Authority
import UiHelper

class MainWindow(QtGui.QMainWindow):  
	def __init__(self,parent=None):
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.init()
		# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
		# 瓦斯抽采设计类型

	def init(self):
		self.myActions = []
		self.loginAction = None
		self.logoutAction = None
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.createActions()
		self.createMenusToolBars()
		self.createStatusBar()
		self.setWindowTitle(u"井下煤层气规模化抽采计算机辅助设计（CAD）系统——数据录入模块")
		self.setWindowIcon(QtGui.QIcon(':/images/cbm.ico'))
		palette1 = QtGui.QPalette()
		#palette1.setColor(self.backgroundRole(), QColor(192,253,123))#设置背景颜色
		palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(':/images/bg.png')))
		self.setPalette(palette1)
	
	def real_logout(self):
		# 注销(清空sys_info表)
		DataHelper.sql_logout()
		# 设置菜单激活状态
		self.loginAction.setEnabled(True)
		self.logoutAction.setEnabled(False)

	def closeEvent(self, event):
		reply = UiHelper.MessageBox(u'确定退出本系统?', True)
		if reply == True:
			# 注销
			self.real_logout()
			# close消息处理完毕,不再需要qt继续处理close消息了
			event.accept()
		else:
			# qt内部继续处理close消息
			event.ignore()

	def login(self):
		"""返回True或False"""
		dialog = LoginDialog()
		if dialog.exec_():
			self.loginAction.setEnabled(False)
			self.logoutAction.setEnabled(True)
			return True
		else:  
			return False

	def logout(self):
		reply = UiHelper.MessageBox(u'您确定要注销?', True)
		if reply == True:
			# 注销
			self.real_logout()

	def run_dialog(self, DialogClass):
		# 启动对话框(传入当前登录用户的)
		mine = CbmClientHelper.GetOnlineMine()
		dlg = DialogClass(mine.id)
		dlg.exec_()

	# 尝试运行对话框
	def try_run(self, DialogClass, authority):
		can_run = True
		while can_run:
			# 检查用户登录状态
			ret = DataHelper.sql_login_status()
			# 内部错误
			if ret == 0 or ret == -1:
				UiHelper.MessageBox(u"系统技术性故障(错误码:M1),请联系技术人员!")
				can_run = False
				break
			# 用户未登录
			elif ret == 2:
				UiHelper.MessageBox(u"您需要登录才能使用本功能!")
				can_run = self.login() # 登录
			# 管理员已登录		
			elif ret == 3 and authority == Authority.USER:
				UiHelper.MessageBox(u"管理员禁止使用该功能,请重新登录!")
				can_run = self.login() # 登录
			# 普通用户已登录
			elif ret == 1 and authority == Authority.ADMIN:
				UiHelper.MessageBox(u"您的权限不够,请重新登录!")
				can_run = self.login() # 登录

			if can_run and DataHelper.sql_login_authority(authority):
				break

		# 启动对话框
		if can_run:
			# 启动对话框(传入当前登录用户的)
			self.run_dialog(DialogClass)

	def sampleManage(self):
		# 启动示范矿区管理库对话框
		self.try_run(SampleManageDlg, Authority.ADMIN)

	def deginMine(self):
		# 启动矿井设计对话框
		self.try_run(MineDeginDlg, Authority.USER)

	def dragTec(self):
		# 启动辅助决策对话框
		self.try_run(MineBaseParamDlg, Authority.USER)

	def difficultEval(self):
		# 启动抽采难易程度评价对话框
		self.try_run(DifficultEvalDlg, Authority.USER)

	def mineGasReservesPredict(self):
		# 启动矿井瓦斯储量计算对话框
		self.try_run(MineGasReservesPredictDlg, Authority.USER)

	def mineGasFlowPredict(self):
		# 启动矿井瓦斯流量计算对话框
		self.try_run(MineGasFlowPredictDlg, Authority.USER)

	def twsGasFlowPredict(self):
		# 启动掘进面瓦斯流量计算对话框
		self.try_run(TwsGasFlowPredictDlg, Authority.USER)

	def wsGasFlowPredict(self):
		# 启动工作面瓦斯流量计算对话框
		self.try_run(WsGasFlowPredictDlg, Authority.USER)

	def highDrillingTunnel(self):
		# 启动高抽巷计算对话框
		self.try_run(HighDrillingTunnelDlg, Authority.USER)

	def highDrillingPore(self):
		# 启动高抽钻孔计算对话框
		self.try_run(HighDrillingDesignDlg, Authority.USER)

	def drillingRadius(self):
		# 启动瓦斯抽采半径计算对话框
		self.try_run(DrillingRadiusDlg, Authority.USER)

	def poreSize(self):
		# 启动瓦斯抽采钻孔计算对话框
		self.try_run(PoreSizeDlg, Authority.USER)

	def poreFlow(self):
		# 启动孔板流量计算对话框
		self.try_run(PoreFlowDlg, Authority.USER)

	def evaluationUnitDivision(self):
		# 启动评价单元划分计算对话框
		# self.try_run(PoreFlowDlg, Authority.USER)
		pass

	def wsGasDesign(self):
		# 进行工作面的瓦斯抽采设计
		DataHelper.GAS_DESIGN_TYPE = 1
		# 启动瓦斯抽采设计对话框
		self.try_run(GasDesignDlg, Authority.USER)

	def twsGasDesign(self):
		# 进行掘进面的瓦斯抽采设计
		DataHelper.GAS_DESIGN_TYPE = 2
		# 启动掘进面瓦斯抽采设计对话框
		self.try_run(GasDesignDlg, Authority.USER)

	def goafGasDesign(self):
		# 进行采空区的瓦斯抽采设计
		DataHelper.GAS_DESIGN_TYPE = 3
		self.try_run(GasDesignDlg, Authority.USER)

	def openOfficeNet(self):
		doc.OpenNet('http://www.ccri.com.cn/')

	#查看《煤层气资源勘察技术规范》文档
	def investigationOfCBMResources(self):
		doc.OpenPDFFile(u'help\\pdf\\煤层气资源勘察技术规范.pdf')

	#查看《保护层开采技术规范》文档
	def protectiveLayerMining(self):
		doc.OpenPDFFile('help\\pdf\\保护层开采技术规范.pdf')

	#查看《煤矿瓦斯抽放规范》文档
	def coalMineGasDrainage(self):
		doc.OpenPDFFile(u'help\\pdf\\煤矿瓦斯抽放规范.pdf')

	#查看《煤矿瓦斯抽放技术规范》文档
	def technicalSpecificationCoalMineGasDrainage(self):
		doc.OpenPDFFile(u'help\\pdf\\煤矿瓦斯抽放技术规范.pdf')

	#查看《煤矿瓦斯抽采工程设计规范》文档
	def coalMineGasDrainageEngineeringDesign(self):
		doc.OpenPDFFile(u'help\\pdf\\煤矿瓦斯抽采工程设计规范.pdf')

	#查看《煤矿瓦斯抽采达标暂行规定》文档
	def standardInterimProvisions(self):
		doc.OpenPDFFile(u'help\\pdf\\煤矿瓦斯抽采达标暂行规定.pdf')

	#查看《煤层气(煤矿瓦斯)开发利用十二五规划》文档
	def coalGasDevelopment(self):
		doc.OpenPDFFile(u'help\\pdf\\煤层气(煤矿瓦斯)开发利用十二五规划.pdf')

	#查看《煤矿瓦斯抽采基本指标》文档
	def basicCoalMineGasIndex(self):
		doc.OpenPDFFile(u'help\\pdf\\煤矿瓦斯抽采基本指标.pdf')


	def buildAction(self,name,tip,trigger):
		return QtGui.QAction(name, self, statusTip=tip, triggered=trigger)

	def regAction(self,menu,name,tip,trigger):
		return self.myActions.append([menu,name,tip,trigger])

	def createActions(self):
		self.regAction(u"账户管理", u"登录", u"用户登录", self.login)
		self.regAction(u"账户管理", u"注销", u"注销用户", self.logout)		
		self.regAction(u"设计模块", u"示范矿区技术管理", u"对示范矿区进行技术管理", self.sampleManage)
		self.regAction(u"设计模块", u"矿井设计", u"设计本矿井", self.deginMine)
		self.regAction(u"辅助决策", u"抽采技术模式", u"抽采技术模式辅助决策", self.dragTec)
		self.regAction(u"辅助计算", u"煤层气抽采难易程度评价", u"煤层气抽采难易程度评价辅助计算", self.difficultEval)
		self.regAction(u"辅助计算", u"矿井煤层气储量及可抽量预测", u"矿井煤层气储量及可抽量预测辅助计算", self.mineGasReservesPredict)
		self.regAction(u"辅助计算", u"矿井瓦斯涌出量预测", u"矿井瓦斯涌出量预测辅助计算", self.mineGasFlowPredict)
		self.regAction(u"辅助计算", u"掘进面瓦斯涌出量预测", u"掘进面瓦斯涌出量预测辅助计算", self.twsGasFlowPredict)
		self.regAction(u"辅助计算", u"回采面瓦斯涌出量预测", u"回采面瓦斯涌出量预测辅助计算", self.wsGasFlowPredict)
		self.regAction(u"辅助计算", u"高抽巷合理布设层位", u"高抽巷合理布设层位辅助计算", self.highDrillingTunnel)
		self.regAction(u"辅助计算", u"高位抽采钻孔有效布设范围", u"高位抽采钻孔有效布设范围辅助计算", self.highDrillingPore)
		self.regAction(u"辅助计算", u"煤层瓦斯抽采半径", u"煤层瓦斯抽采半径辅助计算", self.drillingRadius)
		self.regAction(u"辅助计算", u"抽采管径大小", u"抽采管径大小辅助计算", self.poreSize)
		self.regAction(u"辅助计算", u"孔板流量", u"孔板流量辅助计算", self.poreFlow)
		self.regAction(u"辅助计算", u"评价单元划分", u"评价单元划分辅助计算", self.evaluationUnitDivision)
		self.regAction(u"抽采设计", u"工作面", u"工作面瓦斯抽采辅助设计", self.wsGasDesign)
		self.regAction(u"抽采设计", u"掘进面", u"掘进面瓦斯抽采辅助设计", self.twsGasDesign)
		self.regAction(u"抽采设计", u"采空区", u"采空区瓦斯抽采辅助设计", self.goafGasDesign)
		self.regAction(u"帮助文档", u"官网", u"打开官网", self.openOfficeNet)
		self.regAction(u"帮助文档", u"煤层气资源勘察技术规范", u"查看《煤层气资源勘察技术规范》文档", self.investigationOfCBMResources)
		self.regAction(u"帮助文档", u"保护层开采技术规范", u"查看《保护层开采技术规范》文档", self.protectiveLayerMining)
		self.regAction(u"帮助文档", u"煤矿瓦斯抽放规范", u"查看《煤矿瓦斯抽放规范》文档", self.coalMineGasDrainage)
		self.regAction(u"帮助文档", u"煤矿瓦斯抽放技术规范", u"查看《煤矿瓦斯抽放技术规范》文档", self.technicalSpecificationCoalMineGasDrainage)
		self.regAction(u"帮助文档", u"煤矿瓦斯抽采工程设计规范", u"查看《煤矿瓦斯抽采工程设计规范》文档", self.coalMineGasDrainageEngineeringDesign)
		self.regAction(u"帮助文档", u"煤矿瓦斯抽采达标暂行规定", u"查看《煤矿瓦斯抽采达标暂行规定》文档", self.standardInterimProvisions)
		self.regAction(u"帮助文档", u"煤层气(煤矿瓦斯)开发利用十二五规划", u"查看《煤层气(煤矿瓦斯)开发利用十二五规划》文档", self.coalGasDevelopment)
		self.regAction(u"帮助文档", u"煤矿瓦斯抽采基本指标", u"查看《煤矿瓦斯抽采基本指标》文档", self.basicCoalMineGasIndex)

	def createMenusToolBars(self):
		menus = {}
		toolBars = {}
		for menu,name,tip,trigger in self.myActions:
			action = self.buildAction(name,tip,trigger)
			if name == u"登录":
				self.loginAction = action
				self.loginAction.setEnabled(False)
			if name == u"注销":
				self.logoutAction = action
			if menu not in menus:
				menus[menu] = self.menuBar().addMenu(menu)
				# toolBars[menu] = self.addToolBar(menu)
			menus[menu].addAction(action)
			# 增加工具栏
			# toolBars[menu].addAction(action)

	def createStatusBar(self):
		self.statusBar().showMessage(u"欢迎使用\"井下煤层气规模化抽采计算机辅助设计（CAD）系统——数据录入模块\"")


def loginFirst():
	"""返回True或False"""
	dialog = LoginDialog()
	if dialog.exec_():
		return True
	else:
		return False

# 设置皮肤样式
def SetStyle(app, styleName):
	file = QtCore.QFile(QtCore.QString(":/images/%1.css").arg(styleName))
	file.open(QtCore.QFile.ReadOnly)
	qss = QtCore.QString(file.readAll())
	print unicode(qss)
	app.setStyleSheet(qss)
	app.setPalette(QtGui.QPalette(QtGui.QColor("#F0F0F0")))

# 设置编码为UTF8
def SetUTF8Code(app):
	codec = QtCore.QTextCodec.codecForName("UTF-8")
	QtCore.QTextCodec.setCodecForLocale(codec)
	QtCore.QTextCodec.setCodecForCStrings(codec)
	QtCore.QTextCodec.setCodecForTr(codec)

# 加载中文字符
def SetChinese(app):
	translator = QtCore.QTranslator(app)
	translator.load(":/images/qt_zh_CN.qm")
	app.installTranslator(translator)

def run():
	import sys
	app = QtGui.QApplication(sys.argv)
	# 设置utf-8编码
	SetUTF8Code(app)
	# 设置样式
	SetStyle(app, 'blue')
	# 设置qt中文界面(消息框、菜单之类的默认使用中文)
	SetChinese(app)
	# 首先启动登录窗口
	if loginFirst():
		# 登录成功后启动主界面
		mw = MainWindow()
		mw.show()
		# 进入消息循环
		app.exec_()
		# 注销(清空sys_info表)
		DataHelper.sql_logout()