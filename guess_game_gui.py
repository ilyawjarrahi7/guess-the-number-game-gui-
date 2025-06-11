import tkinter as tk
import random

secret_number = random.randint(0, 100)
guess_count = 0
max_tries = 10
game_over = False

#check the guess func

def check_guess():
    global guess_count, game_over
   
    if game_over :
        return
    
    
    guess = entry.get()
    try:
        guess = int(guess)
        guess_count += 1
        if guess < secret_number:
            result_label.config(text="Too low",fg="red")
        elif guess > secret_number :
            result_label.config(text="Too high", fg="red")
        elif guess == secret_number:
            result_label.config(
                text=f"Correct! You gussed it in {guess_count} tries.",
                fg="green"
                )
            game_over = True
            guess_button.config(state="disabled")

        if guess_count == max_tries and guess != secret_number:
            result_label.config(
                text=f"Out of tries! The number was {secret_number}",
                fg="orange"
            )
            game_over = True
            guess_button.config(state="disable")

    except ValueError:
        result_label.config(text="Please enter a valid number.",fg="gray")  
    entry.delete(0, tk.END)    


def new_game():
    global secret_number, guess_count,game_over
    secret_number = random.randint(0, 100)
    guess_count = 0
    game_over = False
    result_label.config(text="New game started! Enter your guess: ",fg="black")
    guess_button.config(state="normal")
    entry.delete(0,tk.END)





root = tk.Tk()
root.title("Guess The Number")
root.geometry("300x250")


tk.Label(root, text="Enter your guess (1-100):",font=("Arial",12)).pack(pady=10)
entry = tk.Entry(root,font=("Arial",12))
entry.pack()

guess_button = tk.Button(root, text="Guess",command=check_guess).pack(pady=5)

result_label = tk.Label(root, text="Start guessing!",font=("Arial", 12))
result_label.pack(pady=10)

tk.Button(root, text="New game",command=new_game,font=("Arial",12)).pack(pady=5)

root.mainloop()