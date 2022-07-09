from flask import Flask, render_template, request, redirect
from app import app
from models.player import Player
from models.game import Game, get_computer_choice

@app.route('/play')
def index():
    return render_template('index.html')

# @app.route('/play/<player1_choice>/<player2_choice>')
# def game(player1_choice, player2_choice):
#     player1 = Player("player 1", player1_choice)
#     player2 = Player("player 2", player2_choice)
#     game = Game(player1, player2)
#     game.getResult()
#     return render_template('game.html', game=game)


@app.route('/play', methods=["POST"])
def clicked_play():
    if request.method == "POST" and "user_selection" in request.form:
        user_choice = request.form["user_selection"]
        user_name = request.form["user_name"]

        user = Player(user_name, user_choice)
        computer_choice = get_computer_choice()
        computer = Player("Computer", computer_choice)

        game = Game(user, computer)
        game.getResult()
        print(game.result)
        return render_template('game.html',user_choice=user_choice, user_name=user_name, computer_choice=computer.player_choice, result=game.result, user_score=game.player1_score, computer_score=game.player2_score)

    else:
        return render_template('game.html')

