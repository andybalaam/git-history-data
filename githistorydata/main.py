
import subprocess
import sys

from githistorydata.csv import Csv
from githistorydata.expand_commits import expand_commits
from githistorydata.git import Git
from githistorydata.rawgit import RawGit


def main( argv, out, err ):
    try:
        git = Git( RawGit() )
        csv = Csv( out, ( "Hash", "Date", "Author", "Weight" ) )
        for cod in expand_commits( git.log() ):
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
