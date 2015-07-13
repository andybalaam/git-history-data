
import subprocess


class RawGit( object ):
    def __init__( self ):
        pass

    def git_log_pretty_tformat_H_ai_an( self ):
        return self._run_git( ["log", "--pretty=tformat:%H %ai %an"] )

    def git_show_numstat( self, commit_hash ):
        return self._run_git( ["show", "--numstat", commit_hash] )

    def _run_git( self, args ):
        return subprocess.check_output(
            ["/usr/bin/git"] + args
        ).split( "\n" )
