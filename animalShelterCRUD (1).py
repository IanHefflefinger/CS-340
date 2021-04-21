from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:50549/AAC' % (username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None and type(data) == dict:
            #self.database.animals.insert(data)  # data should be dictionary  
            try:
                self.database.animals.insert_one(data)
                return True
            except:
                return False
                
        else:
            raise Exception("Nothing to save, because data parameter is empty or not a dict")

# Create method to implement the R in CRUD. 
    def read(self, data):
        if data is not None:
            my_cursor = self.database.animals.find(data, {"_id" : False})
            if my_cursor.count() > 0:
                #for obj in my_cursor:
                    #print(obj)
                return my_cursor
            else:
                raise Exception('No documents found')
                
        else:
            raise Exception("Nothing to find, because data parameters (key and/or value) are empty")
            
# Complete this create method to implement the U in CRUD.
    def update(self, target_object, updated_object):
        if target_object is not None and updated_object is not None:
            updated_results = self.database.animals.update_many(target_object, updated_object)
            return updated_results.raw_result
            
        else:
            raise Exception('Missing arguments')
    
# Complete this create method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            if self.database.animals.find(data).count() > 0:
                deleteResult = self.database.animals.delete_many(data)
                return deleteResult.raw_result
            else:
                raise Exception('No documents deleted') 
        else:
            raise Exception("Nothing to find, because data parameters (key and/or value) are empty")

    
    
    
    
    
    
    
    