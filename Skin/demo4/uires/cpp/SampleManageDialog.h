#pragma once
#include "AcadSouiDialog.h"

class SampleManageDialog : public AcadSouiDialog
{

	/** 构造和析构函数 */
public:
	SampleManageDialog(BOOL bModal = FALSE);
	~SampleManageDialog(void);

	/** 控件消息处理 */
protected:
	void OnRegionComboxSelChanged(SOUI::EventArgs *pEvt);
	void OnTopoGeoComboxSelChanged(SOUI::EventArgs *pEvt);
	void OnHydrGeoComboxSelChanged(SOUI::EventArgs *pEvt);
	void OnDelButtonClick();
	void OnRankComboxSelChanged(SOUI::EventArgs *pEvt);
	void OnConstComplexityComboxSelChanged(SOUI::EventArgs *pEvt);
	void OnAddCoalButtonClick();
	void OnResAbundanceComboxSelChanged(SOUI::EventArgs *pEvt);
	void OnStabilityComboxSelChanged(SOUI::EventArgs *pEvt);
	void OnCoalComboxSelChanged(SOUI::EventArgs *pEvt);
	void OnSaveButtonClick();

	/** 菜单消息 */
protected:
	//处理菜单消息(菜单在一个单独的xml文件中描述，每个菜单项都有一个id号)
	void OnCommand(UINT uNotifyCode, int nID, HWND wndCtl);

	/** 窗口消息 */
protected:
	//对话框初始化过程
	LRESULT OnInitDialog(HWND hWnd, LPARAM lParam);

	//控件消息映射表
	EVENT_MAP_BEGIN()
		EVENT_NAME_HANDLER(_T("region"), EVT_CB_SELCHANGE, OnRegionComboxSelChanged)
		EVENT_NAME_HANDLER(_T("topo_geo"), EVT_CB_SELCHANGE, OnTopoGeoComboxSelChanged)
		EVENT_NAME_HANDLER(_T("hydr_geo"), EVT_CB_SELCHANGE, OnHydrGeoComboxSelChanged)
		EVENT_NAME_COMMAND(_T("del"), OnDelButtonClick)
		EVENT_NAME_HANDLER(_T("rank"), EVT_CB_SELCHANGE, OnRankComboxSelChanged)
		EVENT_NAME_HANDLER(_T("const_complexity"), EVT_CB_SELCHANGE, OnConstComplexityComboxSelChanged)
		EVENT_NAME_COMMAND(_T("add_coal"), OnAddCoalButtonClick)
		EVENT_NAME_HANDLER(_T("res_abundance"), EVT_CB_SELCHANGE, OnResAbundanceComboxSelChanged)
		EVENT_NAME_HANDLER(_T("stability"), EVT_CB_SELCHANGE, OnStabilityComboxSelChanged)
		EVENT_NAME_HANDLER(_T("coal"), EVT_CB_SELCHANGE, OnCoalComboxSelChanged)
		EVENT_NAME_COMMAND(_T("save"), OnSaveButtonClick)
		CHAIN_EVENT_MAP(AcadSouiDialog)
	EVENT_MAP_END()
	
//HOST消息(WINDOWS消息)映射表
	BEGIN_MSG_MAP_EX(SampleManageDialog)
		MSG_WM_INITDIALOG(OnInitDialog)
		MSG_WM_COMMAND(OnCommand)
		CHAIN_MSG_MAP(AcadSouiDialog)
		REFLECT_NOTIFICATIONS_EX()
	END_MSG_MAP()

protected:
	SComboBox* m_RegionCombox;
	SComboBox* m_TopoGeoCombox;
	SComboBox* m_HydrGeoCombox;
	SEdit* m_NumberEdit;
	SEdit* m_FValueEdit;
	SEdit* m_ThickEdit;
	SComboBox* m_RankCombox;
	SEdit* m_PressureEdit;
	SEdit* m_GasContentEdit;
	SEdit* m_GasPenetrationEdit;
	SComboBox* m_ConstComplexityCombox;
	SEdit* m_VarCoeffEdit;
	SEdit* m_DipAngleEdit;
	SEdit* m_CavingZoneHeightEdit;
	SComboBox* m_ResAbundanceCombox;
	SEdit* m_LayerGapEdit;
	SEdit* m_InfluenceFactorEdit;
	SEdit* m_MineIndexEdit;
	SComboBox* m_StabilityCombox;
	SComboBox* m_CoalCombox;
};