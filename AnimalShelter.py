#!/usr/bin/env python
# coding: utf-8

# In[9]:


from pymongo import MongoClient
from bson.objectid import ObjectId
#Lindsey Delorenzo for CS340

class AnimalShelter(object):
    
    
    # using the base code from the assignment
    
    def __init__(self):
        USER = 'aacuser'
        PASS = 'password123'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31080
        DB = 'AAC'
        COL = 'animals'
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    
    # creating the functions for create, read, update, and delete
    
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            if insertSuccess != 0:
                return False
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    def read(self, findData):
        if findData:
            self.database.animals.find(findData, {"_id": False})
        else:
            raise Exception("Nothing to read, because data parameter is empty")
        return data
    
    def update (self, updateData):
        if findData is not None:
            self.database.animals.update_many(findData, {"$set": updateData})
        else:
            raise Exception("Nothing to update, because data parameter is empty")
        return result.raw_result
    
    def delete(self, deleteData):
        if deleteData is not None:
            self.database.animals.delete_many(deleteData)
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
        return result.raw_result


# In[ ]:









