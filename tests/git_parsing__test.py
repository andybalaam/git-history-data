
from datetime import datetime
import dateutil.parser

from githistorydata.commitdetail import CommitDetail
from githistorydata.filechanges import FileChanges
from githistorydata.git import Git
from githistorydata.logline import LogLine

from tests.fakegit import FakeGit

from nose.tools import assert_equal


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


def FileChanges_to_string__test():
    assert_equal( "+3 -2 foo.txt", str( FileChanges( 3, 2, "foo.txt" ) ) )


def CommitDetail_to_string__test():
    assert_equal(
        """myhash dt auth
    +1 -0 x.cpp
    +3 -2 y.cpp""",
        str( CommitDetail(
            "myhash",
            "dt",
            "auth",
            [
                FileChanges( 1, 0, "x.cpp" ),
                FileChanges( 3, 2, "y.cpp" ),
            ]
        ) )
    )


def Numstat_lines_are_parsed__test():
    git = Git( FakeGit( """2993dbf Lennart Tange "More generic dnd helper."
71      0       scripts/drag_and_drop_helper.js
0       66      scripts/dragdrop_pin_to_assemble.js
23      16      src/step_definitions/StepDef.java
""" ) )

    assert_equal(
        str( CommitDetail(
            "2993bdfAAAAAAAAAAAA",
            "dt",
            "auth",
            [
                FileChanges( 71,  0, "scripts/drag_and_drop_helper.js" ),
                FileChanges(  0, 66, "scripts/dragdrop_pin_to_assemble.js" ),
                FileChanges( 23, 16, "src/step_definitions/StepDef.java" ),
            ]
        ) ),
        str( git.show( "2993bdfAAAAAAAAAAAA", "dt", "auth" ) )
    )
