
from githistorydata.codeline import CodeLine
from githistorydata.expand_commits import expand_commits
from githistorydata.logline import LogLine

from nose.tools import assert_equal


def Normal_commits_are_not_expanded__test():
    assert_equal(
        [
            CodeLine( "h1", "dt1", "a1", 1.0 ),
            CodeLine( "h2", "dt2", "a2", 1.0 ),
        ],
        list( expand_commits(
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
        list( expand_commits(
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
        list( expand_commits(
            [
                LogLine( "h1", "dt1", "a1" ),
                LogLine( "h2", "dt2", "a1,a2,a3" ),
                LogLine( "h4", "dt4", "a4" ),
            ]
        ) )
    )
