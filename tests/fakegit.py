
class FakeGit( object ):

    def __init__( self, ret_value ):
        self.ret_value = ret_value

    def git_log_pretty_tformat_H_ai_an( self ):
        return self.ret_value.split( "\n" )

    def git_show_numstat( self, commit_hash ):
        return self.ret_value.split( "\n" )
