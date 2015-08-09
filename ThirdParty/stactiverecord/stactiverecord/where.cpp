/*
Copyright (C) 2007 Butterfat, LLC (http://butterfat.net)

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

Created by bmuller <bmuller@butterfat.net>
*/

#include "stactive_record.h"

namespace stactiverecord
{

    Where* startswith( tstring value )
    {
        return new Where( value, STARTSWITH );
    };

    Where* endswith( tstring value )
    {
        return new Where( value, ENDSWITH );
    };

    Where* contains( tstring value )
    {
        return new Where( value, CONTAINS );
    };

    Where* greaterthan( int value )
    {
        return new Where( value, GREATERTHAN );
    };

    Where* greaterthan( DateTime value )
    {
        return new Where( value, GREATERTHAN );
    };

    Where* lessthan( int value )
    {
        return new Where( value, LESSTHAN );
    };

    Where* lessthan( DateTime value )
    {
        return new Where( value, LESSTHAN );
    };

    Where* between( int value, int valuetwo )
    {
        return new Where( value, valuetwo, BETWEEN );
    };

    Where* between( DateTime value, DateTime valuetwo )
    {
        return new Where( value, valuetwo, BETWEEN );
    };

    Where* equals( int value )
    {
        return new Where( value, EQUALS );
    };

    Where* equals( DateTime value )
    {
        return new Where( value, EQUALS );
    };

    Where* equals( tstring value )
    {
        return new Where( value, EQUALS );
    };

    Where* equals( bool value )
    {
        if( value )
            return new Where( 0, EQUALS, true );
        return new Where( 0, EQUALS );
    };

    Where* equals( const tchar* value )
    {
        return equals( tstring( value ) );
    };

    Where* in( std::vector<int> values )
    {
        return new Where( values, ISIN );
    };

    Where* isnull()
    {
        return new Where( ISNULL );
    };

    // negated values

    Where* nstartswith( tstring value )
    {
        return new Where( value, STARTSWITH, true );
    };

    Where* nendswith( tstring value )
    {
        return new Where( value, ENDSWITH, true );
    };

    Where* ncontains( tstring value )
    {
        return new Where( value, CONTAINS, true );
    };

    Where* ngreaterthan( int value )
    {
        return new Where( value, GREATERTHAN, true );
    };

    Where* ngreaterthan( DateTime value )
    {
        return new Where( value, GREATERTHAN, true );
    };

    Where* nlessthan( int value )
    {
        return new Where( value, LESSTHAN, true );
    };

    Where* nlessthan( DateTime value )
    {
        return new Where( value, LESSTHAN, true );
    };

    Where* nbetween( int value, int valuetwo )
    {
        return new Where( value, valuetwo, BETWEEN, true );
    };

    Where* nbetween( DateTime value, DateTime valuetwo )
    {
        return new Where( value, valuetwo, BETWEEN, true );
    };

    Where* nequals( int value )
    {
        return new Where( value, EQUALS, true );
    };

    Where* nequals( DateTime value )
    {
        return new Where( value, EQUALS, true );
    };

    Where* nequals( tstring value )
    {
        return new Where( value, EQUALS, true );
    };

    Where* nequals( bool value )
    {
        return equals( !value );
    };

    Where* nequals( const tchar* value )
    {
        return nequals( tstring( value ) );
    };

    Where* nin( std::vector<int> values )
    {
        return new Where( values, ISIN, true );
    };

    Where* nisnull()
    {
        return new Where( ISNULL, true );
    };

};
