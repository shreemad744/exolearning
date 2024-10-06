from flask import Flask, request, jsonify, render_template
from config import app, db
from models import User, Questions, REELS
import csv, json
import subprocess
import os
def add_questions_from_csv(filename):
   
    Questions.query.delete()
    db.session.commit()

   
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            question_text = row[0]
            options = json.dumps(row[1:5])  
            correct_answer = row[5]

            question = Questions(question_text=question_text, options=options, correct_answer=correct_answer)
            db.session.add(question)

    db.session.commit()
    
def add_questions_from_csv_reel(filename):
   

    REELS.query.delete()
    db.session.commit()
   
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            question_text = row[0]
            options = json.dumps(row[1:5])  
            correct_answer = row[5]

            question1 = REELS(question_text=question_text, options=options, correct_answer=correct_answer)
            db.session.add(question1)

    db.session.commit()
    
@app.route('/')
@app.route('/home')
def home():
    return render_template("home/index.html")

@app.route('/video')
def video():
    return render_template("videos/index.html")

@app.route("/start-quiz")
def QuizStart():
    return render_template("start_quiz.html")

@app.route("/reels")
def reels():
    return render_template("/reels/index.html")

@app.route("/flashcard")
def flashcard():
    return render_template("flashcard/flashcard.html")

@app.route("/simulation")
def simulation():
    return render_template("Simulator/hello.html")

@app.route("/api/questions1", methods=["GET"])
def get_questions1():
    questions = REELS.query.all()
    json_data = list(map(lambda x: x.to_json(), questions))
    return jsonify(json_data)

@app.route("/api/questions", methods=["GET"])
def get_questions():
    questions = Questions.query.all()
    json_data = list(map(lambda x: x.to_json(), questions))
    return jsonify(json_data)


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")
@app.route("/quiz1")
def quiz1(): 
    return render_template("quiz1.html")


@app.route("/user", methods=["GET"])
def get_users():
    user = User.query.all()
    json_data = list(map(lambda x: x.to_json(),user))
    return jsonify({"user": json_data})


@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.json.get("username")
    
    if not username:
        return (jsonify({"message": "include a username"}),
                400)
    
    new_user = User(username=username)
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return (jsonify({"message":str(e)}),400)

    return jsonify({"message":"User Created"}),201
    
    
app.route("/update_user/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message":"User not found"}), 404
    
    user.username = request.json.get("username",user.username)
    
    db.session.commit()
    return jsonify({"message":"User Updated"}),200


app.route("/delete_user/<int:user_id>",methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message":"User not found"}), 404
    
    db.session.delete(user)
    
    db.session.commit()
    return jsonify({"message":"User Deleted"}),200
    
    
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        add_questions_from_csv('questions.csv')
        add_questions_from_csv_reel('question_reel.csv')
       
    app.run(debug=True)