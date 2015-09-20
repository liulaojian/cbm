#pragma once

#include "dlimexp.h"
#include "Entity.h"

#include <vector>
typedef std::vector<CString> StringArray;
typedef std::vector<int> IntArray;
typedef std::vector<double> DoubleArray;

class DAO_DLLIMPEXP DaoHelper
{
public:
	//从配置文件中读取数据库信息并连接数据库
    static bool ConfigureFromFile( const CString& cfgFile );
	//连接数据库
    static bool ConfigureDao( const CString& username, const CString& password, const CString& database, const CString& host = _T( "localhost" ), const CString& port = _T( "3306" ) );
	//测试dao功能
    static void TestDao();

    //初始化示范矿区(虚拟的矿井和煤层)
    static void InitSampleRegion();
    //查询已登录用户的id
    static int GetOnlineAccountId();
    //获取已登录用户的矿井数据
    static cbm::MinePtr GetOnlineMine();
    //验证用户名和密码
    static int VerifyMineAccount( const CString& username, const CString& pwd );
    //查询所有的基地
    static void GetAllMineBases( StringArray& bases );
    //查询基地所有的矿区
    static void GetAllMineRegions( const CString& baseName, StringArray& regions );
    //根据矿区反查基地
    static CString GetBaseByRegion( const CString& regionName );
    //查询示范矿区的虚拟矿井
    static cbm::MinePtr GetSampleMine( const CString& regionName );
    //查询示范矿区的虚拟煤层
    static cbm::CoalPtr GetSampleCoal( const CString& regionName );
    //查询矿井所有的煤层名称
    static void GetCoalNames( int mine_id, StringArray& coals );
    //查询矿井所有的煤层id
    static void GetCoalIds( int mine_id, IntArray& coals );
    //查询矿井所有的采区
    static orm::RecordPtrListPtr GetWorkAreas( int mine_id );
    //查询矿井所有的工作面
    static orm::RecordPtrListPtr GetWorkSurfs( int mine_id );
    //查询矿井所有的掘进面
    static orm::RecordPtrListPtr GetDrillingSurfs( int mine_id );

    //抽采难易程度评价
    static int DifficultEval( cbm::CoalPtr coal );
    static CString DifficultEvalString( cbm::CoalPtr coal );
    //可采煤层瓦斯涌出量计算W1
    static double MineGasReservesW1( int mine_id );
    //不可采煤层瓦斯涌出量计算W2
    static double MineGasReservesW2( int mine_id );
    //计算采区的瓦斯涌出量
    static double WorkAreaGasFlow( cbm::WorkAreaPtr work_area, double K1 );
    //计算矿井的瓦斯涌出量
    static double MineGasFlow( cbm::MinePtr mine );
    //工作面开采层瓦斯涌出量
    static double WorkSurfGasFlow1( cbm::CoalPtr coal, cbm::WorkAreaPtr work_area, cbm::WorkSurfPtr work_surf );
    //工作面邻近层瓦斯涌出量
    static double WorkSurfGasFlow2( cbm::CoalPtr coal, cbm::WorkAreaPtr work_area, cbm::WorkSurfPtr work_surf );
    //掘进面瓦斯涌出量
    static void DrillingSurfGasFlow( cbm::CoalPtr coal, cbm::DrillingSurfPtr drilling_surf, cbm::TunnelPtr tunnel );
};
