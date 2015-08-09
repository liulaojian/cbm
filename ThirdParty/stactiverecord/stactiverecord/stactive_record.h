/** \mainpage StactiveRecord :: (Static) ActiveRecord for C++
    \section desc Description
    The goal of the project is to create an implementation of the Active Record pattern for C++

    \section Resources
    \li The source, docs, and more info can be found at http://findingscience.com/StactiveRecord
    \li Bug reporting can be found at http://github.com/bmuller/StactiveRecord/issues
    \section Author
    Brian Muller <bmuller@butterfat.net>
*/

#pragma once

#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <exception>
#include <time.h>

/// \namespace stactiverecord The project's namespace
namespace stactiverecord
{
    /**
     * \enum coltype The possible valid column types. Note that a change here means
     * editing coltype_to_name in utils too.
     * \enum wheretype The possible specific types/relationships a Where class can represent.
     */
    enum coltype { NONE, INTEGER, STRING, RECORD, DATETIME, ALL };
    enum wheretype { STARTSWITH, ENDSWITH, CONTAINS, GREATERTHAN, LESSTHAN, BETWEEN, EQUALS, OBJECTRELATION, ISIN, ISNULL };

    // Forward declaration of class Record
    template <class T> class Record;
};

#include "config.h"
#include "tstring.h"
#include "datetime.h"
#include "where.h"
#include "utils.h"
#include "types.h"
#include "cud_property_register.h"
#include "exception.h"
#include "query.h"
#include "storage.h"
#include "record.h"

#define VALUE_MAX_SIZE 255
#define VALUE_MAX_SIZE_S "255"

#define SAR_INIT() static tstring classname;
#define SAR_SET_CLASSNAME(c, n) tstring c::classname = n;
