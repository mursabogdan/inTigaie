__author__ = 'bogdanmursa'


class InMemoryRepository():

    def __init__(self):
        self.list = []

    def add(self, object):
        self.list.append(object)

    def remove(self, object):
        self.list.remove(object)

    def findOne(self, value):
        return [object for object in self.list if object.id == value][0]

    def findAll(self, value):
        return [object for object in self.list if object.id == value]

    def getAll(self):
        return self.list



