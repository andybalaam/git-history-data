

class LogLine( object ):
    def __init__( self, commit_hash, date, author ):
        self.commit_hash = commit_hash
        self.date = date
        self.author = author

    def __str__( self ):
        return "%s %s %s" % ( self.commit_hash, self.date, self.author )

    def __eq__( self, other ):
        return (
            self.commit_hash == other.commit_hash
            and self.date == other.date
            and self.author == other.author
        )
