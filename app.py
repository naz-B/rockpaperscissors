from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

choices = ["Rock", "Paper", "Scissors"]
facts = [
    "Rock-Paper-Scissors is believed to have originated in China over 2,000 years ago.",
    "The game is known as 'Janken' in Japan.",
    "Rock-Paper-Scissors is often used as a decision-making tool.",
    "There are international Rock-Paper-Scissors tournaments.",
    "In some variations, additional moves like 'Lizard' and 'Spock' are included."
]


def play(user_choice, computer_choice):
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif user_choice == "Rock" and computer_choice == "Scissors":
        result = "You win!"
    elif user_choice == "Paper" and computer_choice == "Rock":
        result = "You win!"
    elif user_choice == "Scissors" and computer_choice == "Paper":
        result = "You win!"
    else:
        result = "You lose!"
    return result


@app.route('/')
def index():
    return render_template('index.html',facts=facts)


@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/result', methods=['POST'])
def result():
    user_choice = request.form['choice']
    computer_choice = random.choice(choices)
    result = play(user_choice, computer_choice)
    return render_template('result.html', user_choice=user_choice, computer_choice=computer_choice, result=result)


if __name__ == '__main__':
    app.run(host='https://rockpaperscissors-phxk.onrender.com', port=8080)
