""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Author(Model):
    def __init__(self):
        super(Author, self).__init__()

    def add_author(self, author_name):
        error_dict = {}
        error = False
        if author_name == '':
            error_dict ['authorError'] = "Please enter or select Author Name!"
            error = True

        if error: 
            return {"status":False, "error_dict": error_dict}

        else:
           query = "INSERT INTO authors (name, created_at, updated_at) values(:name, NOW(),NOW())"
           data ={"name" : author_name}
           author_info = self.db.query_db(query, data)

           if author_info:
               select_query = "SELECT * from authors WHERE name =:name"
               data={"name" : author_name} 
               author =  self.db.query_db(select_query, data)
               #return author[0]
               return{"status": True, "author": author[0]}
            
    def get_all_authors(self):
        all_authors = self.db.query_db("SELECT * FROM authors")
        return all_authors
