"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import ctypes

class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Book')
        self.load_model('Author')
        self.load_model('User')
        self.load_model('Review')
        self.db = self._app.db    
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        first_three_books_reviews = self.models['Review'].get_first_three_books_reviews(3)
        book_ids = [r['bookId'] for r in first_three_books_reviews]
        all_books = self.models['Book'].get_all_books(book_ids)
        return self.load_view('/books/index.html', first_three_books_reviews = first_three_books_reviews, all_books = all_books)


    def add(self):
        all_books = self.models['Book'].get_books_title()
        all_authors = self.models['Author'].get_all_authors()
        return self.load_view('/books/add.html', all_books = all_books, all_authors = all_authors)  

    def add_book_review(self):
      print ("add_book_review starts now")
      book_info ={"book_title": request.form['book_title']}
      print book_info

      reviewer = self.models['User'].get_user(session['userId'])
      print reviewer

      if request.form['book_title_list']!='' :
          book = self.models['Book'].get_book(request.form['book_title_list'])
          review = self.models['Review'].add_review(book['id'], reviewer['id'], request.form['review'], request.form['rating'])
      else:
          author = self.models['Author'].add_author(request.form['new_author'])
          if author['status'] == False:
              error_dict_author= author['error_dict']
              for key, val in error_dict_author.items():
                  flash(val, key)    
              return redirect ('/books/add')
          book = self.models['Book'].add_book(book_info, author['author']['id'])
          if book['status'] == False:
              error_dict_book = book['error_dict']
              for key, val in error_dict_book.items():
                  flash(val, key)    
              return redirect ('/books/add')

          review = self.models['Review'].add_review(book['book']['id'], reviewer['id'], request.form['review'], request.form['rating'])
          print review    

      return redirect('/books')

    def book_detail(self, id):
      book_title_and_author = self.models['Book'].get_book_title_and_author(id)
      print book_title_and_author
      book_total_reviews = self.models['Review'].get_a_book_total_reviews(id)
      return self.load_view('/books/detail.html', book_title_and_author = book_title_and_author, book_total_reviews = book_total_reviews)        
      
      #return self.load_view('/books/detail.html', book_details = book_detail_review)
 
    def confirm_delete(self, id):
      one_review = self.models['Review'].get_review_by_id(id)
      return self.load_view('/books/show.html', review=one_review)  

    def review_delete(self, id):
      one_review = self.models['Review'].get_review_by_id(id)
      review_deleted = self.models['Review'].delete(id)
      return redirect('/books/'+str(one_review['book_id']))