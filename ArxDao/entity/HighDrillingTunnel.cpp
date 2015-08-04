#include "stdafx.h"
#include "HighDrillingTunnel.h"
#include "WorkSurf.h"

#include <sstream>
#include "../dao/util.h"

namespace cbm {

HighDrillingTunnel::HighDrillingTunnel()
{
	high_drilling_tunnel_id = 0;
	hdt_k = 0.0;
	hdt_rock = 0;
	hdt_hz_min = 0.0;
	hdt_hz_max = 0.0;
	comment = "NULL";
}

HighDrillingTunnel::HighDrillingTunnel(long id)
{
	high_drilling_tunnel_id = id;
	hdt_k = 0.0;
	hdt_rock = 0;
	hdt_hz_min = 0.0;
	hdt_hz_max = 0.0;
	comment = "NULL";
}

HighDrillingTunnel::HighDrillingTunnel(soci::row &rs)
{
	high_drilling_tunnel_id = rs.get<long>(0);
	long work_surf_id = rs.get<long>(1);
	if(work_surf_id > -1) {
		work_surf = WorkSurfPtr(new WorkSurf(work_surf_id));
	}
	hdt_k = rs.get<double>(2);
	hdt_rock = rs.get<long>(3);
	hdt_hz_min = rs.get<double>(4);
	hdt_hz_max = rs.get<double>(5);
	comment = rs.get<std::string>(6);
}

std::string HighDrillingTunnel::getTableName() const
{
	return "cbm_high_drilling_tunnel";
}

std::string HighDrillingTunnel::getSqlInsert() const
{
	std::stringstream sql;
	sql <<"insert into cbm_high_drilling_tunnel values("
		<<"NULL"<<","
		<<work_surf->getId()<<","
		<<hdt_k<<","
		<<hdt_rock<<","
		<<hdt_hz_min<<","
		<<hdt_hz_max<<","
		<<"'"<<comment<<"'"<<");";
	return sql.str();
}

std::string HighDrillingTunnel::getSqlUpdate() const
{
	std::stringstream sql;
	sql <<"update cbm_high_drilling_tunnel set"
		<<" work_surf_id="<<work_surf->getId()<<","
		<<" hdt_k="<<hdt_k<<","
		<<" hdt_rock="<<hdt_rock<<","
		<<" hdt_hz_min="<<hdt_hz_min<<","
		<<" hdt_hz_max="<<hdt_hz_max<<","
		<<" comment="<<"'"<<comment<<"'"
		<<" where high_drilling_tunnel_id="<<high_drilling_tunnel_id
		<<" ;";
	return sql.str();
}

std::string HighDrillingTunnel::getSqlDelete() const
{
	std::stringstream sql;
	sql <<"delete from cbm_high_drilling_tunnel"
		<<" where high_drilling_tunnel_id="<<high_drilling_tunnel_id
		<<" ;";
	return sql.str();
}

long HighDrillingTunnel::getId() const
{
	return high_drilling_tunnel_id;
}

void HighDrillingTunnel::setId(const long& value)
{
	this->high_drilling_tunnel_id = value;
}

WorkSurfPtr HighDrillingTunnel::getWorkSurf() const
{
	return work_surf;
}

void HighDrillingTunnel::setWorkSurf(const WorkSurfPtr& value)
{
	this->work_surf = value;
}

double HighDrillingTunnel::getHdtK() const
{
	return hdt_k;
}

void HighDrillingTunnel::setHdtK(const double& value)
{
	this->hdt_k = value;
}

long HighDrillingTunnel::getHdtRock() const
{
	return hdt_rock;
}

void HighDrillingTunnel::setHdtRock(const long& value)
{
	this->hdt_rock = value;
}

double HighDrillingTunnel::getHdtHzMin() const
{
	return hdt_hz_min;
}

void HighDrillingTunnel::setHdtHzMin(const double& value)
{
	this->hdt_hz_min = value;
}

double HighDrillingTunnel::getHdtHzMax() const
{
	return hdt_hz_max;
}

void HighDrillingTunnel::setHdtHzMax(const double& value)
{
	this->hdt_hz_max = value;
}

std::string HighDrillingTunnel::getComment() const
{
	return comment;
}

void HighDrillingTunnel::setComment(const std::string& value)
{
	this->comment = value;
}

} // namespace cbm
