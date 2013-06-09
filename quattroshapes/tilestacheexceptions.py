#!/usr/bin/env python

foo = 123

class NothingMoreToSeeHere(Exception):
    """ Don't recon any farther.
    
        This exception can be thrown in a provider to signal to
        TileStache.getTile() that the result tile should be returned,
        and saved in a cache, but no further child tiles should be rendered.
        Useful in cases where data is not well distributed geographically.
        
        The one constructor argument is an instance of PIL.Image or
        some other object with a save() method, as would be returned
        by provider renderArea() or renderTile() methods.
    """
    def __init__(self, tile):
        self.tile = tile
        Exception.__init__(self, tile)

class NothingToSeeHere(Exception):
    """ Don't recon any farther.
    
        This exception can be thrown in a provider to signal to
        TileStache.getTile() that the result tile should be returned,
        and but not saved in a cache and no further child tiles should be rendered.
        Useful in cases where data is not well distributed geographically.
    """
    def __init__(self):
        Exception.__init__(self)