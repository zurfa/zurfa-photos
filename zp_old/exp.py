class DirectoryError(Exception):
    def __init__(self, Directory=None):
        self.Dir = Directory
        Exception.__init__(self,"Error opening directory, does it exist? %s" % self.Dir)

class NullDirectoryError(Exception):
    def __init__(self, Directory=None):
        self.Dir = Directory
        Exception.__init__(self,"Did not find any files in directory. %s" % self.Dir)

class ValidFilesError(Exception):
    def __init__(self, Directory=None):
        self.Dir = Directory
        Exception.__init__(self,"Did not find any valid files in directory. %s" % self.Dir)

class ExifError(Exception):
    def __init__(self, File=None):
        self.File = File
        Exception.__init__(self,"Error getting EXIF data, it might be corrupt or non-existent %s" % self.File)