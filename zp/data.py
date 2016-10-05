import sqlite3 as lite
import sys

class Data(object):
    """docstring for Data"""
    def __init__(self):
        super(Data, self).__init__()
        self.db = SQLLite()

    def add_to_library(self,data):
        pass

class SQLLite(object):
    """docstring for SQLLite"""
    def __init__(self):
        super(SQLLite, self).__init__()
        self.conn    = None

    def add_to_library(self,data):
        data    = self.noner(data)
        library_insert_query = ("INSERT INTO `library` (`id`, `ufid`, `path`, `origin`, `size`, "
            "`checksum`, `added`, `updated`, `extension`, `format`, `category`, `taken`, "
            "`lat`, `lon`, `device`, `width`, `height`, `exif_dump`) "
            "VALUES (NULL, :ufid, :path, :origin, :size, :checksum, :added, :updated, :extension, "
            ":format, :category, :taken, :lat, :lon, :device, :width, :height, :exif_dump);")
        if not self.conn:
            self.connect()
        cur = self.conn.cursor()
        try:
            cur.execute(library_insert_query,data)
        except lite.Error as Err:
            print Err
        else:
            cur.close()

    def commit(self):
        self.conn.commit()


    def connect(self):
        if not self.conn:
            self.conn = lite.connect('library.db')

    def noner(self,data_in):
        columns = ["ufid", "path", "origin", "size", "checksum", "added", "updated", 
            "extension", "format", "category", "taken", "lat", "lon", "device",
             "width", "height", "exif_dump"]
        data_out   = {}
        for column in columns:
            if column in data_in:
                data_out.update({column:data_in[column]})
            else:
                data_out.update({column:None})
        return data_out