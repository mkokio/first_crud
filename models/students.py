from database import db

#represent database structure as classes
#each class is going to be it's own table in the database (only one table for now)
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #data type is integer, unique to each person
    first_name = db.Column(db.String(26), unique=True, nullable=False)
    #max 26 characters, each unique, can't be blank
    email = db.Column(db.String(80), unique=True, nullable=False)
    #max 26 characters, each unique, can't be blank
    
    def __repr__(self): #makes a string representation of an object
        return f"Student('{self.first_name}','{self.email}')"