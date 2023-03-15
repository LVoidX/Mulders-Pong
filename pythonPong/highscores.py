import sys
import turtle
import time
import end_screen
import tkinter
import start_screen

# Get the player's score from the end_screen module
player_score = end_screen.highscore

turtle.bye()


# Save the player's score to a file
def save_highscore():
    player_name = name_entry.get()
    if player_name:
        with open("highscores.txt", "a") as file:
            file.write(player_name + ": " + str(player_score) + "\n")
        save_button.config(state=tkinter.DISABLED)
        message_label.config(text="Highscore saved!:\n " + player_name + ": " + str(player_score))
        time.sleep(2)
        sys.exit()


# Tkinter
window = tkinter.Tk()
window.title(start_screen.game_name)
window.geometry("300x175")

# Create a label and entry field for the player's name
name_label = tkinter.Label(window, text="What is your name?")
name_label.pack(pady=10)
name_entry = tkinter.Entry(window)
name_entry.pack(pady=5)

# Create a button to save the highscore
save_button = tkinter.Button(window, text="Save Highscore", command=save_highscore)
save_button.pack(pady=5)

# Create a label to display a message after saving the highscore
message_label = tkinter.Label(window, text="")
message_label.pack(pady=5)

# Start the tkinter event loop
window.mainloop()

# Read the contents of the file into a list of tuples
with open("highscores.txt", "r") as file:
    highscores = [tuple(line.strip().split(": ")) for line in file]

# Sort the list in descending order by score
highscores.sort(key=lambda x: int(x[1]), reverse=True)

# Print the top 10 highscores and find the player's score
player_place = None
print("----- TOP 10 HIGHSCORES -----")
for i, (name, score) in enumerate(highscores[:10]):
    print(f"{i + 1}. {name}: {score}")
    if player_name == name:
        player_place = i + 1

# Print the player's place in the highscores
if player_place is not None:
    print(f"\nYou are in place number {player_place}!")
else:
    print("\nYour score was not found in the highscores.")
turtle.bye()
sys.exit()
