
import re
import dateutil.parser

from githistorydata.commitdetail import CommitDetail
from githistorydata.filechanges import FileChanges
from githistorydata.logline import LogLine


class Git( object ):

    def __init__( self, raw_git ):
        self.raw_git = raw_git

    def log( self ):
        """
        Return a list of LogLine for the repo in the current dir.
        """
        return list(
            self._logline( ln.strip() )
            for ln in self.raw_git.git_log_pretty_tformat_H_ai_an()
            if ln.strip() != ""
        )

    def show( self, commit_hash, date, author ):
        show_lines = self.raw_git.git_show_numstat( commit_hash )
        return CommitDetail(
            commit_hash,
            date,
            author,
            list( self._showline( l ) for l in show_lines[1:] if l != "")
        )

    _logline_re = re.compile(
        r"([0-9a-f]{40}) (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [-+]\d{4}) (.+)"
    )

    def _logline( self, ln ):
        m = Git._logline_re.match( ln )
        if not m:
            raise Exception(
                "Line from git log '%s' did not match expected format"
                % ln
            )
        return LogLine(
            m.group( 1 ),
            dateutil.parser.parse( m.group( 2 ) ),
            m.group( 3 )
        )

    showline_re = re.compile(
        r"(-|\d+)\s+(-|\d+)\s+(.*)"
    )

    @staticmethod
    def lines_changed( num ):
        if num == "-":
            return 0
        else:
            return int( num )

    def _showline( self, ln ):
        m = Git.showline_re.match( ln )
        if not m:
            raise Exception(
                "Line from git show '%s' did not match expected format"
                % ln
            )
        return FileChanges(
            Git.lines_changed( m.group( 1 ) ),
            Git.lines_changed( m.group( 2 ) ),
            m.group( 3 )
        )
