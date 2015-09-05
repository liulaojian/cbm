#include "stdafx.h"
#include "SouiListHelper.h"
#include "GasDesignDialog.h"
#include "GasDesignQuestionDialog.h"
#include "GasDesignP11Dialog.h"
#include "GasDesignP12Dialog.h"

#include <ArxHelper/HelperClass.h>
#include <ArxDao/DaoHelper.h>
#include <ArxDao/Entity.h>
using namespace orm;
using namespace cbm;

GasDesignDialog::GasDesignDialog(BOOL bModal) : AcadSouiDialog(_T("layout:gas_design"), bModal)
{
}

GasDesignDialog::~GasDesignDialog()
{
}

void GasDesignDialog::OnCommand( UINT uNotifyCode, int nID, HWND wndCtl )
{
	if(uNotifyCode==0)
	{
		//if(nID==6)
		//{
		//}
	}
}

LRESULT GasDesignDialog::OnInitDialog( HWND hWnd, LPARAM lParam )
{
	AcadSouiDialog::OnInitDialog(hWnd, lParam);
	//do something
	m_CoalCombox = FindChildByName2<SComboBox>(L"coal");
	m_ThickEdit = FindChildByName2<SEdit>(L"thick");
	m_DipAngleEdit = FindChildByName2<SEdit>(L"dip_angle");

	fillCoalCombox();

	return 0;
}


void GasDesignDialog::OnCoalComboxSelChanged(SOUI::EventArgs *pEvt)
{
	if(!isLayoutInited()) return;
	EventCBSelChange* pEvtOfCB = (EventCBSelChange*)pEvt;
	if(pEvtOfCB == 0) return;
	int nCurSel = pEvtOfCB->nCurSel;
	if(nCurSel == -1) return;

	// do something
	int coal_id = SComboBoxHelper::GetCurSelItemID( m_CoalCombox );
	if( coal_id == 0 ) return;
	CoalPtr coal = FIND_BY_ID( Coal, coal_id );
	if( coal == 0 ) return;

	//填充煤层数据
	m_ThickEdit->SetWindowText( Utils::double_to_cstring( coal->thick ) );
	m_DipAngleEdit->SetWindowText( Utils::double_to_cstring( coal->dip_angle ) );
}

void GasDesignDialog::OnTwsDesignButtonClick()
{
	GasDesignQuestionDialog dlg(true);
	dlg.region = 1;
	dlg.Run(GetSafeHwnd());
	int tech = dlg.tech;
	if(tech == 0) return;
	
	int coal_id = SComboBoxHelper::GetCurSelItemID( m_CoalCombox );
	if( coal_id == 0 )
	{
		SMessageBox( GetSafeHwnd(), _T( "请选择一个【煤层】进行抽采设计!!!" ), _T( "友情提示" ), MB_OK );
		return;
	}

	AcadSouiDialog::OnOK();
	if(tech == 1)
	{
		GasDesignP11Dialog* dlg = new GasDesignP11Dialog( FALSE );
		dlg->coal_id = coal_id;
		dlg->region = 1;
		dlg->Run( acedGetAcadFrame()->GetSafeHwnd() );
	}
	else if(tech == 2)
	{
		GasDesignP12Dialog* dlg = new GasDesignP12Dialog( FALSE );
		dlg->coal_id = coal_id;
		dlg->region = 1;
		dlg->Run( acedGetAcadFrame()->GetSafeHwnd() );
	}
	else
	{

	}
}

void GasDesignDialog::OnWsDesignButtonClick()
{
}

void GasDesignDialog::OnGoafDesignButtonClick()
{
}

void GasDesignDialog::OnSaveButtonClick()
{
	int coal_id = SComboBoxHelper::GetCurSelItemID( m_CoalCombox );
	if( coal_id == 0 ) return;
	CoalPtr coal = FIND_BY_ID( Coal, coal_id );
	if( coal == 0 ) return;

	//保存煤层数据
	Utils::cstring_to_double((LPCTSTR)m_ThickEdit->GetWindowText(), coal->thick);
	Utils::cstring_to_double((LPCTSTR)m_DipAngleEdit->GetWindowText(), coal->dip_angle);
	if( coal->save() )
	{
		SMessageBox( GetSafeHwnd(), _T( "更新成功!" ), _T( "友情提示" ), MB_OK );
	}
	else
	{
		SMessageBox( GetSafeHwnd(), _T( "更新失败!" ), _T( "友情提示" ), MB_OK );
	}
}

void GasDesignDialog::OnDestroyWindow()
{
	//删除所有的附加数据
	SComboBoxHelper::Clear( m_CoalCombox );
	AcadSouiDialog::OnDestroyWindow();
}

void GasDesignDialog::fillCoalCombox()
{
	MinePtr mine = FIND_BY_ID( Mine, mine_id );
	if( mine == 0 ) return;

	StringArray coal_names;
	IntArray coal_ids;
	DaoHelper::GetCoalIds( mine->getID(), coal_ids );
	DaoHelper::GetCoalNames( mine->getID(), coal_names );

	SComboBoxHelper::Clear( m_CoalCombox );
	SComboBoxHelper::Append( m_CoalCombox, coal_names, coal_ids );
	SComboBoxHelper::Select( m_CoalCombox, 0 );
}