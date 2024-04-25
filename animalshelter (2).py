# Name: Kat Gilliland 
# Date: April 7, 2024

from pymongo import MongoClient # Importing MongoClient class from pymongo module KG
from bson.objectid import ObjectId

# Initialzing AnimalShelter class KG
class AnimalShelter(object): 
    def __init__(self, username, password): # Initializing object KG
        USER = 'aacuser' # Setting user KG
        PASS = 'SNHU1234' # Setting pass KG
        HOST = 'nv-desktop-services.apporto.com' # Setting host KG
        PORT = '30460' # Setting port KG
        DB = 'AAC' # Setting database name KG
        COL = 'animals' # Setting collection name KG
        
        # Creating MongoClient instance KG
        self.client = MongoClient('mongodb://%s:%s@%s:%s' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB] 
        self.collection = self.database[COL]
        
# Create method to implement the C in CRUD KG
    def create(self, data):
        if data is not None:
            active_document = self.collection.find_one({"name": data["name"]}) # Checking to make sure there is not an existing document with same name KG
            if active_document:
                updated_data = {"$set": data} # If an existing document is found, update document with new data KG
                result = self.collection.update_one({"_id": active_document["_id"]}, updated_data) # Updating document KG
            else: 
                result = self.collection.insert_one(data) # Else, insert document into collection KG
            return True # Return true is successful KG
        else: # Else, nothing to return because data parameter is empty KG
            raise Exception("Nothing to save because data parameter is empty. Please try again.")
        
# Read method to implement the R in CRUD KG
    def read(self, query):
         if query is not None:
             query_result = self.collection.find(query) # Querying animals collection for matching query KG
             documents = list(query_result) # Converting cursor to documents list KG
             return documents # Returning list of documents KG
         else: # Else, returning exception if query parameter is empty KG
             raise Exception("Nothing to read because query parameter is empty. Please try again.")
        
# Update method to implement the U in CRUD KG
    def update(self, query, updatedData):
        if query is not None:
            active_document = self.collection.find_one(query) # Updating document in collection based on query KG
            if active_document:
                result = self.collection.update_one({"_id": active_document["_id"]}, updatedData) # Using specified ID to update document in collection KG
                if result.modified_count > 0:
                    return True # Returning successful result if record has been updated KG
                else: # Else, raising an exception KG
                    raise Exception("Error occurred. Cannot update. Please try again.")
            else: # Else, raising an exception if document cannot be found based on query KG
                raise Exception("Document not found based on query. Please try again.")
        else: # Else, raising an exception if query parameter is empty KG
            raise Exception("Query parameter cannot be empty. Please try again.")
                      
# Delete method to implement the D in CRUD KG
    def delete(self, query):
        if query is not None:
            result = self.collection.delete_one(query) # If data found, deleting it from single document KG
            if result.deleted_count > 0: # If item deleted/count has been modified, return true KG
                deleted_object = self.collection.find_one(query) # Retrieving deleted item from query KG
                return True, deleted_object # Confirming deletion and showing which item was deleted KG
            else: 
                raise Exception("Error occurred. Cannot delete. Please try again.")
     
            raise Exception("Query parameter cannot be empty. Please try again.")

        
