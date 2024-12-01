import tkinter as tk
import random

player_points = 0
bot_points = 0
choices = ["rock", "paper", "scissors"]

def player_choice(choice):
    global bot_choice, result_label
    bot_choice = random.choice(choices)
    #result_label.config(text=f"Bot chose: {bot_choice}", fg="blue")
    check_winner(choice, bot_choice)
    change_points()

def change_points():
    global player_points_label, bot_points_label, player_points, bot_points
    player_points_label.config(text=f"Player points: {player_points}")
    bot_points_label.config(text=f"Bot points: {bot_points}")

def check_winner(player, bot):
    global player_points, bot_points, result_label
    if player == bot:
        result = "It's a tie!"
    elif (player == "rock" and bot == "scissors") or \
         (player == "paper" and bot == "rock") or \
         (player == "scissors" and bot == "paper"):
        result = "You win!"
        player_points += 1
    else:
        result = "Bot wins!"
        bot_points += 1
    
    if result == "It's a tie!":
        result_label.config(text=f"The bot chose {bot_choice}.\n{result}", fg="blue")
    elif result == "You win!":
        result_label.config(text=f"The bot chose {bot_choice}.\n{result}", fg="green")
    else:
        result_label.config(text=f"The bot chose {bot_choice}.\n{result}", fg="red")

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("800x600")
window.configure(bg="azure")

title = tk.Label(window, text="Rock Paper Scissors", fg="black", bg="azure", font=("Helvetica", 40, "bold"))
title.pack(pady=50)

button_frame = tk.Frame(window, bg="azure")
button_frame.pack(pady=30)

result_label = tk.Label(window, text="", fg="black", bg="azure", font=("Helvetica", 25, "italic"))
result_label.pack(pady=30)

player_points_label = tk.Label(window, text=f"Player points: {player_points}", fg="black", bg="azure", font=("Helvetica", 20, "bold"))
player_points_label.pack(pady=10)

bot_points_label = tk.Label(window, text=f"Bot points: {bot_points}", fg="black", bg="azure", font=("Helvetica", 20, "bold"))
bot_points_label.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", bg="ivory3", fg="black", font=("Helvetica", 20, "bold"), relief="groove", command=lambda:player_choice("rock"))
rock_button.grid(row=0, column=0, padx=20, pady=20)

paper_button = tk.Button(button_frame, text="Paper", bg="ivory3", fg="black", font=("Helvetica", 20, "bold"), relief="groove", command=lambda: player_choice("paper"))
paper_button.grid(row=0, column=1, padx=20, pady=20)

scissors_button = tk.Button(button_frame, text="Scissors", bg="ivory3", fg="black", font=("Helvetica", 20, "bold"), relief="groove", command=lambda: player_choice("scissors"))
scissors_button.grid(row=0, column=2, padx=20, pady=20)
 
footer = tk.Label(window, text="May the best win!", fg="black", bg="azure", font=("Helvetica", 20, "italic"))
footer.pack(pady=50)

window.mainloop()
