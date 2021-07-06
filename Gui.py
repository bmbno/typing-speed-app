import tkinter as tk
from Game import Game
import time


class Gui:
    """
    A class to display the game
    """

    def __init__(self, root):
        """
        Constructs the game gui

        Args:
            root (Class): the root of the gui loop
        """
        self.root = root
        root.title("Type Speed Tester")
        self.game = Game()
        self.time = 0.0

        # The displayed multiline sentence
        self.sentence = tk.Text(root, wrap="word")
        self.sentence.insert(tk.INSERT, self.game.choose_sentence())
        self.sentence.pack(expand=True, fill="both")

        # The entry box to type the attempt
        self.text_entry_box_title = tk.Label(
            root, text="Type here and press enter to submit").pack()
        self.text_entry_box = tk.Entry(root)
        self.text_entry_box.pack(fill="both")
        self.text_entry_box.bind('<Key>', self.start_timer())
        self.text_entry_box.bind(
            '<Return>', (lambda event: self.display_popup(self.text_entry_box.get(), self.sentence.get(1.0, 'end-1c'), self.time, time.time())))

        # The reset button to restart the game
        self.reset_button = tk.Button(root, text="Reset",
                                      command=self.reset).pack(side="bottom")

    def start_timer(self):
        """Sets the start time of the attempt"""
        self.time = time.time()

    def reset(self):
        """Resets the displayed sentence, clears the entry box, and sets the time to 0"""
        self.sentence.delete(1.0, "end")
        self.sentence.insert(tk.INSERT, self.game.choose_sentence())
        self.sentence.pack(expand=True)
        self.text_entry_box.delete(0, "end")
        self.time = 0.0
        self.text_entry_box.bind('<Key>', self.start_timer())

    def display_popup(self, entry, sentence, start_time, end_time):
        """
        Creates a pop-up with the attempt results

        Args:
            entry (string): the the typed sentence
            sentence (string): the sentence to be typed
            start_time (float): the start time of the attempt
            end_time (float): the end time of the attempt
        """
        # constructs the pop-up
        popup = tk.Toplevel(self.root)
        popup.title("Results")
        total_time = self.game.calculate_time(start_time, end_time)
        accuracy, wpm = self.game.calculate_score(
            start_time, end_time, sentence, entry)

        # Displays the result
        results = tk.Text(popup, wrap="word")
        results.insert(tk.INSERT, f"""
        Sentence: {sentence}
        Your attempt: {entry}
        
        Your score is:
        # Time: {total_time[0]} minutes {total_time[1]} seconds
        # Accuracy: {accuracy:.1f}%
        # WPM: {wpm:.2f}
        """)
        results.pack()
