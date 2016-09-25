""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Review(Model):
    def __init__(self):
        super(Review, self).__init__()
    

    def add_review(self, book_id, reviewer_id, review_detail, rating):
        if review_detail:
            query = "INSERT INTO reviews (book_id, user_id, content, rating, created_at, updated_at) values(:book_id, :reviewer_id, :review_detail, :rating, NOW(), NOW())"
            data ={"book_id" : book_id,
                  "reviewer_id" : reviewer_id,
                  "review_detail" : review_detail,
                  "rating" : rating}
            self.db.query_db(query, data)

    def get_first_three_books_reviews(self, limit):
        query ="SELECT b.title, b.id as bookId, u.id as userId, r.content, r.rating, r.id as reviewId, u.alias, a.name, date_format(r.created_at,'%%D-%%M-%%Y') as created_at FROM reviews r inner join books b on r.book_id = b.id inner join authors a on  b.author_id = a.id inner join users u on r.user_id = u.id  ORDER BY r.id DESC LIMIT %s" %(limit)
        first_three_books_reviews = self.db.query_db(query)
        return first_three_books_reviews

    def get_a_user_total_review(self, id):
        if id:
            query = "SELECT count(r.id) as totalReview from reviews r inner join users u on r.user_id =u.id where u.id=:userId"    
            data = {'userId': id}
            total_review = self.db.query_db(query, data)
            return total_review[0]

    def get_a_user_total_reviewed_books(self, id):
        if id:
            query = "SELECT distinct b.title , b.id as bookId from books b inner join reviews r on r.book_id = b.id inner join  users u on u.id = r.user_id where r.user_id =:userId"    
            data = {'userId': id}
            total_reviewed_books = self.db.query_db(query, data)
            return total_reviewed_books

    def get_a_book_total_reviews(self, id):
        if id:
            query = "SELECT r.content, r.id as reviewId, r.rating, date_format(r.created_at,'%D-%M-%Y') as created_at, u.alias, u.id as userId from reviews r inner join books b on b.id = r.book_id inner join users u on u.id = r. user_id where b.id =:bookId"          
            data = {"bookId" :id}
            book_total_review = self.db.query_db(query, data)
            return book_total_review

    def get_review_by_id(self, id): 
        query = "SELECT * FROM reviews where id=:reviewId"
        data ={'reviewId' : id}
        review = self.db.query_db(query, data)
        return review[0]        

    def delete(self, id):
        if id:
            query ="DELETE from reviews where id=:review_id"
            data = {'review_id': id}
            res = self.db.query_db(query, data)
            return res       
                  