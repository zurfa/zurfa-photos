class DirectoryError(Exception):
    def __init__(self, Directory):
        self.Dir = Directory
        Exception.__init__(self,"Error opening directory, does it exist? %s" % self.Dir)

class NullDirectoryError(Exception):
    def __init__(self, Directory):
        self.Dir = Directory
        Exception.__init__(self,"Did not find any files in directory. %s" % self.Dir)

class ValidFilesError(Exception):
    def __init__(self, Directory):
        self.Dir = Directory
        Exception.__init__(self,"Did not find any valid files in directory. %s" % self.Dir)