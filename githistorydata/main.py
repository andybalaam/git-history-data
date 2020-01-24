
import subprocess
import sys

from githistorydata.csv import Csv
from githistorydata.expand_commits import expand_authors, expand_lines
from githistorydata.git import Git
from githistorydata.rawgit import RawGit
from githistorydata.settings import Settings


def main( argv, out, err ):
    settings = Settings()
    try:
        git = Git( RawGit(settings["git_path"]) )
        csv = Csv(
            out,
            ( "Commit", "Date", "Author", "Added", "Removed", "File" )
        )
        for cod in expand_lines( git, expand_authors( git.log() ) ):
            csv.line( (
                cod.commit_hash,
                cod.date.date().isoformat(),
                cod.author,
                cod.added,
                cod.removed,
                cod.filename,
            ) )
    except subprocess.CalledProcessError as e:
        print(str( e ))
        sys.exit( 1 )
    finally:
        out.flush()
