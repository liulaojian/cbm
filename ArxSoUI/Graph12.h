#pragma once

#include "Data.h"
#include "Graph.h"

#include <ArxHelper/HelperClass.h>
#include <ArxDao/DaoHelper.h>
#include <ArxDao/Entity.h>
using namespace orm;
using namespace cbm;

namespace P12
{

	//����ͼ���ƻ���
	class Graph : public BaseGraph
	{
	protected:
		//�������
		virtual void drawPores() = 0;
		//�������
		virtual void drawTunnel() = 0;
		//����ú��
		virtual void drawCoal() = 0;

	protected:
		//���캯��
		Graph(const cbm::CoalPtr& coal, const cbm::DesignDrillingSurfTechnologyPtr& tech);
		//ִ�о���Ļ�ͼ����(����ú�㡢������������곡����׵ȵ�)
		virtual void subDraw();

		/** �������㷽��. */
	protected:
		//����ú��ĳߴ�(��-����, ��-����, ��-���)
		void caclCoalExtent(double& Lc, double& Wc, double& Hc) const;

		/** ����ͻ�ͼ�õ��Ĳ���. */
	protected:
		//���򳤶Ⱥ����򳤶�
		double L1, L2;
		//ú���Ⱥ����(����)
		double thick, angle;
		//����������Ŀ��Ⱥ͸߶�
		double w, h;
		//�������°��
		double left, right, top, bottom;
		//��װ뾶����׵׼�ࡢ��׳�ǰ���롢�����������
		double radius, pore_gap, L_stripe, leading;

		//�������ұ߾�(�����ڻ�ͼ����,������ʵ�ʼ���)
		double left_margin, right_margin, top_margin, bottom_margin;

		/** ��������������Ǵ���3������ָ������ȡ������. */
	protected:
		cbm::CoalPtr coal;                 // ú��ָ��
		cbm::DesignDrillingSurfTechnologyPtr tech;     // ��Ƴ�ɼ�������ָ��

	}; // class Graph

	//ƽ��ͼ
	//�Ծ����������Ϊԭ��,���������Ϊx�������򣬴�ֱ���ϵķ���Ϊy��������
	class PlanGraph : public Graph
	{
	public:
		PlanGraph(const cbm::CoalPtr& coal, const cbm::DesignDrillingSurfTechnologyPtr& tech);

	protected:
		//�������
		virtual void drawPores();
		//�������
		virtual void drawTunnel();
		//����ú��
		virtual void drawCoal();

	}; // class PlanGraph

} // namespace P12