
from datetime import datetime
import dateutil.parser

from githistorydata.git import Git
from githistorydata.logline import LogLine

from nose.tools import assert_equal


class FakeGit( object ):
    def __init__( self, ret_value ):
        self.ret_value = ret_value

    def git_log_pretty_tformat_H_ai_an( self ):
        return self.ret_value.split( "\n" )


def Log_lines_are_parsed__test():
    git = Git( FakeGit( """
64c5da790fb7edef4f99053497075839d11bb6d8 2015-07-09 12:00:00 +0100 Alban Tsui
2993dbf67c7e0659eba13987c98c5a03aade7099 2015-10-31 12:15:27 +0100 Lennart Tange
c504bd352d5d9dd0ccec3cd601ac02b14f4982a8 2015-07-09 12:00:00 -0200 Alban Tsui
    """ ) )

    off1 = dateutil.tz.tzoffset( "tz",    60*60 )  # +0100
    off2 = dateutil.tz.tzoffset( "tz", -2*60*60 )  # -0200

    assert_equal(
        [
            LogLine(
                "64c5da790fb7edef4f99053497075839d11bb6d8",
                datetime( 2015, 7, 9, 12, 0, 0, 0, off1 ),
                "Alban Tsui"
            ),
            LogLine(
                "2993dbf67c7e0659eba13987c98c5a03aade7099",
                datetime( 2015, 10, 31, 12, 15, 27, 0, off1 ),
                "Lennart Tange"
            ),
            LogLine(
                "c504bd352d5d9dd0ccec3cd601ac02b14f4982a8",
                datetime( 2015, 7, 9, 12, 0, 0, 0, off2 ),
                "Alban Tsui"
            )
        ],
        git.log()
    )
