class CodeLine( object ):

    def __init__( self, commit_hash, date, author, weight ):
        self.commit_hash = commit_hash
        self.date = date
        self.author = author
        self.weight = weight

    def __eq__( self, other ):
        return(
            self.commit_hash == other.commit_hash
            and self.date == other.date
            and self.author == other.author
            and self.weight == other.weight
        )

    def __str__( self ):
        return "%s %s %s %f" % (
            self.commit_hash, self.date, self.author, self.weight
        )
