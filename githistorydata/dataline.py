

class DataLine( object ):
    def __init__( self, commit_hash, date, author, added, removed, filename ):
        self.commit_hash = commit_hash
        self.date = date
        self.author = author
        self.added = added
        self.removed = removed
        self.filename = filename

    def __str__( self ):
        return " ".join(
            (
                self.commit_hash,
                self.date,
                self.author,
                str( self.added ),
                str( self.removed ),
                self.filename
            )
        )

    def __eq__( self, other ):
        return (
            self.commit_hash == other.commit_hash
            and self.date == other.date
            and self.author == other.author
            and self.added == other.added
            and self.removed == other.removed
            and self.filename == other.filename
        )
