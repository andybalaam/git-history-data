
import subprocess


class RawGit( object ):
    def __init__( self, git_path="/usr/bin/git" ):
        self._git_path = git_path

    def git_log_pretty_tformat_H_ai_an( self ):
        return self._run_git(
            ["log", "--no-merges", "--pretty=tformat:%H %ai %an"] )

    def git_show_numstat( self, commit_hash ):
        return self._run_git(
            ["show", "--pretty=oneline", "--numstat", commit_hash] )

    def _run_git( self, args ):
        return subprocess.check_output(
            [self._git_path] + args
        ).decode( encoding="UTF-8", errors="replace" ).split( "\n" )

