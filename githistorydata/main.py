
import subprocess
import sys

from githistorydata.csv import Csv
from githistorydata.git import Git
from githistorydata.rawgit import RawGit


class CodeLine( object ):
    def __init__( self, commit_hash, date, author, weight ):
        self.commit_hash = commit_hash
        self.date = date
        self.author = author
        self.weight = weight


def expand( log_lines ):
    for log_line in log_lines:
        spl = log_line.author.split( "," )
        weight = 1.0 / len( spl )
        for auth in spl:
            yield CodeLine(
                log_line.commit_hash,
                log_line.date,
                auth.strip(),
                weight
            )


def main( argv, out, err ):
    try:
        git = Git( RawGit() )
        csv = Csv( out, ( "Hash", "Date", "Author", "Weight" ) )
        for cod in expand( git.log() ):
            csv.line( (
                cod.commit_hash,
                cod.date.date().isoformat(),
                cod.author,
                cod.weight
            ) )
    except subprocess.CalledProcessError, e:
        print str( e )
        sys.exit( 1 )
    finally:
        out.flush()
