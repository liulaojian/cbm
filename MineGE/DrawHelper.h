#pragma once

#include "dlimexp.h"

class MineGE;

/*
	��ɫ��
-----------------
1	|	Red		|
-----------------
2	|	Yellow	|
-----------------
3	|	Green	|
-----------------
4	|	Cyan	|
-----------------
5	|	Blue	|
-----------------
6	|	Magenta	|
-----------------
7	|White/Black|
-----------------
*/

// ���ӻ�Ч��������
class MINEGE_DLLIMPEXP DrawHelper
{
public:	
	// LinkedGE����ͼԪ�պϴ���
	static void LinkedGEJunctionClosure(const AcGePoint3d& junctionPt);

	// LinkedGE����ͼԪ�պϴ���
	static void LinkedGEJunctionClosure2(const AcDbObjectId& objId);

	// ��֧��ͼԪ����
	// ����������������ͼԪ��ʼĩ��λ��
	// ͬʱ��������ķ�����ͼԪ,����������򣬷��ŵ�
	static void ReverseDirection( const AcDbObjectId& objId );

	// ��ȡ��ǰ�Ŀ��ӻ�Ч��
	static bool GetCurrentDraw(const CString& type, CString& draw);

	// �л�����geTypeͼԪ����ʾЧ��
	static void SwitchDraw(const CString& geType, const CString& drawName);

	// ����ͼԪ�ĸ��Ӳ���
	// ��������ͼ��Ч��
	static void ConfigDraw(const CString& geType, const CString& drawName);

	// �ж�ͼԪ����geType��ǰ����Ч���Ƿ�ʵ����jig����
	static bool IsGETypeHasDrawJig(const CString& geType);

	// ��ȡ��ǰ��ע���MineGEͼԪ����(����draw�Ĳ�������)
	static void GetAllRegGETypesForDraw(AcStringArray& allGETypes);

	// ����ָ������geType������ͼԪ
	static void FindMineGEs(const CString& geType, AcDbObjectIdArray& objIds);

	// ����ͼԪ�����й����ı�ǩͼԪ
	static void GetAllTagGEById(const AcDbObjectId& objId, AcDbObjectIdArray& objIds);

	// ������ͼԪobjId������ָ�����͵ı�ǩͼԪ(������geType������ͼԪ����)
	static void GetTagGEById2(const AcDbObjectId& objId, const CString& geType, AcDbObjectIdArray& objIds);

	// ������objIds���������е�����ͼԪ
	static void GetHosts(const AcDbObjectIdArray& objIds, AcDbObjectIdArray& hosts);

	// ����������objIdΪ������ģ��ͼԪModelGE
	static void GetModelGEById(const AcDbObjectId& objId, AcDbObjectIdArray& objIds);

	// ��һ����ɫ��ʾͼԪ�����б�ǩͼԪ
	static void ShowAllTagGE(const AcDbObjectId& objId, unsigned short colorIndex);

	// ��һ����ɫ��ʾ������ʾĳ��ͼԪ
	static void HighLightShowGE(const AcDbObjectId& objId, unsigned short colorIndex);

	// ��һ����ɫ��ʾ��ǩͼԪ������������ͼԪHostGE
	static void ShowHostGE(const AcDbObjectId& objId, unsigned short colorIndex);

	static bool GetHostGE(const AcDbObjectId& objId, AcDbObjectId& host);

	static AcDbObjectId GetRelatedTW(AcDbObjectId objId);

	static AcDbObjectIdArray GetRelatedTunnel(AcDbObjectId tunnelId);
};