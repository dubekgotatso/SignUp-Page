from .. import mongo

class User:

    def create_user(signupdetails):
        mongo.db.signup.insert_one(signupdetails)
        return str(signupdetails)
    
    # def find_by_username_or_email(self, username, email):
    #     return mongo.db.signup.find_one({'$or': [{'username': username}, {'email': email}]})

    def get_all_login():
        signup = mongo.db.signup.find_one(signup)
        return list(mongo.db.signup.find({}, {'_id', 0}))
    
  