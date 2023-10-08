import tkinter as tk
from random import randint
from datetime import datetime

class DiceGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Game")
        self.master.geometry("400x550")

        # Define pastel color codes
        self.pastel_blue = "#add8e6"
        self.pastel_pink = "#ffb6c1"
        self.pastel_green = "#98fb98"

        # build t gui
        self.label = tk.Label(self.master, font=("Arial", 100), text="🎁", bg=self.pastel_blue)
        self.label.pack(pady=50)


        self.name_label = tk.Label(self.master, text="Enter Your Name:", font=("Arial", 14))
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(self.master, font=("Arial", 14), bg=self.pastel_pink)
        self.name_entry.pack(pady=20)

        self.roll_button = tk.Button(self.master, text="Roll Dice", font=("Arial", 16), command=self.roll_dice, bg=self.pastel_green)
        self.roll_button.pack(pady=20)

        self.show_scores_button = tk.Button(self.master, text="Show Scores", font=("Arial", 16), command=self.show_scores, bg=self.pastel_pink)
        self.show_scores_button.pack(pady=20)


        # like a global
        self.click_count = 0
        self.accumulated_score = 0
        self.game_over = False
        self.player_name = None
        self.lines = []
        self.updated = False
        self.users = []

    def roll_dice(self):
        if self.click_count >= 5:
            self.game_over = True

        if not self.game_over:
            """logic of gameplay
                each click on  the button run this func

            """
            self.player_name = self.name_entry.get() if self.name_entry.get() else "Anonymous" # TODO:  can be changed each click; or stop disable after first click
            # if self.player_name:
                # self.name_entry.unbind(sequence=False) # update config canvas
            dice_num = randint(1, 6)
            self.accumulated_score += dice_num


            dice_image = ["❶", "❷", "❸", "❹", "❺", "❻"][dice_num - 1]
            self.label.config(text=dice_image)

            self.click_count += 1
        else:
            self.update_score_in_log(username=self.player_name, score=self.accumulated_score)
            self.roll_button.config(state=tk.DISABLED)
            self.label.config(text='Game Over', font=("Arial", 16))


    # def update_score_in_log(self, username, score):
    def update_score_in_log(self, username, score):
        self.open_log()

        # users = [] # затычка
        for idx, line in enumerate(self.lines):
            try:
                cur_username = line.split(", ")[1].split(": ")[1]
            except Exception:
                cur_username = 'not found username'
            try:
                cur_score = line.split('Score:')[-1]
            except Exception:
                cur_score = 'not found score'
            self.users.append(cur_username) # Затычка
            if (username == cur_username) and (score > int(line.split('Score:')[1])):
                self.lines[idx] = self.entry_log(line=line, score=score)
                break

        if username not in self.users:
            self.updated = True

        if self.updated:
            self.lines.append(self.entry_log(username=username, score=score))
        
        self.save_log()


    def show_scores(self):
        scores_window = tk.Toplevel(self.master)
        scores_window.title("Player Scores")
        scores_text = "\n".join([f"Name: {self.player_name}, Score: {self.accumulated_score}"])
        scores_label = tk.Label(scores_window, text=scores_text, font=("Arial", 14))
        scores_label.pack(padx=20, pady=20)

    # utils to log
    def open_log(self):
        with open('temp.txt', 'r') as file:
            self.lines = file.readlines()
        
    def entry_log(self, line=None, score=None, username=None):
        """generate report to row of the log file"""
        if username is not None:
            report = ', '.join([datetime.now().strftime('%Y/%m/%d')] + [f"Name: {username}"] +  [f"Score: {score}"]) + '\n' # using join easy to auto add comma
        else:
            report = ', '.join(line.split(", ")[:-1] + [f'Score: {score}']) + '\n'
        return report

    def save_log(self):
        if self.lines is not None:
            with open('temp.txt', 'w') as file:
                file.writelines(self.lines)
        else:
            raise FileExistsError("log file doesn't exist.")


if __name__ == "__main__":
    root = tk.Tk()
    app = DiceGame(root)
    root.mainloop()
