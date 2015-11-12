class Csv( object ):
    def __init__( self, out, columns ):
        self.out = out
        self.columns = columns
        self._write( columns )

    def line( self, items ):
        assert len( items ) == len( self.columns )
        self._write( items )

    def _write( self, items ):
        self.out.write(
            u", ".join( self._fmt( c ) for c in items ) )

        self.out.write( u"\n" )

    def _fmt( self, item ):
        try:
            float( item )
            return str( item )
        except:
            return '"%s"' % item
