from config import db
import json

class  User(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    username = db.Column(db.String(80), unique=False, nullable=False)
    
    def to_json(self):   
        return {
            "id": self.id,
            "username": self.username
        }
    
class Questions(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)
    options = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.Integer, nullable=False)
    
    def get_options(self):
        return json.loads(self.options)
    
    
    def to_json(self):
        return {
            'id': self.id,
            'question_text': self.question_text,
            'options': self.get_options(), 
            'correct_answer': self.correct_answer
        }
        
class REELS(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)
    options = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.Integer, nullable=False)
    
    def get_options(self):
        return json.loads(self.options)
    
    
    def to_json(self):
        return {
            'id': self.id,
            'question_text': self.question_text,
            'options': self.get_options(), 
            'correct_answer': self.correct_answer
        }
    