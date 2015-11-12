
from io import StringIO
from githistorydata.csv import Csv

from nose.tools import assert_equal


def Headings_are_printed_quoted__test():
    out = StringIO()
    csv = Csv( out, ( "a", "B c" ) )
    csv # Silence lint
    assert_equal(
        '''"a", "B c"
''',
        out.getvalue()
    )


def String_lines_are_printed_in_quotes__test():
    out = StringIO()
    csv = Csv( out, ( "a", "b" ) )
    csv.line( ( "x", "y" ) )
    assert_equal(
        '''"a", "b"
"x", "y"
''',
        out.getvalue()
    )


def Number_lines_are_printed_without_quotes__test():
    out = StringIO()
    csv = Csv( out, ( "a", "b", "c" ) )
    csv.line( ( 2, "x", 3.5 ) )
    assert_equal(
        '''"a", "b", "c"
2, "x", 3.5
''',
        out.getvalue()
    )


def Multiple_lines_are_printed__test():
    out = StringIO()
    csv = Csv( out, ( "a", "b", "c" ) )
    csv.line( ( 2, "x", 3.5 ) )
    csv.line( ( 4, "y", 5.5 ) )
    assert_equal(
        '''"a", "b", "c"
2, "x", 3.5
4, "y", 5.5
''',
        out.getvalue()
    )
