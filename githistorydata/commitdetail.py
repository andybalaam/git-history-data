

class CommitDetail( object ):
    def __init__( self, commit_hash, date, author, file_changes ):
        self.commit_hash = commit_hash
        self.date = date
        self.author = author
        self.file_changes = file_changes

    def __str__( self ):
        ret = "%s %s %s" % (
            self.commit_hash,
            self.date,
            self.author,
        )
        ret += "\n"
        ret += "\n".join( ( "    " + str(ch) ) for ch in self.file_changes )
        return ret

    def __eq__( self, other ):
        return (
            self.commit_hash == other.commit_hash
            and self.file_changes == other.file_changes
        )
