# create a dictionary about session details

user_session = {
    'is_logged_in' : False
}

# login required decorator
def login_required(func):
    def wrapper(*args ,  **kwargs):
        if user_session.get('is_logged_in'):
            return func(*args , **kwargs)
        else:
            print("You have to login")
            return None
    return wrapper

@login_required
def view_profile():
    print("Welcome to your profile")
    
print('---------No logged in----------')
view_profile()

# user is logged in
user_session['is_logged_in'] = True

print('---------Logged in----------')
view_profile()