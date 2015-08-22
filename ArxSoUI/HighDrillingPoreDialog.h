#pragma once
#include "AcadSouiDialog.h"

class HighDrillingPoreDialog : public AcadSouiDialog
{

	/** 构造和析构函数 */
public:
	HighDrillingPoreDialog(BOOL bModal = FALSE);
	~HighDrillingPoreDialog(void);

	/** 控件消息处理 */
protected:
	void OnSaveButtonClick();
	void OnCaclButtonClick();

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
		EVENT_NAME_COMMAND(_T("save"), OnSaveButtonClick)
		EVENT_NAME_COMMAND(_T("cacl"), OnCaclButtonClick)
		CHAIN_EVENT_MAP(AcadSouiDialog)
	EVENT_MAP_END()
	
//HOST消息(WINDOWS消息)映射表
	BEGIN_MSG_MAP_EX(HighDrillingPoreDialog)
		MSG_WM_INITDIALOG(OnInitDialog)
		MSG_WM_COMMAND(OnCommand)
		CHAIN_MSG_MAP(AcadSouiDialog)
		REFLECT_NOTIFICATIONS_EX()
	END_MSG_MAP()

protected:
	SEdit* m_LkEdit;
	SEdit* m_LcEdit;
	SEdit* m_LwEdit;
	SEdit* m_N2Edit;
	SEdit* m_BetaEdit;
	SEdit* m_LdEdit;
	SEdit* m_N1Edit;

public:
	double Lg;
	int ws_id; // 工作面id(外部传入)

private:
	void initDatas();
	void fillDatas();
};
