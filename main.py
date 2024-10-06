from flask import Flask, request, jsonify, render_template
from config import app
import csv, json
import subprocess
import os

    
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


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")
@app.route("/quiz1")
def quiz1(): 
    return render_template("quiz1.html")

@app.route("/api/questions")
def something():
     File = []
     with open('questions.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            question_text = row[0]
            options = json.dumps(row[1:5])  
            correct_answer = row[5]
            
            temp = {
                 'question_text': question_text,              
                 'options': json.loads(options), 
                 'correct_answer': correct_answer
            }
            
            File.append(temp)
        return File
         
@app.route("/api/questions1")
def ssomething():
     File = []
     with open('question_reel.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            question_text = row[0]
            options = json.dumps(row[1:5])  
            correct_answer = row[5]
            
            temp = {
                 'question_text': question_text,              
                 'options': json.loads(options), 
                 'correct_answer': correct_answer
            }
            
            File.append(temp)
        return File


    
    
if __name__ == "__main__":
    app.run(debug=True)
