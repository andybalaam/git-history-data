
import subprocess


class RawGit( object ):
    def __init__( self ):
        pass

    def git_log_pretty_tformat_H_ai_an( self ):
        return subprocess.check_output(
            ["/usr/bin/git", "log", "--pretty=tformat:%H %ai %an"]
        ).split( "\n" )
