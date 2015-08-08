#include "stdafx.h"
#include "DaoManager.h"
#include <mysql/soci-mysql.h>

DaoManagerPrt DaoManager::instance;

bool DaoManager::Configure(const CString& url, const CString& user, const CString& password, const CString& database)
{
	bool ret = true;
	try
	{
		if( ! instance ) {
			if(!url.IsEmpty() && !user.IsEmpty()) {
				instance.reset(new DaoManager(url, user, password, database));
				//���mysql������������
				instance->executeQuery(_T("set names 'gbk';"));
				//instance->executeQuery("set character_set_client=utf8;");
				//instance->executeQuery("set character_set_results=utf8;");
				//instance->executeQuery("set character_set_connection=utf8;");
			}
			else {
				throw std::runtime_error("Passe a URL, Usuario e Senha na primeira vez que chamar: Dao::getInstance");
			}
		}
	}
	catch(soci::soci_error const & e)
	{
		ret = false;
		instance.reset();
		LOG_DEBUG_FMT(_T("�������ݿ��쳣:%s"), EncodeHelper::ANSIToUnicode(e.what()).c_str());
	}
	catch (std::exception const & e)
	{
		ret = false;
		instance.reset();
		LOG_DEBUG_FMT(_T("Runtime�쳣:%s"), EncodeHelper::ANSIToUnicode(e.what()).c_str());
	}
	return ret;
}

DaoManagerPrt DaoManager::GetInstance()
{
	return instance;
}

DaoManager::DaoManager(const CString& host, const CString& user, const CString& password, const CString& database)
{
	std::string c_host = EncodeHelper::UnicodeToANSI((LPCTSTR)host);
	std::string c_user = EncodeHelper::UnicodeToANSI((LPCTSTR)user);
	std::string c_password = EncodeHelper::UnicodeToANSI((LPCTSTR)password);
	std::string c_database = EncodeHelper::UnicodeToANSI((LPCTSTR)database);

	sql.open(soci::mysql, "host="+c_host+" db="+c_database+" user="+c_user+" password=\'"+c_password+"\'");
}

DaoManager::~DaoManager()
{
}

soci::session* DaoManager::getConnection()
{
    return &sql;
}

ResultSet DaoManager::executeQuery(const CString &sql)
{
	soci::session* connection = getConnection();
	//ִ��һ��ʲôҲ�ò�����sql���(ǰ��cbm_dummy��������!!!)
	//�����������д���!!!
    ResultSet rs = (connection->prepare << "select * from cbm_dummy where 0");
    try
    {
		LOG_DEBUG_FMT(_T("sql���:%s"), sql);
		ResultSet temp_rs = (connection->prepare << EncodeHelper::UnicodeToANSI((LPCTSTR)sql));
        rs = temp_rs;
    }
    catch(soci::soci_error const & e)
    {
		LOG_DEBUG_FMT(_T("����executeQuery()�쳣:%s"), EncodeHelper::ANSIToUnicode(e.what()).c_str());
    }
	catch (std::exception const & e)
	{
		LOG_DEBUG_FMT(_T("Runtime�쳣:%s"), EncodeHelper::ANSIToUnicode(e.what()).c_str());
	}
    return rs;
}

bool DaoManager::executeUpdate(const CString& sql)
{
	bool ret = true;
    try
    {
		LOG_DEBUG_FMT(_T("sql���:%s"), sql);
        soci::session* connection = getConnection();

		*connection << EncodeHelper::UnicodeToANSI((LPCTSTR)sql);
        connection->commit();
    }
    catch(soci::soci_error const & e)
    {
		ret = false;
		LOG_DEBUG_FMT(_T("����executeUpdate()�쳣:%s"), EncodeHelper::ANSIToUnicode(e.what()).c_str());
    }
	catch (std::exception const & e)
	{
		ret = false;
		LOG_DEBUG_FMT(_T("Runtime�쳣:%s"), EncodeHelper::ANSIToUnicode(e.what()).c_str());
	}
	return ret;
}

DaoManagerPrt dao()
{
	return DaoManager::GetInstance();
}