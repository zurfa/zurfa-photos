import sqlite3 as lite
import sys

class Data(object):
    """docstring for Data"""
    def __init__(self, dbtype):
        super(Data, self).__init__()
        self.dbtype = dbtype


class SQLLite(object):
    """docstring for SQLLite"""
    def __init__(self):
        super(SQLLite, self).__init__()
        self.con    = None
        

    def conn(self):
        if not self.con:
            self.con = lite.connect('library.db')