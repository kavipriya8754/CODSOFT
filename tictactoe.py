import tkinter as tk
from tkinter import messagebox
from tkinter import font
import random

# Initialize the board
board = [" " for _ in range(9)]

# Check if a player has won
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

# Check if the board is full
def is_full(board):
    return " " not in board

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 10 - depth
    if check_winner(board, "X"):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

# AI's move
def best_move():
    best_score = -float("inf")
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Handle button clicks
def on_click(index):
    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X", state=tk.DISABLED, disabledforeground="#1E88E5")
        if check_winner(board, "X"):
            messagebox.showinfo("Tic-Tac-Toe", "You win!")
            reset_game()
            return
        elif is_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_game()
            return

        # AI's turn
        ai_index = best_move()
        board[ai_index] = "O"
        buttons[ai_index].config(text="O", state=tk.DISABLED, disabledforeground="#F4511E")
        if check_winner(board, "O"):
            messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
            reset_game()
            return
        elif is_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_game()
            return

# Reset the game
def reset_game():
    global board, buttons
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ", state=tk.NORMAL)

# GUI setup
window = tk.Tk()
window.title("Tic-Tac-Toe AI")
window.geometry("400x500")
window.resizable(False, False)
window.configure(bg="#263238")

# Title label
title_label = tk.Label(
    window, text="Tic-Tac-Toe AI", font=("Helvetica", 24, "bold"),
    bg="#263238", fg="#FFFFFF"
)
title_label.pack(pady=20)

# Create game frame
frame = tk.Frame(window, bg="#263238")
frame.pack()

# Initialize buttons
buttons = []
for i in range(3):
    for j in range(3):
        index = i * 3 + j
        button = tk.Button(
            frame, text=" ", font=("Helvetica", 20, "bold"),
            width=5, height=2, relief="flat", bg="#37474F", fg="#FFFFFF",
            activebackground="#455A64", activeforeground="#FFFFFF",
            command=lambda idx=index: on_click(idx)
        )
        button.grid(row=i, column=j, padx=5, pady=5)
        buttons.append(button)

# Reset button
reset_button = tk.Button(
    window, text="Reset Game", font=("Helvetica", 14),
    width=15, bg="#1E88E5", fg="#FFFFFF", relief="flat",
    command=reset_game
)
reset_button.pack(pady=20)

# Footer label
footer_label = tk.Label(
    window, text="Developed by AI Enthusiasts", font=("Helvetica", 10, "italic"),
    bg="#263238", fg="#B0BEC5"
)
footer_label.pack(side=tk.BOTTOM, pady=10)

# Run the application
window.mainloop()
