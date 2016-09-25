"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('User')
        self.load_model('Book')
        self.load_model('Review')
        #self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
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
        if not session.get('userId'):
            session['userId']=''
        if not session.get('first_name'):
            session['first_name']=''
        if not session.get('last_name'):
            session['last_name']=''
        return self.load_view('/users/index.html')

        if session[userId]!='':
           return redirect('/books')


    def login(self):

        login_info = {
            "email": request.form['email'], 
            "password": request.form['password']
        }
        login_status = self.models['User'].login_user(login_info)

        #Log in the user if user is authenticated
        if login_status['status']:
            session['userId'] = login_status['user']['id']
            session['first_name'] = login_status['user']['first_name']
            session['last_name'] = login_status['user']['last_name']
            print session['last_name']
            return redirect('/books')

        if login_status['status'] == False:
            error_dict = login_status['error_dict']
            for key, val in error_dict.items():
                flash(val, key)
            return redirect('/')         


    def register(self):
        register_info = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "alias": request.form['alias'],
            "email": request.form['email'], 
            "password": request.form['password'],
            "confirm_password": request.form['confirm_password']
        }

        register_status = self.models['User'].register(register_info)

        #Flash errors if registration fails
        if register_status['status'] == False:
            error_dict = register_status['error_dict']
            for key, val in error_dict.items():
                flash(val, key)
            return redirect ('/')    

        #Log in the user if user is registered successfully
        else:
            session['userId'] = register_status['user']['id']
            session['first_name'] = register_status['user']['first_name']
            session['last_name'] = register_status['user']['last_name']
            print session['last_name']

            return redirect ('/books')

    def logoff(self):
        session['userId'] = ''
        session['First_name'] = ''
        session['last_name'] = ''
        return redirect ('/')

    def user_detail(self, id):
       user_detail = self.models['User'].get_user(id) 
       total_review =self.models['Review'].get_a_user_total_review(id)
       total_reviewed_books = self.models['Review'].get_a_user_total_reviewed_books(id)
       return self.load_view('/users/detail.html', user_detail = user_detail, total_review = total_review, total_reviewed_books = total_reviewed_books)    


    def get_user_details(self, id):
        user_detail = self.models['User'].get_user(id)
        return self.load_view('/users/edit.html', user_detail = user_detail)

    def edit_user_details(self, id):
        total_review =self.models['Review'].get_a_user_total_review(id)
        total_reviewed_books = self.models['Review'].get_a_user_total_reviewed_books(id)
        edit_info = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "alias": request.form['alias'],
            "email": request.form['email'], 
            "password": request.form['password'],
            "confirm_password": request.form['confirm_password'],
        }
        #return redirect ('/users/edit/'+str(id))

        edit_status = self.models['User'].edit_user_details(edit_info, id)
        #print edit_status['user']['id']

        #Flash errors if edit fails
        if edit_status['status'] == False:
            error_dict = edit_status['error_dict']
            for key, val in error_dict.items():
                flash(val, key)
            return redirect ('/users/edit/'+str(id))    

        else:
            session['userId'] = edit_status['user']['id']
            session['first_name'] = edit_status['user']['first_name']
            session['last_name'] = edit_status  ['user']['last_name']
            return self.load_view('/users/detail.html', user_detail = edit_status['user'], total_review = total_review, total_reviewed_books = total_reviewed_books)     
