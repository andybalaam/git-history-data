

class FileChanges( object ):
    def __init__( self, added, removed, name ):
        self.added = added
        self.removed = removed
        self.name = name

    def __str__( self ):
        return "+%d -%d %s" % ( self.added, self.removed, self.name )

    def __eq__( self, other ):
        return (
            self.added == other.added
            and self.removed == other.removed
            and self.name == other.name
        )
