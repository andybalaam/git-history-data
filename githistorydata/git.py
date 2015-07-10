
import re
import dateutil.parser

from githistorydata.logline import LogLine


class Git( object ):

    def __init__( self, raw_git ):
        self.raw_git = raw_git

    def log( self ):
        """
        Return a list of LogLine for the repo in the current dir.
        """
        return list(
            self.logline( ln.strip() )
            for ln in self.raw_git.git_log_pretty_tformat_H_ai_an()
            if ln.strip() != ""
        )

    logline_re = re.compile(
        r"([0-9a-f]{40}) (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [-+]\d{4}) (.+)"
    )

    def logline( self, ln ):
        m = Git.logline_re.match( ln )
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