#pragma once

/*
 * ��ɾ��һ��ͼԪ��Ҫͬʱɾ��ͼԪ�ϵı�ǩͼԪTagGE
 * �Լ�������ģ��ͼԪModelGE
 */
class MineGEDatabaseReactor : public AcDbDatabaseReactor 
{
protected:
	AcDbDatabase *mpDatabase ;

public:
	MineGEDatabaseReactor (AcDbDatabase *pDb =NULL) ;
	virtual ~MineGEDatabaseReactor () ;

	virtual void Attach (AcDbDatabase *pDb) ;
	virtual void Detach () ;
	virtual AcDbDatabase *Subject () const ;
	virtual bool IsAttached () const ;

	virtual void objectAppended(const AcDbDatabase* db, const AcDbObject* pObj);

	/*
	 * �����ݶ����ں�̨���ı䣬ǿ�Ƹ�����֮������ͼ��Ч��
	 * ��ЩͼԪ�Ŀ��ӻ�Ч���������йأ�������վ(Joint)
	 */
	virtual void objectModified(const AcDbDatabase* dwg, const AcDbObject* dbObj);

	/*
	 * ��ͼԪ��ɾ����ͬʱҲӦɾ��ͼԪ�����ı�ǩͼԪ(TagGE)
	 */
	virtual void objectErased(const AcDbDatabase * dwg, const AcDbObject * dbObj, Adesk::Boolean pErased);
} ;