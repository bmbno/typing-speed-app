import tkinter as tk


class Gui:
    def __init__(self, master):
        self.master = master
        master.title("Type Speed Tester")

        self.text_entry_box_title = tk.Label(
            master, text="Type here to start").pack()
        self.text_entry_box = tk.Entry(master).pack()
        self.reset_button = tk.Button(master, text="Reset",
                                      command=self.reset).pack(side="bottom")

    def reset(self):
        return


def main():
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()


if __name__ == '__main__':
    main()
