#include "stdafx.h"
#include "RegDialog.h"

#include <ArxHelper/HelperClass.h>
#include <Dao/DaoHelper.h>

using namespace orm;
using namespace cbm;

RegDialog::RegDialog( BOOL bModal ) : AcadSouiDialog( _T( "layout:reg" ), bModal )
{
}

RegDialog::~RegDialog()
{
}

void RegDialog::OnCommand( UINT uNotifyCode, int nID, HWND wndCtl )
{
    if( uNotifyCode == 0 )
    {
        //if(nID==6)
        //{
        //}
    }
}

LRESULT RegDialog::OnInitDialog( HWND hWnd, LPARAM lParam )
{
    AcadSouiDialog::OnInitDialog( hWnd, lParam );

    m_NameEdit = FindChildByName2<SEdit>( L"name" );
    m_ProvinceEdit = FindChildByName2<SEdit>( L"province" );
    m_CityEdit = FindChildByName2<SEdit>( L"city" );
    m_CoalNumsEdit = FindChildByName2<SEdit>( L"coal_nums" );
    m_UsernameEdit = FindChildByName2<SEdit>( L"username" );
    m_PasswordEdit = FindChildByName2<SEdit>( L"password" );
    m_BaseCombox = FindChildByName2<SComboBox>( L"base" );
    m_RegionCombox = FindChildByName2<SComboBox>( L"mine_region" );
	m_TopoGeoCombox = FindChildByName2<SComboBox>(L"topo_geo");
	m_GroundCondCheck = FindChildByName2<SCheckBox>(L"ground_cond");
	m_HydrGeoCombox = FindChildByName2<SComboBox>(L"hydr_geo");
	m_CapacityEdit = FindChildByName2<SEdit>(L"capacity");

    fillBaseCombox();

    return 0;
}

void RegDialog::OnRegButtonClick()
{
    CString user = m_UsernameEdit->GetWindowText();
    CString pwd = m_PasswordEdit->GetWindowText();

    //注册矿井账户
    int ret = DaoHelper::VerifyMineAccount( user, pwd );
    if( ret != 0 )
    {
        SMessageBox( m_hWnd, _T( "用户名已存在,请使用其他名称!" ), _T( "友情提示" ), MB_OK );
    }
    else
    {
        //新建账户
        AccountPtr account( new Account );
        account->username = user;
        account->password = pwd;

        //新建矿井
        MinePtr mine( new Mine );
        mine->name = m_NameEdit->GetWindowText();
        mine->province = m_ProvinceEdit->GetWindowText();
        mine->city = m_CityEdit->GetWindowText();
		Utils::cstring_to_double( ( LPCTSTR )m_CapacityEdit->GetWindowText(), mine->capacity );
		mine->topo_geo = m_TopoGeoCombox->GetCurSel() + 1;
		mine->hydr_geo = m_HydrGeoCombox->GetCurSel() + 1;
		mine->ground_condition = m_GroundCondCheck->IsChecked();

		//分解煤层编号(空格隔开)
		StringArray coal_nums;
		Utils::cstring_explode( ( LPCTSTR )m_CoalNumsEdit->GetWindowText(), _T( " " ), coal_nums );

        //矿井关联账户
        mine->account = account;

        //矿井关联矿区
        mine->mine_region = FIND_ONE( MineRegion, FIELD( name ), (LPCTSTR)m_RegionCombox->GetWindowText() );
        //增加到数据库并返回新增行的id值
        if( account->save() && mine->save() )
        {
            //新建煤层
            for( int i = 0; i < coal_nums.size(); i++ )
            {
                CoalPtr coal( new Coal );
                //煤层关联到矿井
                coal->mine = mine;
                //设置煤层名称
                coal->name = coal_nums[i];
                //保存到数据库
                coal->save();
            }

            SMessageBox( m_hWnd, _T( "注册矿井账户成功!" ), _T( "友情提示" ), MB_OK );
            AcadSouiDialog::OnOK();
        }
        else
        {
            SMessageBox( m_hWnd, _T( "注册矿井账户失败!" ), _T( "友情提示" ), MB_OK );
        }
    }
}

void RegDialog::OnBaseComboxSelChanged( SOUI::EventArgs* pEvt )
{
    if( !isLayoutInited() ) return;
    EventCBSelChange* pEvtOfCB = ( EventCBSelChange* )pEvt;
    if( pEvtOfCB == 0 ) return;
    int nCurSel = pEvtOfCB->nCurSel;
    if( nCurSel == -1 ) return;

    //查找当前煤炭基地对应所有的矿区
    CString base = m_BaseCombox->GetLBText( pEvtOfCB->nCurSel );
    fillRegionCombox( base );
}

void RegDialog::OnRegionComboxSelChanged( SOUI::EventArgs* pEvt )
{
    if( !isLayoutInited() ) return;
    EventCBSelChange* pEvtOfCB = ( EventCBSelChange* )pEvt;
    if( pEvtOfCB == 0 ) return;
    int nCurSel = pEvtOfCB->nCurSel;
    if( nCurSel == -1 ) return;
}

void RegDialog::OnTopoGeoComboxSelChanged(SOUI::EventArgs *pEvt)
{
	if(!isLayoutInited()) return;
	EventCBSelChange* pEvtOfCB = (EventCBSelChange*)pEvt;
	if(pEvtOfCB == 0) return;
	int nCurSel = pEvtOfCB->nCurSel;
	if(nCurSel == -1) return;

	// do something
}

void RegDialog::OnHydrGeoComboxSelChanged(SOUI::EventArgs *pEvt)
{
	if(!isLayoutInited()) return;
	EventCBSelChange* pEvtOfCB = (EventCBSelChange*)pEvt;
	if(pEvtOfCB == 0) return;
	int nCurSel = pEvtOfCB->nCurSel;
	if(nCurSel == -1) return;

	// do something
}

void RegDialog::fillBaseCombox()
{
    //查找所有的煤炭基地
    StringArray bases;
    DaoHelper::GetAllMineBases( bases );

    //清空所有的煤炭基地列表
    clearBaseCombox();
    for( int i = 0; i < bases.size(); i++ )
    {
        m_BaseCombox->InsertItem( i, bases[i], 0, 0 );
    }
    //SetCurSel会触发EVT_CB_SELCHANGE消息
    m_BaseCombox->SetCurSel( 0 );
}

void RegDialog::fillRegionCombox( const CString& base )
{
    StringArray regions;
    DaoHelper::GetAllMineRegions( base, regions );

    //清空矿区下拉列表
    clearRegionCombox();
    for( int i = 0; i < regions.size(); i++ )
    {
        m_RegionCombox->InsertItem( i, regions[i], 0, 0 );
    }
    m_RegionCombox->SetCurSel( 0 );
}

void RegDialog::clearBaseCombox()
{
    m_BaseCombox->ResetContent();
}

void RegDialog::clearRegionCombox()
{
    m_RegionCombox->ResetContent();
}