#include "storm.h"

#include <assert.h>

using namespace std;

namespace ORM{

Query::Query() :
	n_limit(0),
	query_type(0),
	currupted(false){
}
Query::~Query(){
}

void Query::set_with_no_dirt(const string &key, const string &value){
	fields[key] = value;
}
void Query::set_connection_object(MYSQL *_mysql){
	mysql = _mysql;
}

void Query::set_query_type(int _query_type){
	query_type = _query_type;
}
void Query::set_table(const string &_table){
	table = _table;
}
void Query::set_limit(int _limit){
	n_limit = _limit;
}

void Query::add_result_column(const string &col){
	results.push_back( col );
}
void Query::add_condition(
	const string &col, const string &op, const string &value){

	conditions.push_back(
		col + " " + op + " \'" +
		escape(value) + "\'" );
}
void Query::add_condition(const string &query){
	conditions.push_back( query );
}
void Query::add_order_by(const string &col, const string &order){
	order_by.push_back(
		col + " " + order );
}
void Query::add_group_by(const string &col){
	group_by.push_back( col );
}

int Query::query(const std::string &query){
	assert( currupted == false );

	int result = mysql_query(
		mysql, query.c_str() );

	currupted = true;

	return result;
}
MYSQL_RES *Query::store_result(){
	MYSQL_RES *result = 
		mysql_store_result( mysql );

	return result;
}
void Query::free_result(MYSQL_RES *mysql){
	mysql_free_result( mysql );
}
vector<string> Query::fetch_fields(MYSQL_RES *result){
	vector<string> fields;
	int n_field =
		mysql_num_fields( result );

	for(int i=0;i<n_field;i++) {
		MYSQL_FIELD *field =
			mysql_fetch_field( result );
		
		fields.push_back(
			field->name );
	}

	return fields;
}
vector<MYSQL_ROW> Query::fetch_rows(MYSQL_RES *result){
	vector<MYSQL_ROW> rows;
	int n_row =
		mysql_num_rows( result );
	
	for(int i=0;i<n_row;i++) {
		MYSQL_ROW row = 
			fetch_next_row( result );

		rows.push_back( row );
	}

	return rows;
}
MYSQL_ROW Query::fetch_next_row(MYSQL_RES *result){
	MYSQL_ROW row =
		mysql_fetch_row( result );
	
	return row;
}

void Query::dirt_field(const string &field_name){
	dirty_fields.push_back( field_name );
}
void Query::clean_dirty_fields(){
	dirty_fields.clear();
}

string Query::find_single_value(){
	string sql = build_select();

	if( query( sql ))
		return "";

	MYSQL_RES *result = store_result();
	if( result == NULL )
		return "";

	MYSQL_ROW row =
		fetch_next_row( result );
	if( row == NULL )
		return "";
	
	mysql_free_result( result );

	return row[0];
}
Query *Query::find_single_record(){
	string sql = build_select();

	if( query( sql ))
		return NULL;

	MYSQL_RES *result = store_result();
	if( result == NULL )
		return NULL;

	MYSQL_ROW row =
		fetch_next_row( result );
	if( row == NULL )
		return NULL;

	ORM::Query *obj = ORM::from( table );
	vector<string> fields =
		fetch_fields( result );

	for(int i=0;i<fields.size();i++)
		obj->set_with_no_dirt( fields[i], row[i] );

	/* then, in order to identify the record. */
	obj->where("id", obj->get("id") );
	obj->set_query_type(
		QueryType::eUPDATE );
	
	mysql_free_result( result );

	return obj;
}
vector<Query*> Query::find_records(){
	vector<Query*> results;
	string sql = build_select();

	if( query( sql ))
		return results;

	MYSQL_RES *result = store_result();
	if( result == NULL )
		return results;

	vector<string> fields = fetch_fields( result );
	vector<MYSQL_ROW> rows = fetch_rows( result );

	for(int i=0;i<rows.size();i++){
		ORM::Query *obj = ORM::from( table );

		for(int j=0;j<fields.size();j++)
			obj->set_with_no_dirt( fields[j], rows[i][j] );

		/* then, in order to identify the record. */
		obj->where("id", obj->get("id") );
		obj->set_query_type(
			QueryType::eUPDATE );

		results.push_back( obj );
	}
	
	mysql_free_result( result );

	return results;
}
bool Query::update_records(){
	string sql = build_update();

	if( query( sql ))
		return false;
	return true;
}
bool Query::insert_record(){
	string sql = build_insert();

	if( query( sql ))
		return false;
	return true;
}
bool Query::remove_records(){
	string sql = build_delete();

	if( query( sql ))
		return false;
	return true;
}

}
