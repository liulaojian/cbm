#include "StdAfx.h"
#include "SystemHelper.h"
#include "HelperClass.h"
#include "config.h"

void SystemHelper::Start()
{
    // 注册dictionary和regAppName
    ArxDictTool::RegDict( PROPERTY_DATA_FIELD_DICT );
    ArxDictTool::RegDict( PROPERTY_DATA_FIELD_INFO_DICT );
    ArxDictTool::RegDict( FUNC_FIELD_DICT );

    //ArxDataTool::RegAppName( acdbHostApplicationServices()->workingDatabase(), DRAW_PARAMS_XDATA_GROUP );

    //创建标注样式
    ArxDrawHelper::CreateDimStyle( DIM_STYLE_NAME, false );
}

void SystemHelper::ShutDown()
{

}
