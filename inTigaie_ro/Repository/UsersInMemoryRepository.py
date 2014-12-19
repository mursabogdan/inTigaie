__author__ = 'bogdanmursa'

from InMemoryRepository import InMemoryRepository

class UsersInMemoryRepository(InMemoryRepository):

    def __init__(self):
        self.list = []

    def add(self, value):
        self.list.append(value)

    def update(self, value):
        pass

    def delete(self, value):
        self.list.pop(value)

    def findOne(self, value):
        pass

    def findAll(self, value):
        pass

    def getAll(self):
        return self.list
