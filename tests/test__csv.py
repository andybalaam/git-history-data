import unittest
from io import StringIO
from githistorydata.csv import Csv


class TestCsv(unittest.TestCase):
    def test__Headings_are_printed_quoted(self):
        out = StringIO()
        csv = Csv( out, ( "a", "B c" ) )
        csv # Silence lint
        self.assertEqual(
            '''"a", "B c"
''',
            out.getvalue()
        )


    def test__String_lines_are_printed_in_quotes(self):
        out = StringIO()
        csv = Csv( out, ( "a", "b" ) )
        csv.line( ( "x", "y" ) )
        self.assertEqual(
            '''"a", "b"
"x", "y"
''',
            out.getvalue()
        )


    def test__Number_lines_are_printed_without_quotes(self):
        out = StringIO()
        csv = Csv( out, ( "a", "b", "c" ) )
        csv.line( ( 2, "x", 3.5 ) )
        self.assertEqual(
            '''"a", "b", "c"
2, "x", 3.5
''',
            out.getvalue()
        )


    def test__Multiple_lines_are_printed(self):
        out = StringIO()
        csv = Csv( out, ( "a", "b", "c" ) )
        csv.line( ( 2, "x", 3.5 ) )
        csv.line( ( 4, "y", 5.5 ) )
        self.assertEqual(
            '''"a", "b", "c"
2, "x", 3.5
4, "y", 5.5
''',
            out.getvalue()
        )
