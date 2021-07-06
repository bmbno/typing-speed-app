import tkinter as tk
from tkinter.constants import END
from Game import Game


class Gui:
    def __init__(self, root):
        self.root = root
        root.title("Type Speed Tester")
        self.game = Game()
        self.sentence = tk.Text(root)
        self.sentence.insert(tk.INSERT, self.game.choose_sentence())
        self.sentence.pack()
        self.text_entry_box_title = tk.Label(
            root, text="Type here and press enter to submit").pack()
        self.text_entry_box = tk.Entry(root)
        self.text_entry_box.pack()
        self.reset_button = tk.Button(root, text="Reset",
                                      command=self.reset).pack(side="bottom")

    def reset(self):
        self.sentence.delete(1.0, END)
        self.sentence.insert(tk.INSERT, self.game.choose_sentence())
        self.sentence.pack()
        self.text_entry_box.delete(0, END)

    def get_entry(self, entry):
        entry.get()


def main():
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()


if __name__ == '__main__':
    main()
