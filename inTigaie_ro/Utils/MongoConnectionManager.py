__author__ = 'bogdanmursa'

from pymongo import Connection


class MongoConnectionManager():
    connection = None

    def __init__(self, database, collection):
        self.connection = Connection()[database][collection]

    def closeConnection(self):
        self.connection.close()