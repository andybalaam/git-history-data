
from githistorydata.codeline import CodeLine
from githistorydata.commitdetail import CommitDetail
from githistorydata.dataline import DataLine
from githistorydata.expand_commits import expand_authors
from githistorydata.expand_commits import expand_detail
from githistorydata.expand_commits import expand_lines
from githistorydata.filechanges import FileChanges
from githistorydata.git import Git
from githistorydata.logline import LogLine

from tests.fakegit import FakeGit

from nose.tools import assert_equal


def Normal_commits_are_not_expanded__test():
    assert_equal(
        [
            CodeLine( "h1", "dt1", "a1", 1.0 ),
            CodeLine( "h2", "dt2", "a2", 1.0 ),
        ],
        list( expand_authors(
            [
                LogLine( "h1", "dt1", "a1" ),
                LogLine( "h2", "dt2", "a2" ),
            ]
        ) )
    )


def Shared_commits_are_expanded__test():
    assert_equal(
        [
            CodeLine( "h1", "dt1", "a1", 0.5 ),
            CodeLine( "h1", "dt1", "a2", 0.5 ),
        ],
        list( expand_authors(
            [
                LogLine( "h1", "dt1", "a1,a2" ),
            ]
        ) )
    )


def Multiple_commits__test():
    assert_equal(
        [
            CodeLine( "h1", "dt1", "a1", 1.0 ),
            CodeLine( "h2", "dt2", "a1", 1.0/3 ),
            CodeLine( "h2", "dt2", "a2", 1.0/3 ),
            CodeLine( "h2", "dt2", "a3", 1.0/3 ),
            CodeLine( "h4", "dt4", "a4", 1.0 ),
        ],
        list( expand_authors(
            [
                LogLine( "h1", "dt1", "a1" ),
                LogLine( "h2", "dt2", "a1,a2,a3" ),
                LogLine( "h4", "dt4", "a4" ),
            ]
        ) )
    )


def Expand_detail_for_single_author__test():
    assert_equal(
        [
            DataLine(
                "myhash1",
                "mydate1",
                "Me",
                32,
                1,
                "foo.txt",
            ),
            DataLine(
                "myhash1",
                "mydate1",
                "Me",
                0,
                10,
                "bar.pl",
            )
        ],
        list( expand_detail(
            CommitDetail(
                "myhash1",
                "mydate1",
                "Me",
                [
                    FileChanges( 32, 1,  "foo.txt" ),
                    FileChanges( 0,  10, "bar.pl" ),
                ]
            ),
            1.0
        ) )
    )


def Expand_detail_with_weights_on_lines__test():
    assert_equal(
        [
            DataLine( "h", "d", "Me", 9, 0, "foo.txt" ),
            DataLine( "h", "d", "Me", 0, 3, "bar.pl" ),
        ],
        list( expand_detail(
            CommitDetail(
                "h",
                "d",
                "Me",
                [
                    FileChanges( 32, 1,  "foo.txt" ),
                    FileChanges( 0,  10, "bar.pl" ),
                ]
            ),
            0.3
        ) )
    )


def Expand_lines_makes_one_line_for_each_modified_file():
    git = Git( FakeGit( """2976 Andy Balaam "desc."
10      2       f.txt
1       0       g.txt
""", """2976 Peter Broadbent "desc2."
0       18      h.txt
4       14      i.txt

""") )
    assert_equal(
        [
            DataLine( "h", "d", "a", 10, 2, "f.txt" ),
            DataLine( "h", "d", "a",  1, 0, "g.txt" ),
            DataLine( "j", "e", "b",  0, 9, "h.txt" ),
            DataLine( "j", "e", "b",  2, 7, "i.txt" ),
        ],
        expand_lines(
            git,
            CodeLine( "h", "d", "a", 1.0 ),
            CodeLine( "j", "j", "b", 0.5 ),
        )
    )
