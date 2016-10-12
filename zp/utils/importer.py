from .. import config

class Directory(object):
    """Imports images from the specified directory (config default if not)"""
    def __init__(self, Dir=False):
        super(Directory, self).__init__()
        self.Dir = Dir
        