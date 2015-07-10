class CodeLine( object ):
    def __init__( self, commit_hash, date, author, weight ):
        self.commit_hash = commit_hash
        self.date = date
        self.author = author
        self.weight = weight
