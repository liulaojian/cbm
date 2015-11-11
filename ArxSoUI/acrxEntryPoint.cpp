#include "StdAfx.h"
#include "resource.h"
#include "CmdHelper.h"

#include <ArxHelper/HelperClass.h>

// 定义注册服务名称
#ifndef ARX_SOUI_SERVICE_NAME
#define ARX_SOUI_SERVICE_NAME _T("ARXSOUI_SERVICE_NAME")
#endif

//-----------------------------------------------------------------------------
//----- ObjectARX EntryPoint
class CArxSoUIApp : public AcRxArxApp
{

public:
    CArxSoUIApp () : AcRxArxApp () {}

    virtual AcRx::AppRetCode On_kInitAppMsg ( void* pkt )
    {
        // TODO: Load dependencies here

        // You *must* call On_kInitAppMsg here
        AcRx::AppRetCode retCode = AcRxArxApp::On_kInitAppMsg ( pkt ) ;

        acrxRegisterService( ARX_SOUI_SERVICE_NAME );

        acutPrintf( _T( "\nArxSoUI::On_kInitAppMsg\n" ) );

        AfxEnableControlContainer();
        AfxInitRichEdit2();

        //初始化log4cplus日志系统
        //为了保证日志功能正常使用，在加载所有模块之前初始化日志系统
        log_init( _T( ".\\log\\log4cplus.properties" ) );

        LOG_TRACE( _T( "ArxSoUI::On_kInitAppMsg" ) );

        return ( retCode ) ;
    }

    virtual AcRx::AppRetCode On_kUnloadAppMsg ( void* pkt )
    {
        // TODO: Add your code here

        // You *must* call On_kUnloadAppMsg here
        AcRx::AppRetCode retCode = AcRxArxApp::On_kUnloadAppMsg ( pkt ) ;

        delete acrxServiceDictionary->remove( ARX_SOUI_SERVICE_NAME );

        acutPrintf( _T( "\nArxSoUI::On_kUnloadAppMsg\n" ) );
        LOG_TRACE( _T( "ArxSoUI::On_kUnloadAppMsg" ) );

        //关闭log4cplus日志系统
        log_uinit();

        return ( retCode ) ;
    }

    virtual AcRx::AppRetCode On_kLoadDwgMsg( void* pkt )
    {
        AcRx::AppRetCode retCode = AcRxArxApp::On_kLoadDwgMsg ( pkt );

        acutPrintf( _T( "\nArxSoUI::On_kLoadDwgMsg\n" ) );

        ArxDataTool::RegAppName( acdbHostApplicationServices()->workingDatabase(), _T( "扩展数据" ) );

        return retCode;
    }

    virtual AcRx::AppRetCode On_kUnloadDwgMsg( void* pkt )
    {
        AcRx::AppRetCode retCode = AcRxArxApp::On_kUnloadDwgMsg( pkt ) ;

        acutPrintf( _T( "\nArxSoUI::On_kUnloadDwgMsg\n" ) );

        return retCode;
    }

    virtual void RegisterServerComponents ()
    {
    }

	static void JL_xxx()
	{
		//UIHelper::testdlg();
		CmdHelper::xxx();
	}

	static void JL_PostJsonDatas()
	{
		CmdHelper::PostJsonDatasToRpc();
	}
} ;

//-----------------------------------------------------------------------------
IMPLEMENT_ARX_ENTRYPOINT( CArxSoUIApp )
ACED_ARXCOMMAND_ENTRY_AUTO( CArxSoUIApp, JL, _xxx, xxx, ACRX_CMD_TRANSPARENT, NULL )
ACED_ARXCOMMAND_ENTRY_AUTO( CArxSoUIApp, JL, _PostJsonDatas, PostJsonDatas, ACRX_CMD_TRANSPARENT, NULL )
