""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Book(Model):
    def __init__(self):
        super(Book, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """

    def add_book(self, book_info, author_id):
        error_dict = {}
        error = False
        book_title = book_info['book_title']

        if book_title == '':
            error_dict ['bookTitleError'] = "Please enter or select Book Title!"
            error = True

        if error: 
            return {"status":False, "error_dict": error_dict}    

        if book_title:
            query = "INSERT INTO books(title, author_id, created_at, updated_at) values(:title, :author_id, NOW(), NOW())"
            data = {"title" : book_title,
                   "author_id" : author_id
                  }
            book_info = self.db.query_db(query, data)

            if book_info:
                select_query = "SELECT * from books WHERE title =:title"
                data={"title" : book_title} 
                book =  self.db.query_db(select_query, data)
                #return book[0]
                print book[0]
                return{"status": True, "book": book[0]}    
           
    def get_book(self, book_title):
        if book_title:
            query = "SELECT * FROM books WHERE title = :title"
            data = {"title" : book_title}
            book_detail = self.db.query_db(query, data)
            return book_detail[0]

    def get_books_title(self):
        query = "SELECT * FROM books"
        books_title = self.db.query_db(query)
        return books_title        

    def get_all_books(self, filter_book_ids):
        query = "SELECT b.title, b.id as bookId FROM books b where b.id in (select distinct r.book_id from reviews r) and b.id not in :filter_book_ids order by b.id"
        print query
        all_books = self.db.query_db(query, {'filter_book_ids': filter_book_ids})
        return all_books

    def get_book_title_and_author(self, id):  
        query = "SELECT b.title, a.name as authorName from books b inner join authors a on b.author_id = a.id where b.id =:bookId"
        data = {"bookId" : id}
        book_ttile_and_author = self.db.query_db(query, data)
        return book_ttile_and_author[0]

                 
            
