#include "stdafx.h"
#include "DaoManager.h"
DaoManagerPrt DaoManager::instance;

#include <stactive_record.h>
using namespace stactiverecord;
Sar_Dbi* Sar_Dbi::dbi = 0;

#include <Util/HelperClass.h>

bool DaoManager::config(const CString& host, const CString& user, const CString& password, const CString& database)
{
	bool ret = true;
	try
	{
		// config is in form scheme://[user[:password]@]host[:port]/database
		CString config;
		config.AppendFormat(_T("mysql://%s"), user);
		if(password.GetLength() > 0)
		{
			config.AppendFormat(_T(":%s"), password);
		}
		config.AppendFormat(_T("@%s"), host);
		
		CString port;
		if(port.GetLength() > 0)
		{
			config.AppendFormat(_T(":%s"), port);
		}
		config.AppendFormat(_T("/%s"), database);
		Sar_Dbi::dbi =  Sar_Dbi::dbi = Sar_Dbi::makeStorage( (LPCTSTR)config, SAR_TEXT("cbm_") );

		//���mysql������������
		Sar_Dbi::dbi->execute(_T("set names 'gbk';"));
		//Sar_Dbi::dbi->execute("set character_set_client=utf8;");
		//Sar_Dbi::dbi->execute("set character_set_results=utf8;");
		//Sar_Dbi::dbi->execute("set character_set_connection=utf8;");
	}
	catch (std::exception const & e)
	{
		ret = false;
		LOG_DEBUG_FMT(_T("�쳣:%s"), EncodeHelper::ANSIToUnicode(e.what()).c_str());
	}
	return ret;
}

DaoManagerPrt DaoManager::Instance()
{
	if( ! instance ) 
	{
		instance = new DaoManager();
	}
	return instance;
}

DaoManager::DaoManager()
{
	//Ϊ�˸��õ�������ģ���Ҫ����localeΪ����
	//log4cplusҲ����������,����������ú�log4cplus�������غ���
	//��vvloader�Ѿ��޸Ĺ�locale��,�����ظ�����
	//std::locale m_origin_locale = std::locale::global(std::locale("chs"));
}

DaoManager::~DaoManager()
{
	//�ָ�ԭ����locale����
	//std::locale::global(m_origin_locale);

	delete Sar_Dbi::dbi;
	Sar_Dbi::dbi = 0;
}
